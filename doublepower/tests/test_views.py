from django.test import TestCase
from django.urls import reverse

from doublepower.models import Player, Team
from doublepower.forms import PlayerForm


class HomeTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('doublepower:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doublepower/home.html')

    def test_home_uses_player_form(self):
        response = self.client.get(reverse('doublepower:home'))

        self.assertIsInstance(response.context['player_form'], PlayerForm)

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            reverse('doublepower:new_team'),
            data={
                'name': 'Roger',
                'forehand_strength': 98,
                'backhand_strength': 91,
            }
        )
        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.name, 'Roger')

    def test_POST_redirects_to_team_view(self):
        response = self.client.post(
            reverse('doublepower:new_team'),
            data={
                'name': 'Raphael',
                'forehand_strength': 96,
                'backhand_strength': 67,
            }
        )
        new_team = Team.objects.first()
        self.assertRedirects(response, f'/doublepower/team/{new_team.id}')


class TeamViewTest(TestCase):

    def test_team_view_uses_team_template(self):
        team = Team.objects.create()

        response = self.client.get(f'/doublepower/team/{team.id}')

        self.assertTemplateUsed(response, 'doublepower/team.html')

    def test_can_save_a_POST_request_to_existing_team(self):
        team = Team.objects.create()
        Player.objects.create(team=team, name='Roger')
        Player.objects.create(team=team, name='Rafa')
        self.assertEqual(Player.objects.count(), 2)

        response = self.client.post(
            f'/doublepower/team/{team.id}',
            data={
                'name': 'Novak',
                'forehand_strength': 96,
                'backhand_strength': 67,
            }
        )

        self.assertEqual(Player.objects.count(), 3)
        new_player = Player.objects.last()
        self.assertEqual(new_player.name, 'Novak')

    def test_displays_all_players(self):
        correct_team = Team.objects.create()
        Player.objects.create(team=correct_team, name='Roger')
        Player.objects.create(team=correct_team, name='Rafa')
        Player.objects.create(team=correct_team, name='Novak')
        other_team = Team.objects.create()
        Player.objects.create(team=other_team, name='Ronaldo')
        Player.objects.create(team=other_team, name='Messi')

        response = self.client.get(f'/doublepower/team/{correct_team.id}')

        self.assertContains(response, 'Roger')
        self.assertContains(response, 'Rafa')
        self.assertContains(response, 'Novak')
        self.assertNotContains(response, 'Ronaldo')
        self.assertNotContains(response, 'Messi')


class TestMovePlayerUp(TestCase):

    def test_POST_redirects_to_team_view(self):
        team = Team.objects.create()
        player = Player.objects.create(team=team, name='Roger')

        response = self.client.post(
            f'/doublepower/team/{team.id}/player_up/{player.id}')

        self.assertRedirects(response, f'/doublepower/team/{team.id}')

    def test_POST_can_move_players_up_in_team(self):
        team = Team.objects.create()
        Player.objects.create(team=team, name='Roger')
        player = Player.objects.create(team=team, name='Novak')
        self.assertEqual(player.rank, 2)

        _ = self.client.post(
            f'/doublepower/team/{team.id}/player_up/{player.id}')

        player.refresh_from_db()
        self.assertEqual(player.rank, 1)

    def test_cannot_move_rank_up_of_player_with_rank_1(self):
        team = Team.objects.create()
        player = Player.objects.create(team=team, name='Roger')
        Player.objects.create(team=team, name='Rafa')

        _ = self.client.post(
            f'/doublepower/team/{team.id}/player_up/{player.id}')

        player.refresh_from_db()
        self.assertEqual(player.rank, 1)


class TestMovePlayerDown(TestCase):

    def test_POST_redirects_to_team_view(self):
        team = Team.objects.create()
        player = Player.objects.create(team=team, name='Roger')

        response = self.client.post(
            f'/doublepower/team/{team.id}/player_down/{player.id}')

        self.assertRedirects(response, f'/doublepower/team/{team.id}')

    def test_POST_can_move_players_down_in_team(self):
        team = Team.objects.create()
        player = Player.objects.create(team=team, name='Roger')
        Player.objects.create(team=team, name='Rafa')
        self.assertEqual(player.rank, 1)

        _ = self.client.post(
            f'/doublepower/team/{team.id}/player_down/{player.id}')

        player.refresh_from_db()
        self.assertEqual(player.rank, 2)

    def test_cannot_move_rank_down_of_player_with_lowest_rank(self):
        team = Team.objects.create()
        Player.objects.create(team=team, name='Roger')
        player = Player.objects.create(team=team, name='Rafa')

        _ = self.client.post(
            f'/doublepower/team/{team.id}/player_down/{player.id}')

        player.refresh_from_db()
        self.assertEqual(player.rank, 2)



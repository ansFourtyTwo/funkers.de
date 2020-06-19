from django.test import TestCase

from doublepower.models import Player, Team


class PlayerModelTest(TestCase):

    def test_can_save_player(self):
        team = Team.objects.create()
        player = Player(team=team)
        player.save()
        self.assertEqual(Player.objects.first(), player)

    def test_player_is_associated_to_team(self):
        team = Team.objects.create()
        player = Player()
        player.team = team
        player.save()
        self.assertIn(player, team.player_set.all())

    def test_default_player_name(self):
        player = Player()
        self.assertEqual(player.name, '')

    def test_default_player_forehand_strength(self):
        player = Player()
        self.assertEqual(player.forehand_strength, 50)

    def test_default_player_backhand_strength(self):
        player = Player()
        self.assertEqual(player.backhand_strength, 50)

    def test_default_player_rank(self):
        player = Player()
        self.assertEqual(player.rank, 1)

    def test_saving_player_adds_rank_attribute_correctly(self):
        team = Team.objects.create()
        player1 = Player.objects.create(team=team)
        player2 = Player.objects.create(team=team)
        self.assertEqual(player1.rank, 1)
        self.assertEqual(player2.rank, 2)

    def test_updating_player_does_not_change_rank(self):
        team = Team.objects.create()
        player1 = Player.objects.create(team=team)
        _ = Player.objects.create(team=team)
        player1.name = 'Pete Sampras'
        player1.save()
        self.assertEqual(player1.rank, 1)


class TeamModelTest(TestCase):

    def test_get_absolute_url(self):
        team = Team.objects.create()
        self.assertEqual(
            team.get_absolute_url(),
            f'/doublepower/team/{team.id}'
        )

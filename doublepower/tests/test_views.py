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
            reverse('doublepower:new_player'),
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

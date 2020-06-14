from django.test import TestCase
from django.urls import reverse

from doublepower.models import Player
from doublepower.forms import PlayerForm


class IndexTest(TestCase):

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

from django.test import TestCase
from django.urls import reverse

from doublepower.forms import PlayerForm


class IndexTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('doublepower:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doublepower/home.html')

    def test_home_uses_player_form(self):
        response = self.client.get(reverse('doublepower:home'))
        self.assertIsInstance(response.context['player_form'], PlayerForm)

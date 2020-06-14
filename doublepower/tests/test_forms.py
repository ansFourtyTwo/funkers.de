from django.test import TestCase

from doublepower.forms import PlayerForm


class PlayerFormTest(TestCase):

    def test_player_form_renders_name_text_input(self):
        player_form = PlayerForm()
        self.assertIn(
            'id="id_name"',
            player_form.as_p()
        )
        self.assertIn(
            'placeholder="Please enter a player name"',
            player_form.as_p()
        )

    def test_player_form_renders_forehand_strength_input(self):
        player_form = PlayerForm()
        self.assertIn(
            'id="id_forehand_strength"',
            player_form.as_p()
        )

    def test_player_form_renders_backhand_strength_input(self):
        player_form = PlayerForm()
        self.assertIn(
            'id="id_backhand_strength"',
            player_form.as_p()
        )

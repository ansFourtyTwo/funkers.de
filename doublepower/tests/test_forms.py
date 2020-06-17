from django.test import TestCase

from doublepower.models import Team, Player
from doublepower.forms import PlayerForm, ExistingTeamPlayerForm


class PlayerFormTest(TestCase):

    def test_player_form_save_handles_saving_to_a_team(self):
        team = Team.objects.create()
        player_form = PlayerForm(data={
            'name': 'Pete Sampras',
            'forehand_strength': 76,
            'backhand_strength': 44,
        })
        new_player = player_form.save(team=team)
        self.assertEqual(new_player, Player.objects.first())
        self.assertEqual(new_player.name, 'Pete Sampras')
        self.assertEqual(new_player.forehand_strength, 76)
        self.assertEqual(new_player.backhand_strength, 44)
        self.assertEqual(new_player.team, team)

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


class TestExistingTeamPlayerForm(TestCase):

    def test_form_save(self):
        team = Team.objects.create()
        existing_team_player_form = ExistingTeamPlayerForm(team=team, data={
            'name': 'Pete Sampras',
            'forehand_strength': 76,
            'backhand_strength': 44,
        })
        new_player = existing_team_player_form.save()
        self.assertEqual(new_player, Player.objects.first())


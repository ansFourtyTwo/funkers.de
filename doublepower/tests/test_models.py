from django.test import TestCase

from doublepower.models import Player


class PlayerModelTest(TestCase):

    def test_can_save_player(self):
        player = Player()
        player.save()
        self.assertEqual(Player.objects.first(), player)

    def test_default_player_name(self):
        player = Player()
        self.assertEqual(player.name, '')

    def test_default_player_forehand_strength(self):
        player = Player()
        self.assertEqual(player.forehand_strength, 50)

    def test_default_player_backhand_strength(self):
        player = Player()
        self.assertEqual(player.backhand_strength, 50)
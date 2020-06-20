from django.core.exceptions import ObjectDoesNotExist

from .base import FunctionalTest


class TeamManipulationTest(FunctionalTest):

    def test_rearrange_team_ranking(self):
        # Simon visits the site and enters some players for analysis
        self.browser.get(self.live_server_url)

        self.enter_player(
            name='Raphael Nadal',
            forehand_strength=65,
            backhand_strength=86,
        )

        self.enter_player(
            name='Roger Federer',
            forehand_strength=95,
            backhand_strength=70,
        )

        self.enter_player(
            name='Novak Djokovic',
            forehand_strength=80,
            backhand_strength=90,
        )

        # Initial ranking is:
        # 1 Raphael Nadal
        # 2 Roger Federer
        # 3 Novak Djokovic

        # Unfortunately this is not the real ranking order, but wait,
        # there is help: Beside the players in the he finds buttons for each
        # player, which he can use to manipulate the ranking

        # Simon clicks on the "UP" button next to Novak Djokovic to bring him
        # up in the ranking
        self.get_player_button('Novak Djokovic', 'Up').click()

        # He notices, that Novak Djokovic has moved up on position in the
        # ranking
        self.wait_for_row_in_player_table('1 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('2 Novak Djokovic 80 90')
        self.wait_for_row_in_player_table('3 Roger Federer 95 70')

        # Still Novak isn't in first position, rank him up!!
        self.get_player_button('Novak Djokovic', 'Up').click()

        # There we go, Novak is at the top
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')
        self.wait_for_row_in_player_table('2 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('3 Roger Federer 95 70')

        # Bring him up to heaven ...
        self.get_player_button('Novak Djokovic', 'Up').click()

        # Nope! There is nothing better than rank 1.
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')

        # One final thing to do. Nadal is not as good as Federer. Rank him
        # down to rank 3.
        self.get_player_button('Raphael Nadal', 'Down').click()

        # Perfect. Federer is now rank 2, Nadal is only on rank 3
        self.wait_for_row_in_player_table('2 Roger Federer 95 70')
        self.wait_for_row_in_player_table('3 Raphael Nadal 65 86')

    def test_delete_player_from_team(self):
        # Simon visits the site and enters some players for analysis
        self.browser.get(self.live_server_url)

        self.enter_player(
            name='Raphael Nadal',
            forehand_strength=65,
            backhand_strength=86,
        )

        self.enter_player(
            name='Roger Federer',
            forehand_strength=95,
            backhand_strength=70,
        )

        self.enter_player(
            name='Novak Djokovic',
            forehand_strength=80,
            backhand_strength=90,
        )

        # He decides, that Federer should not be part of the analysis and
        # removes him from the team
        self.get_player_button('Roger Federer', 'Delete').click()

        # Only Nadal and Djokovic remain in the team
        self.wait_for_row_in_player_table('1 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('2 Novak Djokovic 80 90')

        # He also doesn't want Nadal in the analysis
        self.get_player_button('Raphael Nadal', 'Delete').click()

        # Only Djokovic left
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')

        # Wait what? He deletes Djokovic from the team
        self.get_player_button('Novak Djokovic', 'Delete').click()

        # After all that players are gone, Simon is now back at the home
        # site, where he can start adding a player and thus creating a new team
        self.assertEqual(self.browser.current_url, f'{self.live_server_url}/')


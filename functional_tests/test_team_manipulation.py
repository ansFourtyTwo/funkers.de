import time
from selenium.common.exceptions import WebDriverException
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
        self.rank_player_up_button('Novak Djokovic').click()

        # He notices, that Novak Djokovic has moved up on position in the
        # ranking
        self.wait_for_row_in_player_table('1 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('2 Novak Djokovic 80 90')
        self.wait_for_row_in_player_table('3 Roger Federer 95 70')

        # Still Novak isn't in first position, rank him up!!
        self.rank_player_up_button('Novak Djokovic').click()

        # There we go, Novak is at the top
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')
        self.wait_for_row_in_player_table('2 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('3 Roger Federer 95 70')

        # Bring him up to heaven ...
        self.rank_player_up_button('Novak Djokovic').click()

        # Nope! There is nothing better than rank 1.
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')

        # One final thing to do. Nadal is not as good as Federer. Rank him
        # down to rank 3.
        self.rank_player_down_button('Raphael Nadal').click()

        # Perfect. Federer is now rank 2, Nadal is only on rank 3
        self.wait_for_row_in_player_table('2 Roger Federer 95 70')
        self.wait_for_row_in_player_table('3 Raphael Nadal 65 86')


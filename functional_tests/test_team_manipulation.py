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

        # He notices, that the players are ranked how they were entered
        self.wait_for_row_in_player_table('1 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('2 Roger Federer 95 70')
        self.wait_for_row_in_player_table('3 Novak Djokovic 80 90')

        # Unfortunately this is not the real ranking order, but wait,
        # there is help: Beside the players in the he finds buttons for each
        # player, which he can use to manipulate the ranking
        table = self.browser.find_element_by_id('id_player_table')
        rows = table.find_elements_by_tag_name('tr')

        # Simon clicks on the "UP" button next to Novak Djokovic to bring him
        # up in the ranking
        for row in rows:
            if 'Novak Djokovic' in row.text:
                up_button = row.find_element_by_xpath(".//input[@value='Up']")
                up_button.click()

        # He notices, that Novak Djokovic has moved up on position in the
        # ranking
        self.wait_for_row_in_player_table('1 Raphael Nadal 65 86')
        self.wait_for_row_in_player_table('2 Novak Djokovic 80 90')
        self.wait_for_row_in_player_table('3 Roger Federer 95 70')

        self.fail("Finish me! Development driven tests here ;)!")

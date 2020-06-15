from selenium import webdriver

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_team_for_one_user(self):
        # Simon has heard of a new web application called Doublepower where
        # he can analyse double formations of tennis teams. He decides to go
        # to the home page
        self.browser.get(self.live_server_url)

        # He notices that the page title and header mentions "Doublepower"
        self.assertIn('Doublepower', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Doublepower', header_text)

        # For analysis it is required to enter several tennis players,
        # so he starts to enter the first player.

        # To enter a new player he finds a textfield where he can enter the
        # name of the player
        input_player_name = self.browser.find_element_by_id('id_name')
        self.assertEqual(
            input_player_name.get_attribute('placeholder'),
            "Please enter a player name"
        )

        # He enters the first player
        self.enter_player(
            name='Novak Djokovic',
            forehand_strength=80,
            backhand_strength=90,
        )
        # He notices that he got redirected to a unique URL for viewing the
        # complete team
        current_url = self.browser.current_url
        self.assertRegex(current_url, r'/team/\d+')

        # After submission of the first player he can see the player's
        # information in a table below. The table also contains a rank
        self.wait_for_row_in_player_table('1 Novak Djokovic 80 90')

        # The player is listed at rank #1 as no other player is entered.

        # Simon notices that the form for entering new players is still
        # there and starts to enter a second player
        self.enter_player(
            name='Roger Federer',
            forehand_strength=95,
            backhand_strength=80,
        )

        # He notices that this player also appears on the table
        self.wait_for_row_in_player_table('2 Roger Federer 95 80')

        # Satisfied Simon goes to sleep

    def test_multiple_user_can_start_teams_at_different_urls(self):
        # Simon starts a new team
        self.browser.get(self.live_server_url)

        self.enter_player(
            name='Novak Djokovic',
            forehand_strength=80,
            backhand_strength=90,
        )
        self.enter_player(
            name='Roger Federer',
            forehand_strength=95,
            backhand_strength=80,
        )

        # He notices that he got redirected to a unique URL for viewing the
        # complete team
        simons_url = self.browser.current_url
        self.assertRegex(simons_url, r'/team/\d+')

        # Now a new user Max is coming along, creating a team on his own
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        # Max enters his players of choice
        self.enter_player(
            name='Pete Sampras',
            forehand_strength=77,
            backhand_strength=54,
        )
        self.wait_for_row_in_player_table('1 Pete Sampras 77 54')

        # Max gets his own unique URL
        max_url = self.browser.current_url
        self.assertRegex(max_url, r'/team/\d+')
        self.assertNotEqual(simons_url, max_url)

        # There is no sign of Simon's team on Max' team
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Novak Djokovic', page_text)
        self.assertNotIn('Roger Federer', page_text)

        # Satisfied they both go back to sleep








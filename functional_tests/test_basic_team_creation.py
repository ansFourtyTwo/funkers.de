from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_create_players_for_analysis(self):
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
        input_player_name.send_keys('Novac Djocovic')

        # Also he finds a form for numerical input to enter the forehand
        # strength of the player
        input_forehand_strength = self.browser.find_element_by_id(
            'id_forehand_strength')

        # He adjusts the strength by 30 to 80 for the forehand
        for i in range(30):
            input_forehand_strength.send_keys(Keys.ARROW_UP)

        # Same as for the forehand side is available for the backhand side
        input_backhand_strength = self.browser.find_element_by_id(
            'id_backhand_strength')

        # He adjusts the strength by 40 to 90 for the backhand
        for i in range(40):
            input_backhand_strength.send_keys(Keys.ARROW_UP)

        # He clicks the submit button to finish the first player
        submit_button = self.browser.find_element_by_xpath(
            "//input[@type='submit' and @value='Submit']"
        )
        submit_button.click()

        # He notices that he got redirected to a unique URL for viewing the
        # complete team
        current_url = self.browser.current_url
        self.assertRegex(current_url, r'/team/\d+')

        # After submission of the first player he can see the player's
        # information in a table below. The table also contains a rank
        self.wait_for_row_in_player_table('1 Novac Djocovic 80 90')

        # The player is listed at rank #1 as no other player is entered.

        # Simon notices that the form for entering new players is still
        # there and starts to enter a second player
        input_player_name = self.browser.find_element_by_id('id_name')
        input_player_name.send_keys('Roger Federer')
        input_forehand_strength = self.browser.find_element_by_id(
            'id_forehand_strength')

        for i in range(45):
            input_forehand_strength.send_keys(Keys.ARROW_UP)

        input_backhand_strength = self.browser.find_element_by_id(
            'id_backhand_strength')

        for i in range(30):
            input_backhand_strength.send_keys(Keys.ARROW_UP)

        # He clicks the submit button to finish the second player
        submit_button = self.browser.find_element_by_xpath(
            "//input[@type='submit' and @value='Submit']"
        )
        submit_button.click()

        # He notices that this player also appears on the table
        self.wait_for_row_in_player_table('2 Roger Federer 95 80')

        # Satisfied Simon goes to sleep






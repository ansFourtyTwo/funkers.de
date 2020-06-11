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
        input_player_name = self.browser.find_element_by_id('id_player_name')
        self.assertEqual(
            input_player_name.get_attribute('placeholder'),
            "Please enter the player's name"
        )
        input_player_name.send_keys('Novac Djocovic')
        input.player_name.send_keys(Keys.ENTER)

        # Also he finds a vertical slider with values from 0 to 100 with step
        # size 1 and default to 50, where he can set the player's strength
        # for the forehand side
        input_forehand_strength = self.browser.find_element_by_id(
            'id_forehand_strength')
        self.assertEqual(input_forehand_strength.get_attribute('min'), 0)
        self.assertEqual(input_forehand_strength.get_attribute('max'), 100)
        self.assertEqual(input_forehand_strength.get_attribute('step'), 1)
        self.assertEqual(input_forehand_strength.get_attribute('value'), 50)

        # He adjusts the strength by 30 to 80 for the forehand
        for i in range(30):
            input_forehand_strength.send_keys(Keys.ARROW_RIGHT)

        # Same as for the forehand side is available for the backhand side
        input_backhand_strength = self.browser.find_element_by_id(
            'id_backhand_strength')
        self.assertEqual(input_backhand_strength.get_attribute('min'), 0)
        self.assertEqual(input_backhand_strength.get_attribute('max'), 100)
        self.assertEqual(input_backhand_strength.get_attribute('step'), 1)
        self.assertEqual(input_backhand_strength.get_attribute('value'), 50)

        # He adjusts the strength by 40 to 90 for the backhand
        for i in range(40):
            input_backhand_strength.send_keys(Keys.ARROW_RIGHT)

        # He clicks the submit button to finish the first player
        submit_button = self.browser.find_element_by_class_name("submit")
        submit_button.click()

        # After submission of the first player he can see the player's
        # information in a table below. The table also contains a rank

        # The player is listed at rank #1 as no other player is entered.

        # Simon starts to enter a second player

        self.fail("Finish the test")




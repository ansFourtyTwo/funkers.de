from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class FormAttributesTest(FunctionalTest):
    def test_player_form_has_correct_attributes(self):
        # Simon goes to the Doublepower homepage
        self.browser.get(self.live_server_url)

        # For the numerical input of the forehand strength he notices,
        # that he can enter only numbers between 0-100, with step size 1 and
        # that the default value is set to 50
        input_forehand_strength = self.browser.find_element_by_id(
            'id_forehand_strength')

        self.assertEqual(input_forehand_strength.get_attribute('min'), str(0))
        self.assertEqual(input_forehand_strength.get_attribute('max'), str(100))
        self.assertEqual(input_forehand_strength.get_attribute('step'), str(1))
        self.assertEqual(input_forehand_strength.get_attribute('value'),
                         str(50))

        # He notices that the same applies to the input field of the backhand
        # strength
        input_backhand_strength = self.browser.find_element_by_id(
            'id_backhand_strength')
        self.assertEqual(input_backhand_strength.get_attribute('min'), str(0))
        self.assertEqual(input_backhand_strength.get_attribute('max'), str(100))
        self.assertEqual(input_backhand_strength.get_attribute('step'), str(1))
        self.assertEqual(input_backhand_strength.get_attribute('value'),
                         str(50))

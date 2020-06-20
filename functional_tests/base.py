import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.live_server_url = f'{self.live_server_url}/doublepower'

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_player_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_player_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def enter_player(self, name, forehand_strength, backhand_strength):

        def set_strength(input_element, set_point):
            default_value = 50
            key = Keys.ARROW_UP if set_point > default_value else \
                Keys.ARROW_DOWN
            for _ in range(abs(set_point-default_value)):
                input_element.send_keys(key)

        input_player_name = self.browser.find_element_by_id('id_name')
        input_player_name.send_keys(name)

        input_forehand_strength = self.browser.find_element_by_id(
            'id_forehand_strength')
        set_strength(input_forehand_strength, forehand_strength)

        input_backhand_strength = self.browser.find_element_by_id(
            'id_backhand_strength')
        set_strength(input_backhand_strength, backhand_strength)

        submit_button = self.browser.find_element_by_xpath(
            "//input[@type='submit' and @value='Submit']"
        )
        submit_button.click()

    def rank_player_up_button(self, name):
        table = self.browser.find_element_by_id('id_player_table')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            if name in row.text:
                return row.find_element_by_xpath(".//input[@value='Up']")
        return None

    def rank_player_down_button(self, name):
        table = self.browser.find_element_by_id('id_player_table')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            if name in row.text:
                return row.find_element_by_xpath(".//input[@value='Down']")
        return None

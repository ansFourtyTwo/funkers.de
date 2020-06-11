from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.live_server_url = f'{self.live_server_url}/doublepower'

    def tearDown(self):
        self.browser.quit()

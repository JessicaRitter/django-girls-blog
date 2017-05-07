from django.test import LiveServerTestCase
from selenium import webdriver


class TestingButtonInBrowser(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.FireFox()

    def tearDown(self):
        self.browser.quit()

    def testButton(self):
        self.browser.get('http://jessicalynnritter.pythonanywhere.com/post/1/#collapseExample')

        button = self.browser.find_element_by_id('collapseButton')
        button.click()
        text = self.browser.find_element_by_id('collapseExample')
        self.assertTrue(text)



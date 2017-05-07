from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class TestingButtonInBrowser(LiveServerTestCase):

    def setUp(self):
        driver = webdriver.Chrome
        self.browser = driver()

    def tearDown(self):
        self.browser.quit()

    def testButton(self):
        driver = self.browser.get('http://jessicalynnritter.pythonanywhere.com/post/1/#collapseExample')
        driver_wait = WebDriverWait(driver, 60)
        try:
            driver_wait.until(EC.presence_of_element_located(By.ID('collapseButton')))
        except:
            pass
        button = self.browser.find_element_by_id('collapseButton')
        button.click()
        text = self.browser.find_element_by_id('collapseExample')
        self.assertTrue(text)



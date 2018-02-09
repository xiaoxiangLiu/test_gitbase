# coding=utf-8
from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs ={'download.default_directory': 'e:\\TWOSC_autotest\\TWOSC_autotest_web\\download\\',\
                "profile.managed_default_content_settings.images": 2}
        options.add_argument('disable-infobars')
        # options.add_argument('headless')
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()





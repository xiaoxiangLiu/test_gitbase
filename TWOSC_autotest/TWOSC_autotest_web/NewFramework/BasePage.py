__author__ = '38720'
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Page(object):

    url = 'http://menghua_test.dev.sjgtw.net:48097/'

    def __init__(self, driver, url=url):

        self.options = webdriver.ChromeOptions()
        prefs ={'download.default_directory': 'e:\\TWOSC_autotest\\TWOSC_autotest_web\\download\\'}
        self.options.add_argument('disable-infobars')
        self.options.add_experimental_option('prefs', prefs)
        self.driver = driver
        self.url = url

    def open_chrome(self):
        self.driver.get(self.url)

    def visibility_by_element(self, css='', xpath='', link_text=''):

        if css:
            return EC.visibility_of_element_located((By.CSS_SELECTOR, css))
        elif xpath:
            return EC.visibility_of_element_located((By.XPATH, xpath))
        elif link_text:
            return EC.visibility_of_element_located((By.LINK_TEXT, link_text))

    def window_by_index(self, num=-1):
        return self.driver.switch_to.window(self.driver.window_handles[num])

    def click_element(self, assert_word):
        return self.wait.until(assert_word).click()

    def send_element(self,assert_word, text=''):
        return self.wait.until(assert_word).send_keys(text)




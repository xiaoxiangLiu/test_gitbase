#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Page(object):

    '''页面基础类，用于所有页面的继承'''

    url = 'http://menghua_test.dev.sjgtw.net:48097/'

    def __init__(self, selenium_driver, base_url=url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 10
        self.parent = parent


    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        # 执行script语句
        return self.driver.execute_script(src)

    def max_window(self):
        # 最大化浏览器
        return self.driver.maximize_window()

    # 获取url
    def get_url(self):
        return self.driver.current_url

    # 切换标签页
    def window_by_index(self, num=-1):
        # num:0到-1
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[num])


    # 按照文本来选择select
    def select_by_text(self, element, text):
        return Select(element).select_by_visible_text(text)

    # 下拉滚动条到指定元素
    def down_scroll_bar(self, element, js="arguments[0].scrollIntoView();"):
        return self.driver.execute_script(js, element)

    # 移动鼠标到指定元素
    def move_to_element(self, element):
        return ActionChains(self.driver).move_to_element(to_element=element).perform()

    def visibility_by_element(self, *loc):
        return EC.visibility_of(self.find_element(*loc))

    def wait(self):
        driver = WebDriverWait(self.driver, 5)
        return driver

    # 按照index来选择select
    def select_by_index(self, element, index=0):
        return Select(element).select_by_index(index)




















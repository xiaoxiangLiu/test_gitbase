__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class MainMenu(Page):


    '''服务机构-菜单'''

    # 主菜单
    # 联采比较价
    button_bijiaojia_loc = (By.CSS_SELECTOR, '#menu_151 > a')



    # 点击主菜单联采比较价
    def click_bijiaojia(self):
        self.find_element(*self.button_bijiaojia_loc).click()
        return self
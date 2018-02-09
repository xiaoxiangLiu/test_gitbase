__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):


    '''工区试验人员-主菜单'''

    # 左侧菜单
    # 待抽样发货单
    daichouyan_fahuodan_loc = (By.CSS_SELECTOR, '#menu_155 > a')
    # 抽样检验
    chouyang_jianyan_loc = (By.CSS_SELECTOR, '#menu_154 > a')



    # 点击待抽样发货单
    def click_daichouyan(self):
        return self.find_element(*self.daichouyan_fahuodan_loc).click()

    # 点击抽样检验
    def click_chouyang_jianyan(self):
        return self.find_element(*self.chouyang_jianyan_loc).click()




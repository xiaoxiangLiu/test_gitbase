__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class MainMenu(Page):


    '''监理单位-主菜单页'''

    # 主菜单
    # 抽样检验
    chouyang_jianyan_loc = (By.CSS_SELECTOR, '#menu_154 > a > span')
    # 创建人
    input_greater_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(3) > div > input')
    # 抽样地址
    input_chouyang_address_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(5) > div > input')
    # 搜索
    button_search_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(6) > div > button.btn.btn-primary')
    # 第一列创建人
    text_first_plan_greater_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(6)')
    # 第一列抽样地址
    text_first_plan_address_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(8)')

    # 创建人搜索
    def greater_search(self):
        self.find_element(*self.input_greater_loc).send_keys('工区')
        self.find_element(*self.button_search_loc).click()
        return self.find_element(*self.text_first_plan_greater_loc).text

    # 抽样地址搜索
    def address_search(self):
        self.find_element(*self.input_chouyang_address_loc).send_keys('新疆')
        self.find_element(*self.button_search_loc).click()
        return self.find_element(*self.text_first_plan_address_loc).text

    # 点击主菜单抽样检验
    def click_chouyang(self):
        return self.find_element(*self.chouyang_jianyan_loc).click()



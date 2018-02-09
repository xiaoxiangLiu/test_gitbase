__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class DaichouyangPlanList(Page):

    '''带抽样发货单-主页列表'''


    # 筛选区-发货单名称输入框
    input_plan_name_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(1) > div > input')
    # 筛选区-合同编号输入框
    input_plan_number_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(2) > div > input')
    # 筛选区-搜索
    button_search_loc = (By.CSS_SELECTOR, '#queryForm > div > div.form-group.col-xs-4.pull-right > div > button.btn.btn-primary')
    # 第一列确认收货
    first_affirm_loc = (By.CSS_SELECTOR, '#dispatchTable > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(2)')
    # 第一列创建抽样
    first_plan_great_chouyan_loc = (By.CSS_SELECTOR, '#dispatchTable > tbody > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)')
    # 第一列发货单名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#dispatchTable > tbody > tr:nth-child(1) > td:nth-child(1) > a')
    # 确认
    button_submit_loc = (By.CSS_SELECTOR, '#popup_ok')

    # 筛选区-发货单名称输入数据
    def send_plan_name(self):
        return self.find_element(*self.input_plan_name_loc).send_keys('回归')

    # 筛选区-发货单编号输入数据
    def send_plan_number(self):
        return self.find_element(*self.input_plan_number_loc).send_keys('家里测试')

    # 筛选区-点击搜索
    def click_search(self):
        return self.find_element(*self.button_search_loc).click()

    # 文本，第一列发货单名称
    def text_first_plan(self):
        return self.find_element(*self.first_plan_name_loc).text

    # 点击第一列创建抽样
    def click_first_plan_chouyang(self):
        return self.find_element(*self.first_plan_great_chouyan_loc).click()

    # 点击第一列确认收货
    def click_first_plan_affirm(self):
        self.find_element(*self.first_affirm_loc).click()
        return self

    # 点击确认
    def click_submit(self):
        return self.find_element(*self.button_submit_loc).click()





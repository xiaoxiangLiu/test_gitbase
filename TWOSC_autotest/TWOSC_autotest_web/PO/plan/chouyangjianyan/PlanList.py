__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By
import time




class PlanList(Page):

    '''抽样检验详情页'''

    # 筛选区
    # 抽样单名称
    input_chouyang_name_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(1) > div > input')
    # 发货单名称
    input_fahuo_name_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(2) > div > input')
    # 创建人
    input_greater_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(3) > div > input')
    # 抽样地址
    input_chouyang_address_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(5) > div > input')
    # 搜索
    button_search_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(6) > div > button.btn.btn-primary')
    # 抽样单列表
    # 第一列抽样单名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    # 第一列抽样检验
    first_plan_chouyang_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(9) > a')
    # 第二列抽样检验
    second_plan_chouyang_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(2) > td:nth-child(9) > a')
    # 第三列抽样检验
    thrid_plan_chouyang_loc = (By.XPATH, '//*[@id="datatable"]/tbody/tr[3]/td[9]/a')


    # 抽样单名称搜索
    def search_chouyang_name(self):
        self.find_element(*self.input_chouyang_name_loc).send_keys('123')
        self.find_element(*self.button_search_loc).click()
        time.sleep(1)
        return self.find_element(*self.first_plan_name_loc).text

    # 发货单名称搜索
    def search_fahuo_name(self):
        self.find_element(*self.input_fahuo_name_loc).send_keys('测试使用位置')
        self.find_element(*self.button_search_loc).click()
        time.sleep(1)
        return self.find_element(*self.first_plan_name_loc).text

    # 点击第一列抽样检验，
    def click_first_chouyang_jianyan(self):
        self.find_element(*self.first_plan_chouyang_loc).click()
        return self

    # 点击第二列抽样检验
    def click_second_chouyang_jianyan(self):
        self.find_element(*self.second_plan_chouyang_loc).click()
        return self

    # 点击第三列抽样检验
    def click_thrid_chouyang_jianyan(self):
        self.find_element(*self.thrid_plan_chouyang_loc).click()
        return self

    # 切换到最后一个标签
    def select_to_winodw(self):
        self.window_by_index()
        return self

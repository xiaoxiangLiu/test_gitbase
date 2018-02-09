__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class PlanList(Page):

    '''发货单列表模块'''

    # 第一列发货单名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(1) > a')
    # 第一列发货单合同编号
    first_plan_number_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(2)')
    # 第一列发货单位
    first_plan_sellercompany_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(6)')
    # 第一列发货人
    first_plan_seller_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(7)')
    # 第一列验收人员
    first_checker_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(9)')
    # 第一列验收
    first_plan_check_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(10) > a')
    # 第一列二次验收时的验收
    first_plan_again_check_loc = (By.CSS_SELECTOR, '#datatable > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(2)')



    # 第一列发货单名称文本
    def text_first_plan(self):
        return self.find_element(*self.first_plan_name_loc).text

    # 第一列发货单编号文本
    def text_first_plan_number(self):
        return self.find_element(*self.first_plan_number_loc).text

    # 第一列发货单位文本
    def text_first_plan_sellercompany(self):
        return self.find_element(*self.first_plan_sellercompany_loc).text

    # 第一列发货人文本
    def text_first_plan_seller(self):
        return self.find_element(*self.first_plan_seller_loc).text

    # 第一列验收人员文本
    def text_first_plan_checker(self):
        return self.find_element(*self.first_checker_loc).text

    # 点击第一列验收
    def click_first_plan_check(self):
        return self.find_element(*self.first_plan_check_loc).click()

    # 点击第一列查看按钮后面的验收
    def click_first_plan_again_check(self):
        return self.find_element(*self.first_plan_again_check_loc).click()


__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class sonPlanDetail(Page):

    '''子计划详情页'''

    # 查询子计划

    # 全选checkbox
    all_check_box_loc = (By.CSS_SELECTOR, '#dataTable > thead > tr > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 第一列勾选
    first_check_box_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr > td.bs-checkbox > input[type="checkbox"]')
    # 添加到备选单
    add_list_loc = (By.LINK_TEXT, '添加到备选单')
    # 已选计划列表-删除
    delet_plan_loc = (By.CSS_SELECTOR, '#selectedChildPlanList > tbody > tr > td:nth-child(9) > a')
    # 确认添加
    primary_add_loc = (By.LINK_TEXT, '确认添加')
    # 放弃添加
    default_add_loc = (By.LINK_TEXT, '放弃添加')
    # 确认
    confirm_loc = (By.CSS_SELECTOR, '#popup_ok')


    # 勾选全选
    def click_all_check(self):
        return self.find_element(*self.all_check_box_loc).click()

    # 勾选第一列
    def click_first_check(self):
        return self.find_element(*self.first_check_box_loc).click()

    # 点击添加到备选
    def click_add_list(self):
        return self.find_element(*self.add_list_loc).click()

    # 点击确认添加
    def click_primary(self):
        return self.find_element(*self.primary_add_loc).click()

    # 点击删除
    def click_delet(self):
        return self.find_element(*self.delet_plan_loc).click()

    # 点击放弃添加
    def click_default(self):
        return self.find_element(*self.default_add_loc).click()

    # 点击确认
    def click_confirm(self):
        return self.find_element(*self.confirm_loc).click()




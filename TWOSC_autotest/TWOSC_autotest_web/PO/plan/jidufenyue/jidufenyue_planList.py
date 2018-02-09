__author__ = '38720'
# coding=utf-8

from selenium.webdriver.common.by import By
from base_page.base import Page


class planList(Page):

    '''  标段业务人员-季度分月计划页-计划列表  '''

    '''工具栏'''

    # 季度分月
    jiduFenyue_loc = (By.CSS_SELECTOR, '#menu_170 > a > span')
    # 新建
    xinjian_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/a[1]')
    # 删除
    shanchu_loc = (By.CSS_SELECTOR, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/a[2]')
    # 导出
    daochu_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/a')

    '''计划栏'''

    # 全选
    all_check_box_loc = (By.CSS_SELECTOR, '#demandPlanningSGTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 第一个计划勾选
    first_check_box_loc = (By.CSS_SELECTOR, '#demandPlanningSGTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 第一个计划名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#demandPlanningSGTable > tbody > tr:nth-child(1) > td.width_15 > a')
    # 第一个计划编辑
    first_plan_edit_loc = (By.CSS_SELECTOR, '#demandPlanningSGTable > tbody > tr:nth-child(1) > td:nth-child(11) > a')

    # 点击创建计划
    def click_new_plan(self):
        return self.find_element(*self.xinjian_loc).click()

    # 点击计划列表第一列计划
    def click_first_plan(self):
        return self.find_element(*self.first_plan_name_loc).click()

    # 切换到新标签
    def switch_new_window(self):
        return self.window_by_index(-1)







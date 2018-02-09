__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By


class PlanList(Page):

    '''总需求计划-列表页导航'''

    # 计划管理
    a_jihuaguanli_loc = (By.LINK_TEXT, '计划管理')
    # 总/年度需求计划
    a_zong_niandu_loc = (By.LINK_TEXT, '总/年度需求计划')
    # 创建新需求计划
    button_create_new_plan_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/a')
    # 联采
    a_liancai_loc = (By.LINK_TEXT, '联采')

    # 创建新需求计划的text
    def text_new_plan(self):
        return self.find_element(*self.button_create_new_plan_loc).text

    # 点击计划管理
    def click_jihuaguanli(self):
        self.find_element(*self.a_jihuaguanli_loc).click()
        return self

    # 点击总/年度需求计划
    def click_xuqiujihua(self):
        self.find_element(*self.a_zong_niandu_loc).click()
        return self

    # 点击创建新需求计划
    def click_new_plan(self):
        self.find_element(*self.button_create_new_plan_loc).click()
        return self

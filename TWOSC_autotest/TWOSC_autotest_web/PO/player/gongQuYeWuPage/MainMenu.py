__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):

    '''工区业务人员header'''
    # 计划管理
    a_jihuaguanli_loc = (By.LINK_TEXT, '计划管理')
    # 总/年度需求计划
    a_zong_niandu_loc = (By.LINK_TEXT, '总/年度需求计划')
    # 创建新需求计划
    button_create_new_plan_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/a')
    # 联采
    a_liancai_loc = (By.LINK_TEXT, '联采')
    # 名称搜索
    select_name_loc = (By.CSS_SELECTOR, '#planName')
    # 计划编号
    input_plan_number_loc = (By.CSS_SELECTOR, '#planNbr')
    # 审批状态
    select_status_loc = (By.CSS_SELECTOR, '#auditStsCde')


    def text_new_plan(self):
        return self.find_element(*self.button_create_new_plan_loc).text

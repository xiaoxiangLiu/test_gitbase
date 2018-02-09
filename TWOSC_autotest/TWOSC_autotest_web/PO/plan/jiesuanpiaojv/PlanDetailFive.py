__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetailFive(Page):

    '''第五页'''
    # 文本,选择审批人员
    text_select_auditor_loc = (By.CSS_SELECTOR, '#workflow_actor_details > h4')
    # 添加工区审批人员
    button_add_people_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(3) > td.col-xs-10 > a')
    # 添加施工单位审批人员
    button_add_people_two_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(4) > td.col-xs-10 > a')
    # 添加服务机构审批人员
    button_add_people_three_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(5) > td.col-xs-10 > a')
    # 添加指挥部审批人员
    button_add_people_five_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(6) > td.col-xs-10 > a')
    # 备注
    textarea_remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    button_primary_loc = (By.CSS_SELECTOR, '#workflow_actor_details > div.text-center > a.btn.btn-primary.btn-short.margin.submitForm')
    # 确认
    button_pop_loc = (By.CSS_SELECTOR, '#popup_ok')


    # 文本，选择审批人员
    def text_select_auditor(self):
        return self.find_element(*self.text_select_auditor_loc).text

    # 点击，添加工区审批人员
    def click_add_people(self):
        self.find_element(*self.button_add_people_loc).click()
        return self

    # 点击，添加施工单位审批人员
    def click_add_people_two(self):
        self.find_element(*self.button_add_people_two_loc).click()
        return self

    # 点击，添加服务机构审批人员
    def click_add_people_three(self):
        self.find_element(*self.button_add_people_three_loc).click()
        return self

    # 点击，添加指挥部审批人员
    def click_add_people_five(self):
        self.find_element(*self.button_add_people_five_loc).click()
        return self

    # 输入备注
    def send_remark(self):
        self.find_element(*self.textarea_remark_loc).send_keys('自动化测试审批通过')
        return self

    # 点击提交
    def click_primary(self):
        self.find_element(*self.button_primary_loc).click()
        return self

    # 点击确认
    def click_pop(self):
        self.find_element(*self.button_pop_loc).click()
        return self



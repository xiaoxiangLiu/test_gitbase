__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class PlanFirst(Page):

    '''联采比较价-新建第一页'''

    # 比较价名称
    input_plan_name_loc = (By.CSS_SELECTOR, '#name')
    # 选择省份
    select_province_loc = (By.CSS_SELECTOR, '#provinceId')
    # 选择物资
    select_goods_loc = (By.CSS_SELECTOR, '#materialKindName')
    # 备注
    textarea_remark_loc = (By.CSS_SELECTOR, '#remark')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#formbase > div > div.user-panel.text-center > a.btn.btn-primary.btn-short.margin')

    # 输入比较价名称
    def send_name(self):
        self.find_element(*self.input_plan_name_loc).send_keys('自动化联采比较价测试')
        return self

    # 选择省份
    def select_province(self):
        self.select_by_text(self.find_element(*self.select_province_loc), '吉林省')
        return self

    # 选择物资
    def select_goods(self):
        self.select_by_text(self.find_element(*self.select_goods_loc), '钢材')
        return self

    # 填写备注
    def send_remark(self):
        self.find_element(*self.textarea_remark_loc).send_keys('自动化测试备注')
        return self

    # 点击，下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self


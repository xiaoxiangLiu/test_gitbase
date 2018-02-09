__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class JianLiPlanDetail(Page):

    '''监理单位-平行检验详情页'''

    # 是
    input_yes_loc = (By.CSS_SELECTOR, '#submitForm > div:nth-child(10) > div > div > label:nth-child(1) > input[type="radio"]')
    # 否
    input_no_loc = (By.CSS_SELECTOR, '#submitForm > div:nth-child(10) > div > div > label:nth-child(2) > input[type="radio"]')
    # 合格
    input_qualified_loc = (By.CSS_SELECTOR, '#submitForm > div.ra_box > div > div.form-horizontal > div:nth-child(1) > div > div:nth-child(1) > input[type="radio"]')
    # 不合格
    input_unqualified_loc = (By.CSS_SELECTOR, '#submitForm > div.ra_box > div > div.form-horizontal > div:nth-child(1) > div > div:nth-child(2) > input[type="radio"]')
    # 备注
    textarea_remarl_loc = (By.CSS_SELECTOR, '#submitForm > div.ra_box > div > div.form-horizontal > div:nth-child(2) > div > textarea')
    # 提交
    button_primary_loc = (By.CSS_SELECTOR, 'body > div.wrapper > div:nth-child(5) > div > div > div.box-footer.text-center > button:nth-child(1)')
    # 上报
    report_primary_loc = (By.CSS_SELECTOR, '#report')
    # 检测结论
    text_jiance_jielun_loc = (By.CSS_SELECTOR, '#submitForm > div.ra_box > div > div > div:nth-child(1) > div > div.col-xs-1.control-label.text-left')

    # 点击否并提交
    def click_no(self):
        self.find_element(*self.input_no_loc).click()
        self.find_element(*self.button_primary_loc).click()

    # 点击是，点击合格
    def click_yes_qualified(self):
        self.find_element(*self.input_yes_loc).click()
        self.find_element(*self.input_qualified_loc).click()
        self.find_element(*self.textarea_remarl_loc).send_keys('自动化测试，监理单位平行检验合格备注')
        self.find_element(*self.button_primary_loc).click()
        return self

    # 获取检测结果
    def text_jiance(self):
        text = self.find_element(*self.text_jiance_jielun_loc).text
        return text

    # 点击是，点击不合格,点击提交
    def click_yes_unqualified(self):
        self.find_element(*self.input_yes_loc).click()
        self.find_element(*self.input_unqualified_loc).click()
        self.find_element(*self.textarea_remarl_loc).send_keys('自动化测试，监理单位平行检验不合格,点击提交备注')
        self.find_element(*self.button_primary_loc).click()
        return self

    # 点击是，点击不合格，点击上报
    def click_yes_unqualified_report(self):
        self.find_element(*self.input_yes_loc).click()
        self.find_element(*self.input_unqualified_loc).click()
        self.find_element(*self.textarea_remarl_loc).send_keys('自动化测试，监理单位平行检验不合格,点击上报备注')
        self.find_element(*self.report_primary_loc).click()
        return self


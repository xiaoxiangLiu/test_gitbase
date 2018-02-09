__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class Audit(Page):

    '''到货初验会签页'''

    # 通过
    agree_loc = (By.CSS_SELECTOR, 'input[value="通过"]')
    # 备注
    remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    primary_loc = (By.LINK_TEXT, '提交')
    # 确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 发货单状态
    plan_status_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/form/div/div[8]/div')

    # 点击通过
    def click_agree(self):
        return self.find_element(*self.agree_loc).click()

    # 添加备注
    def send_remark(self):
        return self.find_element(*self.remark_loc).send_keys('自动化测试到货初验审核通过')

    # 点击提交
    def click_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 文本，发货单状态
    def text_plan_status(self):
        return self.find_element(*self.plan_status_loc).text
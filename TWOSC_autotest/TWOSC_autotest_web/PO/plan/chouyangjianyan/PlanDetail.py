__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetail(Page):

    '''抽样检验详情页'''

    # 合格
    input_qualified_loc = (By.CSS_SELECTOR, '#submitForm > div:nth-child(6) > div > div > div:nth-child(1) > input[type="radio"]')
    # 不合格
    input_unqualified_loc = (By.CSS_SELECTOR, 'input[value="2"]')
    # 备注
    texterea_remark_loc = (By.CSS_SELECTOR, '#submitForm > div:nth-child(9) > div > div > textarea')
    # 提交
    button_primary_loc = (By.CSS_SELECTOR, 'body > div.wrapper > div:nth-child(5) > div > div > div.box-footer.text-center > button:nth-child(1)')
    # 检验结论
    text_jianyan_jielun_loc = (By.CSS_SELECTOR, '#submitForm > div:nth-child(6) > div > div > div')

    # 点击合格
    def click_qualified(self):
        element = self.visibility_by_element(*self.input_qualified_loc)
        self.wait().until(element).click()
        return self

    # 点击不合格
    def click_unqualified(self):
        element = self.visibility_by_element(*self.input_unqualified_loc)
        self.wait().until(element).click()
        return self

    # 填写备注
    def send_remark(self):
        element = self.visibility_by_element(*self.texterea_remark_loc)
        self.wait().until(element).send_keys('自动化测试备注')
        return self

    # 点击提交
    def click_primary(self):
        self.find_element(*self.button_primary_loc).click()
        return self

    # 文本，检验结论
    def text_jianyan_jielun(self):
        return self.find_element(*self.text_jianyan_jielun_loc).text


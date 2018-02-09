__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class newPlan(Page):


    '''标段业务人员-季度分月-新建计划页'''

    # title
    titlelable_loc = (By.CSS_SELECTOR, '#myModalLabel')
    # 选择年份
    selectyear_loc = (By.CSS_SELECTOR, '#planYear')
    # 选择季度
    selectplanqtr_loc = (By.CSS_SELECTOR, '#planQtr')
    # 创建
    createbutton_loc = (By.XPATH, '//*[@id="quarter_add_view"]/div[3]/div[1]/button')
    # 取消
    cancelbutton_loc = (By.XPATH, '//*[@id="quarter_add_view"]/div[3]/div[2]/button')


    def select_year(self, text):
        element = self.get_element(*self.selectyear_loc)
        return self.select_by_text(element, text)

    def select_yearqtr(self, text):
        element = self.get_element(*self.selectplanqtr_loc)
        return self.select_by_text(element, text)
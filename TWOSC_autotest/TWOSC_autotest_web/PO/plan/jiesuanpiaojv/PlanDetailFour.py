__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By




class PlanDetailFour(Page):

    '''第四页'''
    # 文本,校对信息
    text_jiaodui_xinxi_loc = (By.CSS_SELECTOR, '#label_check > p')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#section_check > div.user-panel.text-center > a:nth-child(2)')




    # 文本，校对信息
    def text_jiaodui(self):
        return self.find_element(*self.text_jiaodui_xinxi_loc).text

    # 点击下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self

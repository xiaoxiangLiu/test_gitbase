__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanSecond(Page):

    '''联采比较价-第二页填写信息'''

    # 文本,物资列表
    text_goods_list_loc = (By.CSS_SELECTOR, '#section_price > h4')
    # 文本，进度
    text_point_loc = (By.CSS_SELECTOR, '#label_price > p')
    # 全选框
    checkbox_all_loc = (By.CSS_SELECTOR, '#importGoodsPriceInformationTable > thead > tr > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 批量编辑
    button_batch_edit_loc = (By.CSS_SELECTOR, '#comparativePriceListForm > div.tool-bar.overflow_h > div.btn-group.pull-left > a')
    # 比较价输入框
    input_bijiaojia_send_loc = (By.CSS_SELECTOR, '#popup_prompt')
    # 确定，比较价输入框
    button_primary_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#section_price > div.user-panel.text-center > a.btn.btn-primary.btn-short.margin')

    # 文本，物资列表
    def text_goods_list(self):
        return self.find_element(*self.text_goods_list_loc).text

    # 文本，进度
    def text_point(self):
        return self.find_element(*self.text_point_loc).text

    # 点击，全选
    def click_check_all(self):
        self.find_element(*self.checkbox_all_loc).click()
        return self

    # 点击，批量编辑
    def click_batch_edit(self):
        self.find_element(*self.button_batch_edit_loc).click()
        return self

    # 输入，联采比较价
    def send_bijiaojia(self):
        self.find_element(*self.input_bijiaojia_send_loc).send_keys('200')
        return self

    # 点击，输入框确定
    def click_primary(self):
        self.find_element(*self.button_primary_loc).click()
        return self

    # 点击，下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self

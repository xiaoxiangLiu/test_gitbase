__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC



class PlanDetailTwo(Page):

    '''结算票据选择发货单页'''

    # label 选择发货单
    label_select_fahuodan_loc = (By.CSS_SELECTOR, '#section_chooseDispatch > h4:nth-child(1)')
    # 第一个发货单
    checkbox_first_plan_loc = (By.CSS_SELECTOR, '#dispatchBillsTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 添加到已选发货单
    button_yixuan_fahuodan_loc = (By.CSS_SELECTOR, '#section_chooseDispatch > div:nth-child(8) > button')
    # 总运费输入框
    input_zongyunfei_loc = (By.CSS_SELECTOR, '#totalTransportFees')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#section_chooseDispatch > div.user-panel.text-center > a:nth-child(2)')
    # 提示框确定
    button_popup_loc = (By.CSS_SELECTOR, '#popup_ok')




    # 文本，选择发货单label
    def text_select_fahuodan(self):
        return self.find_element(*self.label_select_fahuodan_loc).text

    # 点击勾选第一列发货单
    def click_first_plan(self):
        self.find_element(*self.checkbox_first_plan_loc).click()
        return self

    # 点击添加到已选发货单
    def click_yixuan_fahuodan(self):
        self.find_element(*self.button_yixuan_fahuodan_loc).click()
        return self

    # 输入总运费金额
    def send_zongyunfei(self):
        if self.find_element(*self.input_zongyunfei_loc).is_displayed():
            self.find_element(*self.input_zongyunfei_loc).clear()
            self.find_element(*self.input_zongyunfei_loc).send_keys('100')
        else:
            print('没有需要输入总运费的物资')
        return self

    # 点击下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self

    # 点击提示框
    def click_pop(self):
        self.find_element(*self.button_popup_loc).click()
        return self


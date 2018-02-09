__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By
import time


class PlanDetail(Page):

    '''待抽样发货单详情页'''

    # 发货单基本信息，发货单状态
    plan_status_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/form/div/div[8]/div')
    # 第一列物资创建抽样
    first_goods_great_chouyang_loc = (By.CSS_SELECTOR, '#userTable > tbody > tr:nth-child(1) > td:nth-child(8) > a:nth-child(1)')
    # 第二列物资创建抽样
    second_good_great_chouyang_loc = (By.CSS_SELECTOR, '#userTable > tbody > tr:nth-child(2) > td:nth-child(8) > a:nth-child(1)')
    # 第三列物资创建抽样
    third_goods_great_chouyang_loc = (By.CSS_SELECTOR, '#userTable > tbody > tr:nth-child(3) > td:nth-child(8) > a:nth-child(1)')
    # 第一列物资查看工艺信息
    first_goods_check_loc = (By.CSS_SELECTOR, '#userTable > tbody > tr:nth-child(1) > td:nth-child(8) > a.btn.btn-link.add_info')
    # 抽样单名称输入框
    input_chouyang_name_loc = (By.CSS_SELECTOR, '#sampleName')
    # 抽样数量输入框
    input_chouyang_quantity_loc = (By.CSS_SELECTOR, '#sampleCount')
    # 抽样地址输入框
    input_chouyang_address_loc = (By.CSS_SELECTOR, '#sampleAddress')
    # 抽样单填写框确认
    button_chouyang_primary_loc = (By.CSS_SELECTOR, '#onSubmit')
    # 抽样单填写框弹出的确认
    button_chouyang_submit_loc = (By.CSS_SELECTOR, '#popup_ok')





    # 文本，发货单状态
    def text_plan_status(self):
        return self.find_element(*self.plan_status_loc).text

    # 点击第一列物资创建抽样
    def click_first_goods_great_chouyang(self):
        return self.find_element(*self.first_goods_great_chouyang_loc).click()

    # 点击第一列物资查看工艺信息
    def click_first_goods_check(self):
        return self.find_element(*self.first_goods_check_loc).click()

    # 点击第一列的创建抽样，并填写各项资料
    def great_first_goods_chouyang(self):
        self.find_element(*self.first_goods_great_chouyang_loc).click()
        self.find_element(*self.input_chouyang_name_loc).send_keys('自动化测试')
        self.find_element(*self.input_chouyang_quantity_loc).send_keys('10')
        self.find_element(*self.input_chouyang_address_loc).send_keys('北京天安门')
        self.find_element(*self.button_chouyang_primary_loc).click()
        self.find_element(*self.button_chouyang_submit_loc).click()
        return True

    # 点击第二列的创建抽样，并填写各项资料
    def great_second_goods_chouyang(self):
        self.find_element(*self.second_good_great_chouyang_loc).click()
        self.find_element(*self.input_chouyang_name_loc).send_keys('自动化测试')
        self.find_element(*self.input_chouyang_quantity_loc).send_keys('10')
        self.find_element(*self.input_chouyang_address_loc).send_keys('北京天安门')
        self.find_element(*self.button_chouyang_primary_loc).click()
        self.find_element(*self.button_chouyang_submit_loc).click()
        return True

    # 点击第三列的创建抽样，并填写各项资料
    def great_third_goods_chouyang(self):

        self.find_element(*self.third_goods_great_chouyang_loc).click()
        self.find_element(*self.input_chouyang_name_loc).send_keys('自动化测试')
        self.find_element(*self.input_chouyang_quantity_loc).send_keys('10')
        self.find_element(*self.input_chouyang_address_loc).send_keys('北京天安门')
        self.find_element(*self.button_chouyang_primary_loc).click()
        self.find_element(*self.button_chouyang_submit_loc).click()
        return True

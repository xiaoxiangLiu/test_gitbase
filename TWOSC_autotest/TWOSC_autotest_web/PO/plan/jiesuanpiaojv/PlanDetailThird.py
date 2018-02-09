__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By
import time



class PlanDetailThird(Page):

    '''结算票据-第三页填写结算票据'''

    #编辑
    button_bianji_loc = (By.CSS_SELECTOR, '#fillInvoiceTable > tbody > tr > td:nth-child(14) > a')
    # 第一列编辑
    buttong_bianji_one_loc = (By.CSS_SELECTOR, '#fillInvoiceTable > tbody > tr:nth-child(1) > td:nth-child(14) > a')
    # 第二列编辑
    buttong_bianji_two_loc = (By.CSS_SELECTOR, '#fillInvoiceTable > tbody > tr:nth-child(2) > td:nth-child(14) > a')
    # 发票编号
    input_number_loc = (By.CSS_SELECTOR, '#invoiceNo0')
    # 发票金额
    input_jine_loc = (By.CSS_SELECTOR, '#invoicePrice0')
    # 发票数量
    input_shuliang_loc = (By.CSS_SELECTOR, '#invoiceAmount0')
    # 保存
    button_baocun_loc = (By.CSS_SELECTOR, '#formSub > div > div > div.box-footer > div.col-xs-offset-3.col-xs-3 > a')
    # 添加
    button_tianjia_loc = (By.CSS_SELECTOR, '#section_fillInvoiceInfo > div.tool-bar.clearfix > div > a:nth-child(1)')
    # 发票编号
    input_number_2_loc = (By.CSS_SELECTOR, '#invoiceNo')
    # 发票金额
    input_jine_2_loc = (By.CSS_SELECTOR, '#invoiceMoney')
    # 保存
    button_baocun_2_loc = (By.CSS_SELECTOR, '#transportInvoiceForm > div.box-footer > div.col-xs-offset-2.col-xs-3 > input')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#toStepFour')
    # 文本，填写发票信息清单
    text_fapiao_loc = (By.CSS_SELECTOR, '#section_fillInvoiceInfo > h4:nth-child(3)')
    # 确认
    button_submit_loc = (By.CSS_SELECTOR, '#popup_ok')

    # 编辑物资发票清单
    def edit_fapiao(self):
        if self.find_element(*self.buttong_bianji_one_loc).is_displayed():
            self.find_element(*self.buttong_bianji_one_loc).click()
        else:
            print('没有可以编辑的物资')
        time.sleep(1)
        return self

    # 编辑第二列物资发票清单
    def edit_fapiao_two(self):
        if self.find_element(*self.buttong_bianji_two_loc).is_displayed():
            self.find_element(*self.buttong_bianji_two_loc).click()
        else:
            print('没有第二列物资')
        return self

    # 填写物资发票清单发票编号
    def send_bianhao(self):
        self.find_element(*self.input_number_loc).clear()
        self.find_element(*self.input_number_loc).send_keys('001')
        return self

    # 填写物资发票清单金额
    def send_jine(self):
        self.find_element(*self.input_jine_loc).clear()
        self.find_element(*self.input_jine_loc).send_keys('100')
        return self

    # 填写物资发票清单数量
    def send_shuliang(self):
        self.find_element(*self.input_shuliang_loc).clear()
        self.find_element(*self.input_shuliang_loc).send_keys('100')
        return self

    # 点击保存
    def click_baocun(self):
        self.find_element(*self.button_baocun_loc).click()
        return self

    # 点击添加运输发票清单
    def click_tianjia(self):
        self.find_element(*self.button_tianjia_loc).click()
        return self

    # 填写运输发票编号
    def send_bianhao_2(self):
        self.find_element(*self.input_number_2_loc).send_keys('002')
        return self

    # 填写运输发票金额
    def send_jine_2(self):
        self.find_element(*self.input_jine_2_loc).send_keys('100')
        return self

    # 点击保存
    def click_baocun_2(self):
        self.find_element(*self.button_baocun_2_loc).click()
        return self

    # 文本，填写发票信息
    def text_fapiao_xinxi(self):
        return self.find_element(*self.text_fapiao_loc).text

    # 点击下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self

    # 点击确认
    def click_submit(self):
        self.find_element(*self.button_submit_loc).click()
        return self
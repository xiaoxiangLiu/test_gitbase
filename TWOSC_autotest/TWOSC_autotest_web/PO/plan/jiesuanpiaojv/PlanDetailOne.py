__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetailOne(Page):

    '''结算票据-详情页'''

    # 结算票据名称填写框
    input_jiesuan_name_loc = (By.CSS_SELECTOR, '#settlementBillsName')
    # 质保金输入框
    input_zhibaojin_loc = (By.CSS_SELECTOR, '#guarantee')
    # 预付款金额输入框
    input_yufukuan_loc = (By.CSS_SELECTOR, '#deposit')
    # 备注
    texterea_remark_loc = (By.CSS_SELECTOR, '#settlementBillForm > div > div.form-group.col-xs-12 > div > textarea')
    # 下一步
    button_primary_loc = (By.XPATH, '//*[@id="settlementBillForm"]/div/div[5]/a[2]')


    # 填写结算票据名称
    def send_jiesuan_name(self):
        self.find_element(*self.input_jiesuan_name_loc).send_keys('MH-2017年-9月水泥结算dan')
        return self

    # 填写质保金
    def send_zhibaojin(self):
        self.find_element(*self.input_zhibaojin_loc).send_keys('0.09')
        return self

    # 填写预付款金额
    def send_yufukuan(self):
        self.find_element(*self.input_yufukuan_loc).send_keys('120000')
        return self

    # 填写备注
    def send_remark(self):
        self.find_element(*self.texterea_remark_loc).send_keys('结算单基本信息页-备注')
        return self

    # 点击下一步
    def click_next(self):
        return self.find_element(*self.button_primary_loc).click()

    # 下拉到下一步
    def to_element(self):
        self.down_scroll_bar(self.find_element(*self.button_primary_loc))
        return self

__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetail(Page):

    '''工区业务人员-抽样检验详情页'''

    # 组织重检
    input_zuzhi_chongjian_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div/label/input')
    # 合格
    input_qualified_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/label[1]/input')
    # 备注
    textreae_remark_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/textarea')
    # 提交
    button_primary_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/button[1]')
    # 合格
    text_qualified_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div')

    # 点击组织重检
    def click_zuzhi_chongjian(self):
        self.find_element(*self.input_zuzhi_chongjian_loc).click()
        return self

    # 点击合格
    def click_qualified(self):
        self.find_element(*self.input_qualified_loc).click()
        return self

    # 输入备注
    def send_remark(self):
        self.find_element(*self.textreae_remark_loc).send_keys('监理单位，组织重检，合格')
        return self

    # 点击提交
    def click_primary(self):
        return self.find_element(*self.button_primary_loc).click()

    # 获取合格信息
    def text_qualified(self):
        return self.find_element(*self.text_qualified_loc).text

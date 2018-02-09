__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By

class NewPlan(Page):

    '''新建发货单页面'''

    # 选择机构
    selecet_jigou_loc = (By.CSS_SELECTOR, '#secId')
    # 选择收货地址
    shouhuo_dizhi_loc = (By.XPATH, '//*[@id="1"]')
    # 发货单名称
    fahuodan_name_loc = (By.CSS_SELECTOR, 'input#name[placeholder="例如 ：MHTJ-14标二工区水泥发货单"]')
    # 说明
    remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    submit_loc = (By.XPATH, '//*[@id="GT_CommonModal"]/div[1]/div/div[2]/div/button[1]')



    # 点击选择机构
    def select_jigou(self):
        return self.select_by_text(element=self.find_element(*self.selecet_jigou_loc), text='MHTJ-23标一工区')

    # 发货单名称输入数据
    def send_fahuodan_name(self):

        return self.find_element(*self.fahuodan_name_loc).send_keys('自动化测试脚本' )

    # 输入说明
    def send_remark(self):
        return self.find_element(*self.remark_loc).send_keys('自动化测试备注')

    # 点击提交
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

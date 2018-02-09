__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):

    '''工区验收人员-主菜单'''

    # 到货初验
    daohuo_chuyan_loc = (By.CSS_SELECTOR, '#menu_158 > a > span')
    # 选择工区
    select_gongqu_loc = (By.CSS_SELECTOR, '#dropdownMenu1')
    # 选择MHTJ-23标一工区
    select_biaoyi_gongqu_loc = (By.LINK_TEXT, 'MHTJ-23标一工区')
    # 待抽样发货单
    daichouyan_fahuodan_loc = (By.CSS_SELECTOR, '#menu_155 > a')


    # 筛选区

    # 发货单名称
    fahuodan_name_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(1) > div > input')
    # 合同编号
    contract_number_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(2) > div > input')
    # 发货单位
    seller_company_name_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(4) > div > input')
    # 发货人
    seller_uesr_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(5) > div > input')
    # 验收人
    checker_loc = (By.CSS_SELECTOR, '#queryForm > div > div:nth-child(6) > div > input')
    # 到货时间
    daohuo_time_loc = (By.CSS_SELECTOR, '#reservation')
    # 起始时间
    start_time_loc = (By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/input')
    # 结束时间
    end_time_loc = (By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/input')
    # 时间控件确定按钮
    time_sure_loc = (By.XPATH, '/html/body/div[5]/div[3]/div/button[1]')
    # 搜索
    search_loc = (By.CSS_SELECTOR, '#queryForm > div > div.form-group.col-xs-4.pull-right > div > button.btn.btn-primary')
    # 联采
    button_liancai_loc = (By.LINK_TEXT, '联采')

    # 发货单名称输入数据
    def send_fahuodan_name(self):
        return self.find_element(*self.fahuodan_name_loc).send_keys('自动化')

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_loc).click()

    # 合同编号输入数据
    def send_contract_number(self):
        return self.find_element(*self.contract_number_loc).send_keys('APP合同')

    # 联采-合同编号输入数据
    def send_liancai_contract_number(self):
        return self.find_element(*self.contract_number_loc).send_keys('联采合同')

    # 发货单位输入数据
    def send_seller_company(self):
        return self.find_element(*self.seller_company_name_loc).send_keys('衡水')

    # 发货人输入数据
    def send_sell_user(self):
        return self.find_element(*self.seller_uesr_loc).send_keys('杨')

    # 验收人输入数据
    def send_checker(self):
        return self.find_element(*self.checker_loc).send_keys('工区')

    # 点击到货时间
    def click_daohuo_time(self):
        return self.find_element(*self.daohuo_time_loc).click()

    # 输入起始时间
    def send_start_time(self):
        self.find_element(*self.start_time_loc).clear()
        return self.find_element(*self.start_time_loc).send_keys('2017-01-01')

    # 输入结束时间
    def send_end_time(self):
        self.find_element(*self.end_time_loc).clear()
        return self.find_element(*self.end_time_loc).send_keys('2017-05-05')

    # 点击时间控件确定
    def click_time_sure(self):
        return self.find_element(*self.time_sure_loc).click()

    # 点击联采
    def click_liancai(self):
        return self.find_element(*self.button_liancai_loc).click()

    # 联采-输入起始时间
    def send_liancai_start_time(self):
        self.find_element(*self.start_time_loc).clear()
        return self.find_element(*self.start_time_loc).send_keys('2018-01-01')

    # 联采-输入结束时间
    def send_liancai_end_time(self):
        self.find_element(*self.end_time_loc).clear()
        return self.find_element(*self.end_time_loc).send_keys('2017-05-05')








    # 点击到货初验
    def click_daohuo_chuyan(self):
        return self.find_element(*self.daohuo_chuyan_loc).click()

    # 点击选择工区
    def click_select_gongqu(self):
        return self.find_element(*self.select_gongqu_loc).click()

    # 点击MHTJ-23标一工区
    def click_biaoyi_gongqu(self):
        return self.find_element(*self.select_biaoyi_gongqu_loc).click()

    # 点击待抽样发货单
    def click_daichouyan(self):
        return self.find_element(*self.daichouyan_fahuodan_loc).click()


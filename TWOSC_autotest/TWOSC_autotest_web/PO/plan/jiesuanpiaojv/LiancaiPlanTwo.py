__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By
import time


class LiancaiPlanTwo(Page):

    '''联采-结算票据-新建第二页'''

    # 选择合同编号
    select_contract_number_loc = (By.CSS_SELECTOR, '#contractId')
    # 选择所属机构
    select_jigou_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm > div > div:nth-child(2) > div > select')
    # 选择到货地点
    select_daohuo_didian_loc = (By.CSS_SELECTOR, '#arriveAreaId')
    # 选择供应期，起始时间
    select_start_time_loc = (By.CSS_SELECTOR, '#earlyAcceptFinishStartTime')
    # 选择供应期，结束时间
    select_end_time_loc = (By.CSS_SELECTOR, '#earlyAcceptFinishEndTime')
    # 搜索按钮
    button_search_loc = (By.XPATH, '//*[@id="dispatchBillParamsForm"]/div/div[6]/div/button[1]')

    # 全选
    checkbox_all_loc = (By.CSS_SELECTOR, '#dispatchBillsTable > thead > tr > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 点击第一个勾选
    check_first_loc = (By.CSS_SELECTOR, '#dispatchBillsTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 添加到已选发货单
    button_tianjia_fahuodan_loc = (By.CSS_SELECTOR, '#section_chooseDispatch > div:nth-child(9) > button')
    # 下一步
    button_next_loc = (By.CSS_SELECTOR, '#section_chooseDispatch > div.user-panel.text-center > a:nth-child(2)')
    # 确定
    button_submit_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 第四个状态信息
    lable_point_loc = (By.CSS_SELECTOR, '#label_check > p')


    # 选择合同编号-物资结算汇总联采合同
    def select_contract(self):
        self.select_by_text(self.find_element(*self.select_contract_number_loc), '物资结算汇总联采合同')
        return self

    # 点击确定
    def click_submit(self):
        self.find_element(*self.button_submit_loc).click()
        return self

    # 选择工区-MHTJ-23标一工区
    def select_gongqu(self):
        self.select_by_text(self.find_element(*self.select_jigou_loc), 'MHTJ-23标一工区')
        return self

    # 选择到货地点-吉林省
    def select_daohuo(self):
        self.select_by_text(self.find_element(*self.select_daohuo_didian_loc), '吉林省')
        return self

    # 选择供应期-起始时间-2017-11
    def send_start_time(self):
        js = "document.getElementById('earlyAcceptFinishStartTime').removeAttribute('readonly')"
        self.script(js)
        self.find_element(*self.select_start_time_loc).clear()
        time.sleep(0.5)
        self.find_element(*self.select_start_time_loc).send_keys('2017-11')
        return self

    # 选择供应期-结束时间-2017-12
    def send_end_time(self):
        js = "document.getElementById('earlyAcceptFinishEndTime').removeAttribute('readonly')"
        self.script(js)
        self.find_element(*self.select_end_time_loc).clear()
        time.sleep(0.5)
        self.find_element(*self.select_end_time_loc).send_keys('2017-12')
        return self

    # 点击状态信息
    def click_point(self):
        time.sleep(1)
        self.find_element(*self.lable_point_loc).click()
        return self

    # 点击搜索
    def click_search(self):
        time.sleep(1)
        self.find_element(*self.button_search_loc).click()
        return self

    # 勾选全选
    def check_all(self):
        time.sleep(0.5)
        self.find_element(*self.checkbox_all_loc).click()
        return self

    # 勾选第一个
    def check_first(self):
        time.sleep(0.5)
        self.find_element(*self.check_first_loc).click()
        time.sleep(2)
        return self

    # 点击添加到已选发货单
    def click_tianjia(self):
        self.find_element(*self.button_tianjia_fahuodan_loc).click()
        return self

    # 点击下一步
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self
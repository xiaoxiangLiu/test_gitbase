__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By

class Xuanze_Wuzi_Detail(Page):

    '''选择物资详情页'''

    # 选择合同
    select_hetong_loc = (By.CSS_SELECTOR, '#contractId')
    # 搜索
    search_loc = (By.CSS_SELECTOR, '#submitButton')
    # 全选
    check_all_loc = (By.CSS_SELECTOR, '#dataMateriaTable > thead > tr > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 添加
    primary_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[3]/div[1]/a')
    # 确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 联采，第一列物资勾选
    check_first_goods_loc = (By.CSS_SELECTOR, '#dataMateriaTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')

    # 选择合同
    def select_hetong(self):
        return self.select_by_text(element=self.find_element(*self.select_hetong_loc), text='结算所属机构测试合同(结算所属机构测试合同)')

    # 联采-选择合同
    def select_liancai_hetong(self):
        return self.select_by_text(element=self.find_element(*self.select_hetong_loc), text='物资结算汇总联采合同(物资结算汇总联采合同)')

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_loc).click()

    # 选择全选
    def click_check_all(self):
        return self.find_element(*self.check_all_loc).click()

    # 点击第一列物资勾选
    def click_first_check(self):
        return self.find_element(*self.check_first_goods_loc).click()

    # 点击添加
    def click_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()
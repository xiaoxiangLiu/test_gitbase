__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By


class Tianjia_Wuzi_Detail(Page):

    '''添加物资详情页'''


    # 选择年份
    select_year_loc = (By.CSS_SELECTOR, '#planYear')
    # 选择季度
    select_qtr_loc = (By.CSS_SELECTOR, '#planQtr')
    # 搜索
    search_loc = (By.CSS_SELECTOR, '#submitButton')
    # 全选
    check_all_loc = (By.XPATH, '//*[@id="goodsTable"]/thead/tr[1]/th[1]/div[1]/input')
    # 添加
    primary_loc = (By.LINK_TEXT, '添加')
    # 确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 选择第一列物资
    first_check_box_loc = (By.CSS_SELECTOR, '#goodsTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 第二列物资
    second_check_box_loc = (By.CSS_SELECTOR, '#goodsTable > tbody > tr:nth-child(2) > td.bs-checkbox > input[type="checkbox"]')

    # 选择年份
    def select_year(self):
        return self.select_by_text(element=self.find_element(*self.select_year_loc), text='2018')

    # 联采-选择年份
    def select_liancai_year(self):
        return self.select_by_text(element=self.find_element(*self.select_year_loc), text='2017')

    # 选择季度
    def select_qtr(self):
        return self.select_by_text(element=self.find_element(*self.select_qtr_loc), text='4')

    # 联采-选择季度
    def select_liancai_qtr(self):
        return self.select_by_text(element=self.find_element(*self.select_qtr_loc), text='1')

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_loc).click()

    # 点击全选
    def click_check_all(self):
        return self.find_element(*self.check_all_loc).click()

    # 点击添加
    def click_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 点击勾选第一列物资
    def click_first_check_box(self):
        return self.find_element(*self.first_check_box_loc).click()

    # 点击勾选第二列物资
    def click_second_check_box(self):
        return self.find_element(*self.second_check_box_loc).click()



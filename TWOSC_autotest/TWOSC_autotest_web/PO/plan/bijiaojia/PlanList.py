__author__ = '38720'
# coding=utf-8
from selenium import webdriver
from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanList(Page):

    '''联采比较价-列表页'''

    # 筛选区
    # 省选择框
    select_province_loc = (By.CSS_SELECTOR, '#provinceId_p')
    # 搜索按钮
    button_search_loc = (By.CSS_SELECTOR, '#form1 > div > div:nth-child(3) > div > button.btn.btn-primary')
    # 新建
    button_new_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/a[1]')
    # 删除
    button_delet_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/a[2]')
    # 开始时间控件
    input_start_time_loc = (By.XPATH, '//*[@id="beginSupplyTime"]')
    # 结束时间控件
    input_end_time_loc = (By.XPATH, '//*[@id="endSupplyTime"]')
    # 重置按钮
    button_reset_loc = (By.XPATH, '//*[@id="form1"]/div/div[3]/div/button[2]')

    # 列表
    # 第一列的省
    text_first_plan_province_loc = (By.CSS_SELECTOR, '#comparisonPriceManagement > tbody > tr:nth-child(1) > td:nth-child(4)')
    # 第一列的比较价名称
    text_first_plan_name_loc = (By.CSS_SELECTOR, '#comparisonPriceManagement > tbody > tr > td:nth-child(2) > a')
    # 第一列修改按钮
    button_first_change_loc = (By.CSS_SELECTOR, '#comparisonPriceManagement > tbody > tr:nth-child(1) > td:nth-child(8) > a')
    # 第一行所有的名称
    text_first_row_loc = (By.CSS_SELECTOR, '#comparisonPriceManagement > tbody > tr')
    # 第一列的状态
    text_first_status_loc = (By.CSS_SELECTOR, '#comparisonPriceManagement > tbody > tr:nth-child(1) > td:nth-child(7)')

    # 选择吉林省
    def select_province(self):
        self.select_by_text(self.find_element(*self.select_province_loc), '吉林省')
        return self

    # 点击搜索
    def click_search(self):
        self.find_element(*self.button_search_loc).click()
        return self

    # 文本，第一列的省
    def text_first_plan_province(self):
        return self.find_element(*self.text_first_plan_province_loc).text

    # 去除开始时间控件js只读属性,输入时间
    def delete_start_time_js(self):
        js = "document.getElementById('beginSupplyTime').removeAttribute('readonly')"
        self.script(js)
        self.find_element(*self.input_start_time_loc).send_keys('2017-11')
        return self

    # 去除结束时间控件js只读属性，输入时间
    def delete_end_time_js(self):
        js = "document.getElementById('endSupplyTime').removeAttribute('readonly')"
        self.script(js)
        self.find_element(*self.input_end_time_loc).send_keys('2017-12')
        return self

    # 文本，第一列比较价名称
    def text_first_plan_name(self):
        return self.find_element(*self.text_first_plan_name_loc).text

    # 文本，第一列状态
    def text_first_status(self):
        return self.find_element(*self.text_first_status_loc).text

    # 点击，新建
    def click_new(self):
        self.find_element(*self.button_new_loc).click()
        return self

    # 获取所有的比较价名称元素，并判断是否是新建的比较价
    def judge_new(self):
        text = self.find_elements(*self.text_first_row_loc)
        for i in text:
            if i.text == '自动化联采比较价测试':
                index = i.get_attribute()




    # 点击，第一列修改
    def click_first_change(self):
        self.find_element(*self.button_first_change_loc).click()
        return self



__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By



class addPeople(Page):

    '''增加审批人员'''

    # 手机号输入框
    input_phoneNum_loc = (By.XPATH, '//*[@id="userId"]')

    # 搜索按钮
    search_loc = (By.XPATH, '//*[@id="workflow-userModel"]/div[2]/form/div/div[2]/div/button[1]')

    # 勾选审批人员
    check_loc = (By.CSS_SELECTOR, '#workflowUserTable > tbody > tr > td.bs-checkbox > input[type="radio"]')

    # 确定
    primary_loc = (By.LINK_TEXT, '确定')



    def add_people(self, phoneNum):
        self.find_element(*self.input_phoneNum_loc).send_keys(phoneNum)
        self.find_element(*self.search_loc).click()
        self.find_element(*self.check_loc).click()
        self.find_element(*self.primary_loc).click()





__author__ = '38720'
#coding=utf-8
from base_page import base
from selenium.webdriver.common.by import By

class gongquBuzhangMyoffice(base.Page):

    '''工区物资部长登陆类'''
    login_username_loc = (By.CSS_SELECTOR, 'input#userid')
    login_password_loc = (By.CSS_SELECTOR, 'input[placeholder="输入密码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button#logintSubBut')
    myOffice_loc = (By.LINK_TEXT, '我的办公室')

    # 待办事项
    daibanShixiang_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(4) > div')
    # 待办事项中新建的结算单
    new_jiesuan_loc = (By.LINK_TEXT, 'MH-2017年-9月水泥结算dan')
    # 待办事项中新建的联采结算单
    liancai_new_jiesuan_loc = (By.LINK_TEXT, '联采-MH-2017年-9月水泥结算dan')


    def gongquBuzhangMyofficeLogin(self, username='13843502627', password='123456'):
        self.open()
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
        self.find_element(*self.login_btn_loc).click()
        self.find_element(*self.myOffice_loc).click()


    # 移动鼠标到待办事项
    def move_to_daiban(self):
        self.move_to_element(self.find_element(*self.daibanShixiang_loc))
        return self

    # 点击结算单
    def click_new_jiesuan(self):
        self.find_element(*self.new_jiesuan_loc).click()
        return self

    # 点击新建的联采结算单
    def click_liancai_new_jiesuan(self):
        self.find_element(*self.liancai_new_jiesuan_loc).click()
        return self

    # 切换标签页
    def select_to_window(self):
        self.window_by_index()
        return self
__author__ = '38720'
#coding=utf-8
from base_page import base
from selenium.webdriver.common.by import By

class gongquYanshouMyoffice(base.Page):

    login_username_loc = (By.CSS_SELECTOR, 'input#userid')
    login_password_loc = (By.CSS_SELECTOR, 'input[placeholder="输入密码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button#logintSubBut')
    myOffice_loc = (By.LINK_TEXT, '我的办公室')

    def gongquYanshouMyofficeLogin(self, username = '13843502629', password = '123456'):

        self.open()
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
        self.find_element(*self.login_btn_loc).click()
        self.find_element(*self.myOffice_loc).click()


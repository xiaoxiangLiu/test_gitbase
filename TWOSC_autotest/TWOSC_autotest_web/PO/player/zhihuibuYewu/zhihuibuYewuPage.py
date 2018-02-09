__author__ = '38720'
#coding=utf-8
from base_page import base
from selenium.webdriver.common.by import By

class zhihuibuYewuMyoffice(base.Page):

    login_username_loc = (By.CSS_SELECTOR, 'input#userid')
    login_password_loc = (By.CSS_SELECTOR, 'input[placeholder="输入密码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button#logintSubBut')
    myOffice_loc = (By.LINK_TEXT, '我的办公室')

    # 待办事项
    daibanShixiang_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(4) > div')
    # 待办事项弹出框第一列
    wait_box_first_loc = (By.CSS_SELECTOR, '#workItemList > li:nth-child(1) > div:nth-child(2) > a')
    # 抽样检验
    chouyang_jianyan_loc = (By.CSS_SELECTOR, '#menu_154 > a > span')
    # 待办事项中新建的结算单loc
    jiesuan_new_loc = (By.LINK_TEXT, 'MH-2017年-9月水泥结算dan')
    # 待办事项中新建的联采结算单
    liancai_new_jiesuan_loc = (By.LINK_TEXT, '联采-MH-2017年-9月水泥结算dan')



    def zhihuibuYewuMyofficeLogin(self, username='13843502623', password='123456'):

        self.open()
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
        self.find_element(*self.login_btn_loc).click()
        self.find_element(*self.myOffice_loc).click()
        return True

    # 移动鼠标到待办事项
    def move_to_daiban(self):
        self.move_to_element(self.find_element(*self.daibanShixiang_loc))
        return self

    # 点及待办事项第一列
    def click_first_wait_box(self):
        return self.find_element(*self.wait_box_first_loc).click()

    # 点击抽样检验
    def click_chouyang(self):
        return self.find_element(*self.chouyang_jianyan_loc).click()

    #点击新建的结算单
    def click_jiesuan(self):
        self.find_element(*self.jiesuan_new_loc).click()
        return self

    # 点击新建的联采结算单
    def click_liancai_jiesuan(self):
        self.find_element(*self.liancai_new_jiesuan_loc).click()
        return self

    # 切换标签页
    def select_window(self):
        self.window_by_index()
        return self


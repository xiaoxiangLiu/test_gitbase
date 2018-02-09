__author__ = '38720'
#coding=utf-8

from selenium.webdriver.common.by import By
from base_page.base import Page
import time



class gongquYewuMyoffice(Page):

    '''工区业务人员我的办公室页面'''

    login_username_loc = (By.CSS_SELECTOR, 'input#userid')
    login_password_loc = (By.CSS_SELECTOR, 'input[placeholder="输入密码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button#logintSubBut')
    #  工区业务人员页面logo loc
    logo_loc = (By.CSS_SELECTOR, 'img.logo-lg')
    # 滑动按钮loc
    sidebarToggle_loc = (By.CSS_SELECTOR, 'a.sidebar-toggle')
    # 搜索按钮loc
    search_loc = (By.CSS_SELECTOR, 'a.fa.fa-search')
    # 我的办公室loc
    myOffice_loc = (By.LINK_TEXT, '我的办公室')
    # 待办事项loc
    daiBanShiXiang_loc = (By.CSS_SELECTOR, 'div.btn_wait')
    # 待办事项中新建的结算单loc
    jiesuan_new_loc = (By.LINK_TEXT, 'MH-2017年-9月水泥结算dan')
    # 待办事项中新建的联采结算单
    liancai_jiesuan_new_loc = (By.LINK_TEXT, '联采-MH-2017年-9月水泥结算dan')
    # 消息loc
    xiaoXi_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(5) > a')
    # 消息通知
    xiaoxi_tongzhi_loc = (By.CSS_SELECTOR, 'body > div.wrapper > div:nth-child(5) > div > div > div.box-header.with-border > h3')
    #  您好工区业务人员按钮loc
    gongquYewu_loc = (By.CSS_SELECTOR, 'button#dropdownMenu_op')
    # 推出按钮loc
    tuiChu_loc = (By.LINK_TEXT, '退出')
    # 点击选择工区按钮loc
    button_xuanzeGongqu_loc = (By.CSS_SELECTOR, 'button#dropdownMenu1')
    # MHTJ-23标一工区loc
    button_mhtj23biaoyigongqu_loc = (By.LINK_TEXT, 'MHTJ-23标一工区')


    def gongquYewuMyofficeLogin(self,username='13843502628',password='123456'):
        self.open()
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
        self.find_element(*self.login_btn_loc).click()
        self.find_element(*self.myOffice_loc).click()




    # 搜索按钮点击成功loc
    search_succeed_loc = (By.CSS_SELECTOR, 'span.search.pull-left')

    # 滑动按钮点击成功判断loc
    huadonganniu_succeed_loc = (By.CSS_SELECTOR, 'i.fa.fa_ico_jihua')

    # 切换到MHTJ-23标一工区判断loc
    mhtj23biaoyigongqu_succeed_loc = (By.CSS_SELECTOR, 'button#dropdownMenu1')

    # 点击工区选择按钮
    def click_xuanzegongqu(self):
        self.find_element(*self.button_xuanzeGongqu_loc).click()
        time.sleep(0.5)
        return self

    # 点击MHTJ-23标一工区
    def click_gongqu(self):
        self.find_element(*self.button_mhtj23biaoyigongqu_loc).click()
        return self

    # 点击消息按钮
    def click_xiaoxi(self):
        self.find_element(*self.xiaoXi_loc).click()
        return self

    # 移动鼠标到待办事项
    def move_to_daiban(self):
        self.move_to_element(self.find_element(*self.daiBanShiXiang_loc))
        return self

    # 点击新建的结算单
    def click_jiesuan(self):
        self.find_element(*self.jiesuan_new_loc).click()
        return self

    # 点击新建的联采结算单
    def click_liancai_jiesuan(self):
        self.find_element(*self.liancai_jiesuan_new_loc).click()
        return self

    # 切换标签页
    def select_window(self):
        self.window_by_index()
        return self








__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By

class mainMenu(Page):


    ''' 导航栏 '''

    # 供应商公司选择
    gongquXuanze_loc = (By.CSS_SELECTOR, '#dropdownMenu1')
    # 我的办公室
    bangongShi_loc = (By.LINK_TEXT, '我的办公室')
    # 待办事项
    daibanShixiang_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(4) > div')
    # 待办事项弹出框第一列
    waitboxfirst_loc = (By.CSS_SELECTOR, '#workItemList > li:nth-child(1) > div:nth-child(2) > a')
    # 消息
    xiaoXi_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(5) > a')
    # 右上角下拉按钮
    dropdown_loc = (By.CSS_SELECTOR, '#dropdownMenu_op')
    # 登出
    logout_loc = (By.LINK_TEXT, '退出')

    ''' 主菜单 '''

    # 发货单
    fahuodan_loc = (By.CSS_SELECTOR, '#menu_150 > a > span')
    # 结算票据
    jiesuan_loc = (By.CSS_SELECTOR, '#menu_160 > a > span')




    # 点击主菜单发货单
    def click_mainmenu_fahuodan(self):
        return self.find_element(*self.fahuodan_loc).click()

    # 点击主菜单结算票据
    def click_jiesuan(self):
        return self.find_element(*self.jiesuan_loc).click()





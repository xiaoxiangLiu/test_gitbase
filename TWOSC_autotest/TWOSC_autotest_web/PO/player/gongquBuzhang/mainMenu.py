__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class mainMenu(Page):

    '''主菜单'''

    ''' 导航栏 '''


    # 工区选择
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
    # 待办事项中新建的结算单
    new_jiesuan_loc = (By.LINK_TEXT, 'MH-2017年-9月水泥结算dan')


    def click_audit_plan(self):
        return self.find_element(*self.waitboxfirst_loc).click()

    # 移动鼠标到待办事项
    def move_to_daiban(self):
        self.move_to_element(self.find_element(*self.daibanShixiang_loc))
        return self

    # 点击结算单
    def click_new_jiesuan(self):
        self.find_element(*self.new_jiesuan_loc).click()
        return self
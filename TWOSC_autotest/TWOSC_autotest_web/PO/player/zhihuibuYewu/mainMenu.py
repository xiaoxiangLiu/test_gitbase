__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):

    '''指挥部业务人员-主菜单页'''

    # 待办事项
    daibanShixiang_loc = (By.CSS_SELECTOR, 'body > header:nth-child(1) > nav > div.navbar-custom-menu > ul > li:nth-child(4) > div')
    # 待办事项弹出框第一列
    wait_box_first_loc = (By.CSS_SELECTOR, '#workItemList > li:nth-child(1) > div:nth-child(2) > a')
    # 抽样检验
    chouyang_jianyan_loc = (By.CSS_SELECTOR, '#menu_154 > a > span')



    # 移动鼠标到待办事项
    def move_to_daiban(self):
        return self.move_to_element(self.find_element(*self.daibanShixiang_loc))

    # 点及待办事项第一列
    def click_first_wait_box(self):
        return self.find_element(*self.wait_box_first_loc).click()

    # 点击抽样检验
    def click_chouyang(self):
        return self.find_element(*self.chouyang_jianyan_loc).click()
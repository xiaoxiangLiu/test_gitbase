__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class mainMenu(Page):

    '''页面元素'''

    '''  竖向主菜单栏  '''

    # 总/年度需求计划
    xuqiujihua_loc = (By.CSS_SELECTOR, '#menu_152 > a > span')
    # 施工清单
    shigongQingdan_loc = (By.CSS_SELECTOR, '#menu_164 > a > span')
    # 地材月报
    dicaiYuebao_loc = (By.CSS_SELECTOR, '#menu_75752767881002 > a > span')
    # 批次招标
    piciZhaobiao_loc = (By.CSS_SELECTOR, '#menu_75752767881002 > a > span')
    # 发货单
    fahuoDan_loc = (By.CSS_SELECTOR, '#menu_75752767881002 > a > span')
    # 季度分月
    jiduFenyue_loc = (By.CSS_SELECTOR, '#menu_170 > a > span')
    # 问题处理
    wentiChuli_loc = (By.CSS_SELECTOR, '#menu_163 > a > span')
    # 使用位置
    shiyongWeizhi_loc = (By.CSS_SELECTOR, '#menu_81688988978001 > a > span')
    # 结算票据
    jiesuanPiaojv_loc = (By.CSS_SELECTOR, '#menu_81688988978001 > a > span')


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

    '''筛选区'''

    # 甲供
    jiagong_loc = (By.LINK_TEXT, '甲供')
    # 联采
    liancai_loc = (By.LINK_TEXT, '联采')
    # 所属机构选择框
    suoshujigou_loc = (By.CSS_SELECTOR, '#containerName')
    # 季度选择框
    jidu_loc = (By.CSS_SELECTOR, '#demandPlanParamsForm > div > div:nth-child(2) > div > select')
    # 审批状态选择框
    shenpizhuangtai_loc = (By.CSS_SELECTOR, '#demandPlanParamsForm > div > div:nth-child(3) > div > select')
    # 计划名称输入框
    jihuamingcheng_loc = (By.CSS_SELECTOR, '#planName')
    # 搜索按钮
    sousuo_loc = (By.CSS_SELECTOR, '#submitButton')
    # 重置按钮
    chongzhi_loc = (By.CSS_SELECTOR, '#btnReset')

    def click_mainmenu_jidufenyue(self):
        return self.driver.find_element(*self.jiduFenyue_loc).click()



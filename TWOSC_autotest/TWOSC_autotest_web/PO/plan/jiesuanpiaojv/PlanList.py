__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By
import time



class PlanList(Page):

    # 结算单名称搜索输入框
    input_jiesuan_name_loc = (By.CSS_SELECTOR, '#settlementBillsNameInput')
    # 供应商搜索输入框
    input_gongyingshang_loc = (By.CSS_SELECTOR, '#supplier')
    # 合同编号搜索输入框
    input_plan_number_loc = (By.CSS_SELECTOR, '#contractNo')
    # 制表人搜索输入框
    input_greate_name_loc = (By.CSS_SELECTOR, '#createName')
    # 制单时间
    input_time_loc = (By.CSS_SELECTOR, '#createTime')
    # 时间控件，起始时间
    input_start_time_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/div[1]/input')
    # 时间控件，结束时间
    input_end_time_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/input')
    # 时间控件，确定
    button_time_primary_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/button[1]')
    # 状态搜索输入框
    input_status_loc = (By.CSS_SELECTOR, '#approvalStatusCode')
    # 搜索按钮
    button_search_loc = (By.CSS_SELECTOR, '#settlementListForm > div > div:nth-child(9) > div > button.btn.btn-primary')
    # 重置按钮
    button_chongzhi_loc = (By.CSS_SELECTOR, '#settlementListForm > div > div:nth-child(9) > div > button.btn.btn-default')
    # 第一列结算单名称
    text_first_plan_name_loc = (By.CSS_SELECTOR, '#settlementListTableJG > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    # 联采第一列结算名称
    text_liancai_first_plan_name_loc = (By.CSS_SELECTOR, '#settlementListTableLC > tbody > tr:nth-child(1) > td:nth-child(2) > a')
    # 联采第一列结算单供应商
    text_liancai_first_gongyingshang_loc = (By.CSS_SELECTOR, '#settlementListTableLC > tbody > tr:nth-child(1) > td:nth-child(3)')
    # 第一列供应商文本
    text_first_gongyingshang_loc = (By.CSS_SELECTOR, '#settlementListTableJG > tbody > tr:nth-child(1) > td:nth-child(3)')
    # 第一列合同编号
    text_first_plan_number_loc = (By.CSS_SELECTOR, '#settlementListTableJG > tbody > tr > td:nth-child(5)')
    # 联采-第一列合同编号
    text_liancai_first_plan_number_loc = (By.CSS_SELECTOR, '#settlementListTableLC > tbody > tr:nth-child(1) > td:nth-child(5)')
    # 第一列制单人
    text_first_plan_greater_loc = (By.CSS_SELECTOR, '#settlementListTableJG > tbody > tr:nth-child(1) > td:nth-child(6)')
    # 联采-第一列制单人
    text_liancai_first_plan_greater_loc = (By.CSS_SELECTOR, '#settlementListTableLC > tbody > tr:nth-child(1) > td:nth-child(6)')
    # 第一列状态
    text_first_plan_status_loc = (By.CSS_SELECTOR, '#settlementListTableJG > tbody > tr:nth-child(1) > td:nth-child(8)')
    # 联采-第一列状态
    text_liancai_first_status_loc = (By.CSS_SELECTOR, '#settlementListTableLC > tbody > tr:nth-child(1) > td:nth-child(8)')

    # 新建
    button_new_plan_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/a[1]')
    # 新建的结算单，Link_text定位
    new_plan_loc = (By.LINK_TEXT, 'MH-2017年-9月水泥结算dan')
    # 新建联采结算单，link_text
    new_liancai_plan_loc = (By.LINK_TEXT, '联采-MH-2017年-9月水泥结算dan')
    # 联采
    button_liancai_loc = (By.LINK_TEXT, '联采')



    # 结算单名称输入数据
    def send_jiesuan_name(self):
        self.find_element(*self.input_jiesuan_name_loc).send_keys('2015')
        return self

    # 联采-结算单名称输入数据
    def send_liancai_jiesuan_name(self):
        self.find_element(*self.input_jiesuan_name_loc).send_keys('2016')
        return self

    # 合同编号输入数据
    def send_plan_number(self):
        self.find_element(*self.input_plan_number_loc).send_keys('123')
        return self

    # 联采-合同编号输入数据
    def send_liancai_plan_number(self):
        self.find_element(*self.input_plan_number_loc).send_keys('app')
        return self

    # 供应商搜索输入数据
    def send_gongyingshang(self):
        self.find_element(*self.input_gongyingshang_loc).send_keys('蒙西')
        return self

    # 联采-供应商搜索输入数据
    def send_liancai_gongyingshang(self):
        self.find_element(*self.input_gongyingshang_loc).send_keys('衡水')
        return self

    # 制单人搜索输入数据
    def send_greate_name(self):
        self.find_element(*self.input_greate_name_loc).send_keys('杨延勇')
        return self

    # 状态搜索框
    def status_search(self):
        return self.find_element(*self.input_status_loc)

    # 状态搜索-编制中
    def select_bianzhizhong(self):
        self.select_by_index(self.status_search(), 1)
        return self

    # 状态搜索-审核中
    def select_shenhezhong(self):
        self.select_by_index(self.status_search(), 2)
        return self

    # 状态搜索-已批准
    def select_yipizhun(self):
        self.select_by_index(self.status_search(), 3)
        return self

    # 状态搜索-已结算
    def select_yijiesuan(self):
        self.select_by_index(self.status_search(), 4)
        return self

    # 状态搜索-已驳回
    def select_yibohui(self):
        self.select_by_index(self.status_search(), 5)
        return self

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.button_search_loc).click()

    # 制单时间输入时间
    def send_time(self):
        self.find_element(*self.input_time_loc).click()
        time.sleep(0.5)
        self.find_element(*self.input_start_time_loc).clear()
        self.find_element(*self.input_start_time_loc).send_keys('2016-06-07')
        time.sleep(0.5)
        self.find_element(*self.input_end_time_loc).clear()
        self.find_element(*self.input_end_time_loc).send_keys('2016-11-04')
        time.sleep(0.5)
        self.find_element(*self.button_time_primary_loc).click()
        return self

    # 文本，第一列结算单名称
    def text_first_plan_name(self):
        return self.find_element(*self.text_first_plan_name_loc).text

    # 文本，联采第一列结算单名称
    def text_liancai_first_plan_name(self):
        return self.find_element(*self.text_liancai_first_plan_name_loc).text

    # 文本，第一列结算单供应商
    def text_first_plan_gongyingshang(self):
        return self.find_element(*self.text_first_gongyingshang_loc).text

    # 文本，联采-第一列结算单供应商
    def text_liancai_first_gongyingshang(self):
        return self.find_element(*self.text_liancai_first_gongyingshang_loc).text

    # 文本，第一列结算单合同编号
    def text_first_plan_number(self):
        return self.find_element(*self.text_first_plan_number_loc).text

    # 文本，第一列结算单合同编号
    def text_liancai_first_plan_number(self):
        return self.find_element(*self.text_liancai_first_plan_number_loc).text

    # 文本，第一列结算单制单人
    def text_first_plan_greater(self):
        return self.find_element(*self.text_first_plan_greater_loc).text

    # 文本，联采-第一列结算单制单人
    def text_liancai_first_plan_greater(self):
        return self.find_element(*self.text_liancai_first_plan_greater_loc).text

    # 文本，第一列状态
    def text_first_plan_status(self):
        return self.find_element(*self.text_first_plan_status_loc).text

    # 文本，联采-第一列状态
    def text_liancai_first_status(self):
        return self.find_element(*self.text_liancai_first_status_loc).text

    # 点击新建
    def click_new_plan(self):
        self.find_element(*self.button_new_plan_loc).click()
        return self

    # 切换标签页
    def select_to_window(self):
        return self.window_by_index()

    # 点击新建的结算单
    def click_new(self):
        self.find_element(*self.new_plan_loc).click()
        return self

    # 点击新建的联采结算单
    def click_liancai_new(self):
        self.find_element(*self.new_liancai_plan_loc).click()
        return self

    # 联采
    def click_liancai(self):
        self.find_element(*self.button_liancai_loc).click()
        return self







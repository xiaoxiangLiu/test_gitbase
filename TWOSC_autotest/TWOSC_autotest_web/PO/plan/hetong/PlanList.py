__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class PlanList(Page):

    '''筛选区'''

    # 甲供
    jiagong_loc = (By.LINK_TEXT, '甲供')
    # 联采
    liancai_loc = (By.LINK_TEXT, '联采')
    # 合同编号
    contract_number_loc = (By.CSS_SELECTOR, '#contractNumber')
    # 合同名称
    fahuodan_name_loc = (By.CSS_SELECTOR, '#name')
    # 状态
    zhuangtai_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm > div > div:nth-child(3) > div > select')
    # 供应商
    seller_company_name_loc = (By.CSS_SELECTOR, '#sellerCompanyName')
    # 发货人
    sale_user_name_loc = (By.CSS_SELECTOR, '#saleOperationUserName')
    # 搜索
    search_loc = (By.CSS_SELECTOR, '#submitButton')
    # 出库时间
    creat_time_loc = (By.CSS_SELECTOR, '#createTimeStr')
    # 所属机构
    jigou_loc = (By.CSS_SELECTOR, '#containerName')



    # 合同编号输入数据
    def send_contract_number(self):
        return self.find_element(*self.contract_number_loc).send_keys('app')

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_loc).click()

    # 发货单名称输入数据
    def send_fahuodan_name(self):
        return self.find_element(*self.fahuodan_name_loc).send_keys('97')

    # 状态搜索-编制中
    def select_bianzhizhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='编制中')

    # 状态搜索-审批中
    def select_shenpizhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='审批中')

    # 状态搜索-发货中
    def select_fahuozhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='发货中')

    # 状态搜索-初验中
    def select_chuyanzhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='初验中')

    # 状态搜索-会签中
    def select_huiqianzhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='会签中')

    # 状态搜索-待抽样
    def select_daichouyang(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='待抽样')

    # 状态搜索-抽样中
    def select_chouyangzhong(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='抽样中')

    # 状态搜索-完成
    def select_wancheng(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='完成')

    # 状态搜索-结算编制中
    def select_jiesuan(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='结算编制中')

    # 状态搜索-结算完成
    def select_jiesuanWancheng(self):
        return self.select_by_text(element=self.find_element(*self.zhuangtai_loc), text='结算完成')

    # 供应商搜索输入数据
    def send_gongyingshang(self):
        return self.find_element(*self.seller_company_name_loc).send_keys('衡水')

    # 发货人搜索输入数据
    def send_sale_user(self):
        return self.find_element(*self.sale_user_name_loc).send_keys('杨')

    # 用js去除时间控件
    def time_remove_js(self):
        js = "$('input[id=createTimeStr]').removeAttr('readonly')"
        return self.script(js)

    # 输入出库时间
    def send_create_time(self):
        return self.find_element(*self.creat_time_loc).send_keys('2016-10-10 - 2017-10-10')



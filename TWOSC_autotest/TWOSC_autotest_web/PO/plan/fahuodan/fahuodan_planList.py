__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class Planlist(Page):

    '''发货单页面类-计划列表页'''

    # 创建发货单
    new_plan_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div/a[1]')
    # 删除
    delete_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div/a[2]')
    # 物资统计
    wuzitongji_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div/a[3]')
    # 第一列合同
    first_plan_loc = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[2]/a')
    # 第一列查看详细
    first_plan_check_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(1)')
    # 第一列再次发货
    first_plan_again_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(1)')
    # 第一列发货单位
    first_company_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(7)')
    # 第一列发货人姓名
    first_user_name_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(8)')
    # 第一列发货单状态
    first_plan_status_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(9)')
    # 再次发货提示框发货单名称
    again_plan_name_loc = (By.CSS_SELECTOR, 'input#name[onblur="javascript:checkMore()"]')
    # 再次发货提示框提交
    again_plan_primary_loc = (By.CSS_SELECTOR, '#GT_CommonModal > div > div > div.box-footer > div > button.btn.btn-primary')
    # 全选
    check_all_loc = (By.CSS_SELECTOR, '#dataTable > thead > tr > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 删除失败弹出提示框文本
    text_delete_fail_loc = (By.CSS_SELECTOR, '#popup_message')
    # 第一列作废
    first_plan_zuofei_loc = (By.CSS_SELECTOR, '#dataTable > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(3)')
    # 作废理由
    zuofei_liyou_loc = (By.CSS_SELECTOR, '#cancelReason')
    # 作废提示框确定
    zuofei_queding_loc = (By.CSS_SELECTOR, '#purchaseBill_add_view > div.box-footer > div > button.btn.btn-primary')
    # 联采
    button_liancai_loc = (By.LINK_TEXT, '联采')



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
    # 时间控件确定按钮
    button_time_primary_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/button[1]')
    # 时间控件,起始时间输入框
    input_start_time_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/div[1]/input')
    # 时间控件，结束时间输入框
    input_end_time_loc = (By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/input')
    # 所属机构
    jigou_loc = (By.CSS_SELECTOR, '#containerName')
    # 时间label
    label_time_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm > div > div:nth-child(4) > label')

    # 点击联采
    def click_liancai(self):
        self.find_element(*self.liancai_loc).click()
        return self

    # 切换标签页
    def select_window(self):
        self.window_by_index()
        return self

    # 获取当前url
    def get_fahuodan_url(self):
        return self.get_url()

    # 第一列合同名称
    def text_first_plan_name(self):
        return self.find_element(*self.first_plan_loc).text

    # 第一列发货单位
    def text_first_company(self):
        return self.find_element(*self.first_company_loc).text

    # 第一列发货人姓名
    def text_first_user_name(self):
        return self.find_element(*self.first_user_name_loc).text

    # 点击全选
    def click_check_all(self):
        return self.find_element(*self.check_all_loc).click()

    # 点击删除
    def click_delete(self):
        return self.find_element(*self.delete_loc).click()

    # 删除失败文本信息
    def text_delete(self):
        return self.find_element(*self.text_delete_fail_loc).text

    # 点击新建发货单
    def click_new_plan(self):
        return self.find_element(*self.new_plan_loc).click()

    # 点击第一列发货单
    def click_first_plan(self):
        return self.find_element(*self.first_plan_loc).click()

    # 第一列作废文本
    def text_first_plan_zuofei(self):
        return self.find_element(*self.first_plan_zuofei_loc).text

    # 点击第一列作废
    def click_first_plan_zuofei(self):
        return self.find_element(*self.first_plan_zuofei_loc).click()

    # 输入作废理由
    def send_zuofei_liyou(self):
        return self.find_element(*self.zuofei_liyou_loc).send_keys('自动化测试作废')

    # 点击作废提示框确定
    def click_zuofei_queding(self):
        return self.find_element(*self.zuofei_queding_loc).click()

    # 第一列发货单状态文本
    def text_first_plan_status(self):
        return self.find_element(*self.first_plan_status_loc).text

    # 点击第一列再次发货
    def click_first_plan_again(self):
        return self.find_element(*self.first_plan_again_loc).click()

    # 再次发货输入发货单名称
    def send_again_plan_name(self):
        return self.find_elements(*self.again_plan_name_loc)[0].send_keys('自动化测试再次发货')

    # 点击再次发货确定
    def click_again_plan_primary(self):
        return self.find_element(*self.again_plan_primary_loc).click()


    # 合同编号输入数据
    def send_contract_number(self):
        return self.find_element(*self.contract_number_loc).send_keys('app')

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_loc).click()

    # 发货单名称输入数据
    def send_fahuodan_name(self):
        return self.find_element(*self.fahuodan_name_loc).send_keys('97')

    # 联采-发货单名称输入数据
    def send_liancai_fahuodan_name(self):
        self.find_element(*self.fahuodan_name_loc).send_keys('11')
        return self

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
        # self.find_element(*self.creat_time_loc).clear()
        return self.find_element(*self.creat_time_loc).send_keys('2016-10-10 - 2017-10-10')

    # 点击时间控件确定按钮
    def click_time_primary(self):
        return self.find_element(*self.button_time_primary_loc).click()

    # 点击时间输入框
    def click_time(self):
        self.find_element(*self.creat_time_loc).click()
        return self

    # 输入起始时间
    def send_start_time(self):
        self.find_element(*self.input_start_time_loc).clear()
        self.find_element(*self.input_start_time_loc).send_keys('2016-10-10')
        return self

    # 输入结束时间
    def send_end_time(self):
        self.find_element(*self.input_end_time_loc).clear()
        self.find_element(*self.input_end_time_loc).send_keys('2017-10-10')
        return self


















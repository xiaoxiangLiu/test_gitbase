__author__ = '38720'
# coding=utf-8

from selenium.webdriver.common.by import By
from base_page.base import Page
from selenium.webdriver.support import expected_conditions as EC



class planDetail(Page):

    '''标段业务人员-季度分月-子计划页面'''

    '''计划基本信息'''

    # 修改
    change_loc = (By.LINK_TEXT, '修改')
    # 工区人员审批状态
    build_people_status_loc = (By.CSS_SELECTOR, '#nodeState > div > div.col_5.active > p')

    '''物资列表'''

    # 搜索框
    search_input_loc = (By.CSS_SELECTOR, '#goodsName')
    # 搜索按钮
    search_button_loc = (By.CSS_SELECTOR, '#submitButton')
    # 重置按钮
    reset_loc = (By.CSS_SELECTOR, '#btnReset')
    # 导出
    deriver_loc = (By.CSS_SELECTOR, '#plan_table_material_view > div.pull-right.btn-group > a')
    # 全选
    check_all_loc = (By.CSS_SELECTOR, '#goodsTable > thead > tr:nth-child(1) > th.bs-checkbox > div.th-inner > input[type="checkbox"]')
    # 物资列表第一个勾选
    first_checkbox_loc = (By.CSS_SELECTOR, '#goodsTable > tbody > tr:nth-child(1) > td.bs-checkbox > input[type="checkbox"]')
    # 物资列表第一列编辑物资
    first_edit_loc = (By.CSS_SELECTOR, '#goodsTable > tbody > tr:nth-child(1) > td:nth-child(17) > a:nth-child(1)')
    # 物资列表第一列移除
    first_remove_loc = (By.CSS_SELECTOR, '#goodsTable > tbody > tr:nth-child(1) > td:nth-child(17) > a:nth-child(2)')

    '''各工区计划列表'''

    # 添加子计划
    add_son_plan_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[4]/a[1]')
    # 分工区查看按钮
    check_work_area_loc = (By.CSS_SELECTOR, 'body > div.wrapper > div:nth-child(5) > div > div > div.tool-bar.clearfix > a:nth-child(2)')
    # 计划列表第一列第一个名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#childContainerPlanTable > tbody > tr > td:nth-child(1) > a')
    # 计划列表第一列移除
    first_plan_remove_loc = (By.CSS_SELECTOR, '#childContainerPlanTable > tbody > tr > td:nth-child(7) > a:nth-child(1)')
    # 计划列表第一列驳回
    first_plan_reject_loc = (By.CSS_SELECTOR, '#childContainerPlanTable > tbody > tr > td:nth-child(7) > a:nth-child(2)')

    '''选择审批人员'''

    # 删除审批人员
    delet_people_loc = (By.CSS_SELECTOR, 'a.btn_remove')
    # 添加施工单位审批人员
    add_build_people_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(3) > td.col-xs-10 > a')
    # 添加服务机构审批人员
    add_server_people_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(4) > td.col-xs-10 > a')
    # 添加指挥部审批人员
    add_headquarters_loc = (By.CSS_SELECTOR, '#addActor > tr:nth-child(5) > td.col-xs-10 > a')
    # 备注
    remak_loc = (By.CSS_SELECTOR, '#remark')

    # 提交
    submit_loc = (By.LINK_TEXT, '提交')
    # 保存
    save_loc = (By.LINK_TEXT, '保存')

    # 确认
    confirm_loc = (By.CSS_SELECTOR, '#popup_ok')

    # 手机号输入框
    input_phoneNum_loc = (By.XPATH, '//*[@id="userId"]')

    # 搜索按钮
    search_loc = (By.XPATH, '//*[@id="workflow-userModel"]/div[2]/form/div/div[2]/div/button[1]')

    # 勾选审批人员
    check_loc = (By.CSS_SELECTOR, '#workflowUserTable > tbody > tr > td.bs-checkbox > input[type="radio"]')

    # 确定
    primary_loc = (By.LINK_TEXT, '确定')


    # 工区人员审批状态
    def build_people_status(self):
        return self.find_element(*self.build_people_status_loc).text

    # 判断服务机构审批人员元素是否可见
    def visibility_by_element_server(self):
        return EC.visibility_of_element_located(*self.add_server_people_loc)

    # 判断指挥部审批人员按钮是否可见
    def visibility_by_element_headquarters(self):
        return EC.visibility_of_element_located(*self.add_headquarters_loc)

    # 点击修改
    def click_change(self):
        return self.find_element(*self.change_loc).click()

    # 在搜索框输入数据
    def send_value_search(self, text):
        return self.find_element(*self.search_input_loc).send_keys(text)

    # 点击搜索
    def click_search(self):
        return self.find_element(*self.search_button_loc).click()

    # 点击导出
    def click_deriver(self):
        return self.find_element(*self.deriver_loc).click()

    # 点击添加子计划
    def click_add_son_plan(self):
        return self.find_element(*self.add_son_plan_loc).click()

    # 判断添加子计划
    def assert_son_plan(self):
        return self.find_element(*self.first_plan_remove_loc)

    # 点击删除审批人员按钮
    def click_remove_people(self):
        return self.find_element(*self.delet_people_loc).click()

    # 点击添加施工单位审批人员按钮
    def click_add_build_people(self):
        return self.find_element(*self.add_build_people_loc).click()

    # 点击添加服务机构审批人员按钮
    def click_add_server_people(self):
        return self.find_element(*self.add_server_people_loc).click()

    # 点击添加指挥部审批人员按钮
    def click_add_headquarters_people(self):
        return self.find_element(*self.add_headquarters_loc).click()

    # 添加备注
    def add_remark(self, text):
        return self.find_element(*self.remak_loc).send_keys(text)

    # 点击提交
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 点击确认
    def click_confirm(self):
        return self.find_element(*self.confirm_loc).click()

    # 添加施工单位审批人员
    def add_build_people(self):
        self.find_element(*self.add_build_people_loc).click()
        self.find_element(*self.input_phoneNum_loc).send_keys('13843502627')
        self.find_element(*self.search_loc).click()
        self.find_element(*self.check_loc).click()
        self.find_element(*self.primary_loc).click()
        return True

    # 添加指挥部业务人员
    def add_head_people(self):
        self.find_element(*self.add_headquarters_loc).click()
        self.find_element(*self.input_phoneNum_loc).send_keys('13843502623')
        self.find_element(*self.search_loc).click()
        self.find_element(*self.check_loc).click()
        self.find_element(*self.primary_loc).click()















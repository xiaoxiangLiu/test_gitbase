__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By

class NewPlanDetail(Page):

    '''新建发货单详情页'''

    # 发货单状态
    fahuodan_status_loc = (By.CSS_SELECTOR, '#zdispatchBillStatus')
    # 出库时间文本信息
    chuku_time_status_loc = (By.CSS_SELECTOR, '#zwareHouseTimeStr')
    # 编辑
    edit_loc = (By.CSS_SELECTOR, 'body > div.wrapper > div > div:nth-child(1) > div > div.box-body > div:nth-child(3) > div > a')
    # 选择物资
    xuanze_wuzi_loc = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[4]/div/a[1]')
    # 添加物资
    tianjia_wuzi_loc = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[4]/div/a[2]')
    # 批量编辑
    piliang_bianji_loc = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[4]/div/a[3]')
    # 复制
    copy_loc = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[4]/div/a[4]')
    # 物资列表删除
    delete_loc = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[4]/div/a[5]')
    # 全选
    check_all_loc = (By.XPATH, '//*[@id="addTable"]/thead/tr/th[1]/div[1]/input')

    # 第一列发货单名称
    first_plan_name_loc = (By.CSS_SELECTOR, '#addTable > tbody > tr > td:nth-child(2)')
    # 第二列发货单名称
    second_plan_name_loc = (By.CSS_SELECTOR, '#addTable > tbody > tr:nth-child(2) > td:nth-child(2)')
    # 第一列生产批次号
    first_plan_batch_loc = (By.CSS_SELECTOR, '#addTable > tbody > tr:nth-child(1) > td:nth-child(5)')

    # 文件上传
    send_file_loc = (By.CSS_SELECTOR, '#related_file_list_view_info > div.pull-right.btn-group > a:nth-child(1)')
    # 文件部分删除
    delete_file_loc = (By.CSS_SELECTOR, '#related_file_list_view_info > div.pull-right.btn-group > a.btn.btn-tool-del')
    # 测试lable
    test_table_loc = (By.CSS_SELECTOR, '#addTable > tbody > tr:nth-child(10) > td:nth-child(2)')
    # 提交
    primary_loc = (By.LINK_TEXT, '提交')
    # 提示框确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')


    # 点击编辑
    def click_edit(self):
        return self.find_element(*self.edit_loc).click()

    # 发货单状态
    def text_fahuodan_status(self):
        return self.find_element(*self.fahuodan_status_loc).text

    # 出库时间状态文本
    def text_chuku_time(self):
        return self.find_element(*self.chuku_time_status_loc).text

    # 点击选择物资
    def click_xuanze_wuzi(self):

        return self.find_element(*self.xuanze_wuzi_loc).click()

    # 第一列发货单名称文本
    def text_first_plan(self):
        return self.find_element(*self.first_plan_name_loc).text

    # 第二列发货单名称文本
    def text_second_plan(self):
        return self.find_element(*self.second_plan_name_loc).text

    # 点击添加物资
    def click_tianjia_wuzi(self):
        return self.find_element(*self.tianjia_wuzi_loc).click()

    # 点击全选
    def click_check_all(self):
        return self.find_element(*self.check_all_loc).click()

    # 点击批量编辑
    def click_piliang_bianji(self):
        return self.find_element(*self.piliang_bianji_loc).click()

    # 第一列生产批次号
    def text_first_plan_batch(self):
        return self.find_element(*self.first_plan_batch_loc).text

    # 下拉滚动条到文件上传
    def down_to_element(self):
        return self.down_scroll_bar(element=self.find_element(*self.test_table_loc))

    # 文件上传
    def send_file(self):
        return self.find_element(*self.send_file_loc).send_keys('E:/TWOSC_autotest/TWOSC_autotest_web/data/11.JPG')

    # 点击提交
    def click_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()









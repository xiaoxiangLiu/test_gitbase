__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class Audit(Page):

    '''季度分月页面类-审核'''

    # 通过
    agree_loc = (By.CSS_SELECTOR, 'input[value="通过"]')
    # 驳回
    rebut_loc = (By.CSS_SELECTOR, 'input[value="驳回"]')
    # 备注
    remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    submit_loc = (By.LINK_TEXT, '提交')
    # 保存
    save_loc = (By.LINK_TEXT, '保存')
    # 指派
    reassign_loc = (By.LINK_TEXT, '指派')
    # 提示框确定
    sure_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 第三个审批人员状态信息
    third_audit_status_loc = (By.CSS_SELECTOR, '#nodeState > div > div.col_5.active > p')
    # 第四个审批人员状态信息
    fourth_audit_status_loc = (By.CSS_SELECTOR, '#nodeState > div > div:nth-child(4) > p')
    # 计划审批状态信息
    plan_status_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/form/div/div[7]/div')

    # 输入备注信息
    def add_remark(self, text):
        return self.find_element(*self.remark_loc).send_keys(text)

    # 点击通过
    def click_agree(self):
        return self.find_element(*self.agree_loc).click()

    # 点击提交
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 点击提示框确定
    def click_sure(self):
        return self.find_element(*self.sure_loc).click

    # 第三个审批人员状态信息文本
    def third_audit_status(self):
        return self.find_element(*self.third_audit_status_loc).text

    # 第四个审批人员状态信息文本
    def fourth_audit_status(self):
        return self.find_element(*self.fourth_audit_status_loc).text

    # 计划状态信息文本
    def plan_status(self):
        return self.find_element(*self.plan_status_loc).text





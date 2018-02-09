__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetailSix(Page):


    '''结算票据-第六页'''

    # 文本，第一个审核人
    text_first_auditor_loc = (By.CSS_SELECTOR, '#nodeState > div > div.col_5.active > p')
    # 文本，第二个审核人
    text_second_auditor_loc = (By.CSS_SELECTOR, '#nodeState > div > div:nth-child(3) > p')
    # 文本，第三个审核人
    text_third_auditor_loc = (By.CSS_SELECTOR, '#nodeState > div > div:nth-child(4) > p')
    # 文本，第四个审核人
    text_fourth_auditor_loc = (By.CSS_SELECTOR, '#nodeState > div > div:nth-child(5) > p')
    # 按键，导出物资设备结算清单
    button_daochu_first_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[5]/div/a[1]')
    # 按钮，导出物资设备付款申请单
    buttong_daochu_second_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[5]/div/a[2]')
    # 按钮，导出物资发票清单
    button_daochu_third_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[8]/div/a')
    # 按钮，导出发票
    button_daochu_fourth_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[11]/div/a')
    # 通过
    checkbox_agree_loc = (By.CSS_SELECTOR, 'input[value="通过"]')
    # 备注
    textarea_remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    button_primary_loc = (By.CSS_SELECTOR, '#operater > a.btn.btn-primary.btn-short.margin.submitForm')



    # 文本，第一审核人信息
    def text_first_auditor(self):
        return self.find_element(*self.text_first_auditor_loc).text

    # 文本，第二审核人信息
    def text_second_auditor(self):
        return self.find_element(*self.text_second_auditor_loc).text

    # 文本，第三审核人信息
    def text_third_auditor(self):
        return self.find_element(*self.text_third_auditor_loc).text

    # 文本，第四审核人信息
    def text_fourth_auditor(self):
        return self.find_element(*self.text_fourth_auditor_loc).text

    # 点击导出物资设备结算单
    def click_first_button(self):
        self.find_element(*self.button_daochu_first_loc).click()
        return self

    # 点击导出物资设备付款申请单
    def click_second_button(self):
        self.find_element(*self.buttong_daochu_second_loc).click()
        return self

    # 点击导出物资发票清单
    def click_third_button(self):
        self.find_element(*self.button_daochu_third_loc).click()
        return self

    # 点击导出发票
    def click_fourth_button(self):
        self.find_element(*self.button_daochu_fourth_loc).click()
        return self

    # 点击通过
    def click_ageree(self):
        self.find_element(*self.checkbox_agree_loc).click()
        return self

    # 输入备注
    def send_remark(self):
        self.find_element(*self.textarea_remark_loc).send_keys('结算单审批通过')
        return self

    # 点击提交
    def click_primary(self):
        self.find_element(*self.button_primary_loc).click()
        return self





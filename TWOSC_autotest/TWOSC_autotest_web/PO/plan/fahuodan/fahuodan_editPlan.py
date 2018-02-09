__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By


class EditPlan(Page):


    '''编辑发货单信息页'''


    # 出库时间
    chuku_time_loc = (By.CSS_SELECTOR, '#wareHouseTimeStr')
    # 出库时间选择月份按钮
    month_time_loc = (By.CSS_SELECTOR, 'body > div:nth-child(11) > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.switch')
    # 出库时间一月
    january_time_loc = (By.CSS_SELECTOR, 'body > div:nth-child(11) > div.datetimepicker-months > table > tbody > tr > td > span:nth-child(1)')
    # 出库时间一日
    day_time_loc = (By.CSS_SELECTOR, 'body > div:nth-child(11) > div.datetimepicker-days > table > tbody > tr:nth-child(2) > td:nth-child(1)')
    # 出库时间13：00
    hour_time_loc = (By.CSS_SELECTOR, 'body > div:nth-child(11) > div.datetimepicker-hours > table > tbody > tr > td > span:nth-child(14)')

    # 到货时间
    daohuo_time_loc = (By.CSS_SELECTOR, '#arriveTimeStr')
    # 到货时间选择月份
    month_time_daohuo_loc = (By.XPATH, '/html/body/div[8]/div[3]/table/thead/tr[1]/th[2]')
    # 到货时间一月
    january_time_daohuo_loc = (By.XPATH, '/html/body/div[8]/div[4]/table/tbody/tr/td/span[1]')
    # 到货时间12号
    day_time_daohuo_loc = (By.CSS_SELECTOR, 'body > div:nth-child(12) > div.datetimepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(5)')
    # 到货时间10:00
    hour_time_daohuo_loc = (By.XPATH, '/html/body/div[8]/div[2]/table/tbody/tr/td/span[11]')
    # 发货单名称lable
    fahuodan_lable_loc = (By.CSS_SELECTOR, '#editInfoForm > div > div:nth-child(1) > label')
    # 提交
    submit_loc = (By.CSS_SELECTOR, '#GT_CommonModal > div > div > div.box-footer > div > button.btn.btn-primary')


    # 移除出库时间控件
    def remove_time_js(self):
        js = "$('input[id=wareHouseTimeStr').removeAttr('readonly')"
        return self.script(js)

    # 输入出库时间
    def send_chuku_time(self):
        js = "$('input[id=wareHouseTimeStr').removeAttr('readonly')"
        self.script(js)
        return self.find_element(*self.chuku_time_loc).send_keys('2016-10-10-22:00')

    # 移除到货时间并输入时间
    def send_daohuo_time(self):
        js = "$('input[id=arriveTimeStr').removeAttr('readonly')"
        self.script(js)
        return self.find_element(*self.daohuo_time_loc).send_keys('2018-10-10-22:00')

    # 点击lable
    def click_lable(self):
        return self.find_element(*self.fahuodan_lable_loc).click()

    # 点击提交
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 点击出库时间
    def click_chuku_time(self):
        return self.find_element(*self.chuku_time_loc).click()

    # 点击选择月份
    def click_month_time(self):
        return self.find_element(*self.month_time_loc).click()

    # 点击一月
    def click_january_time(self):
        return self.find_element(*self.january_time_loc).click()

    # 点击一日
    def click_day_time(self):
        return self.find_element(*self.day_time_loc).click()

    # 点击13：00
    def click_hour_time(self):
        return self.find_element(*self.hour_time_loc).click()

    # 点击到货时间
    def click_daohuo_time(self):
        return self.find_element(*self.daohuo_time_loc).click()

    # 点击到货时间选择月份
    def click_month_daohuo(self):
        return self.find_element(*self.month_time_daohuo_loc).click()

    # 点击到货时间选择1月
    def click_january_daohuo(self):
        return self.find_element(*self.january_time_daohuo_loc).click()

    # 点击12号
    def click_day_daohuo(self):
        return self.find_element(*self.day_time_daohuo_loc).click()

    # 点击10：00
    def click_hour_daohuo(self):
        return self.find_element(*self.hour_time_daohuo_loc).click()





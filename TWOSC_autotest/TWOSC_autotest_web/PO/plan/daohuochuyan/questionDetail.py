__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class QuestionDetail(Page):

    '''到货初验-填写问题页'''

    # 问题标题
    question_title_loc = (By.CSS_SELECTOR, '#title')
    # 质量问题
    quality_question_loc = (By.XPATH, '//*[@id="createQuestion"]/div/div/div[2]/div[3]/div/div[1]/input')
    # 数量问题
    quantity_question_loc = (By.XPATH, '//*[@id="createQuestion"]/div/div/div[2]/div[3]/div/div[2]/input')
    # 问题内容
    question_content_loc = (By.XPATH, '//*[@id="contents"]')
    # 提交
    primary_loc = (By.CSS_SELECTOR, '#saveQuestion')
    # 确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')


    # 输入问题标题
    def send_question_title(self):
        return self.find_element(*self.question_title_loc).send_keys('自动问题')

    # 点击勾选质量问题
    def click_quality_question(self):
        return self.find_element(*self.quality_question_loc).click()

    # 点击勾选数量问题
    def click_quantity_question(self):
        return self.find_element(*self.quantity_question_loc).click()

    # 输入问题内容
    def send_question_content(self):
        return self.find_element(*self.question_content_loc).send_keys('自动问题内容')

    # 点击提交
    def click_question_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_question_submit(self):
        return self.find_element(*self.submit_loc).click()


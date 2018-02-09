__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class QuestionPlanDetail(Page):

    '''问题详情页'''

    # 问题标题
    question_title_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[1]/form/div[1]/div[1]/div')


    # 文本，问题标题
    def text_question_title(self):
        return self.find_element(*self.question_title_loc).text

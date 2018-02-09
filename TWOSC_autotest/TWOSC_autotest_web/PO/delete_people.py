__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class deletePeople(Page):

    '''删除审批人员'''

    delete_people_loc = (By.CSS_SELECTOR, 'a.btn_remove')


    def delete_people(self):
        delete_element = self.find_elements(*self.delete_people_loc)
        if len(delete_element) >= 1:
            for i in delete_element:
                self.find_element(*self.delete_people_loc).click()



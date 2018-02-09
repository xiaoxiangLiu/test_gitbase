__author__ = '38720'
# coding=utf-8
import unittest, time
from selenium import webdriver


class LoginTest(unittest.TestCase):

    def sub_setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    def sub_tearDown(self):
        self.driver.quit()


    def test_baidu_01(self):

        datas = ('selenium', 'python')
        for i in datas:
            with self.subTest(i=i):
                self.sub_setUp()
                self.driver.find_element_by_id('kw').send_keys(i)
                time.sleep(1)
                self.driver.find_element_by_id('su').click()
                time.sleep(2)
                text = self.driver.find_element_by_xpath('//*[@id="s_tab"]/b').text
                print(text)
                self.assertEqual(text, '网页')
                self.sub_tearDown()

class NumberTest(unittest.TestCase):

    def sub_setUp(self):
        self.list = range(0,6)

    def sub_tearDown(self):
        print('结束')

    def test_list_01(self):
        self.sub_setUp()
        for i in self.list:
            with self.subTest(msg=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()


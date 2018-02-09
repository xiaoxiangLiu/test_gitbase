__author__ = '38720'
# coding=utf-8

from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver.exe', chrome_options=option)
driver.get('https://www.baidu.com')
driver.maximize_window()
print(driver.title)
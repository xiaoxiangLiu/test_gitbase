# coding=utf-8
from selenium import webdriver
import os, time
import sys

def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('//', '/')
    base = base_dir.split('/common')[0]
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    file_path = base + '/report/image/' + now + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_img(driver, 'baidu.png')
    driver.quit()



__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By


class EditWuzi(Page):

    '''批量编辑物资页面'''

    # 车船号
    car_boat_num_loc = (By.CSS_SELECTOR, '#busNumbe')
    # 发货数量
    goods_number_loc = (By.CSS_SELECTOR, '#goodsCount')
    # 生成批次号
    goods_batch_loc = (By.CSS_SELECTOR, '#goodsBatch')
    # 原料
    yuanliao_loc = (By.CSS_SELECTOR, '#materialDescrib')
    # 工艺
    gongyi_loc = (By.CSS_SELECTOR, '#craftDescrib')
    # 出场质量检验
    chuchang_loc = (By.CSS_SELECTOR, '#exFactoryQultTestResult')
    # 上传附件
    shangchuan_loc = (By.CSS_SELECTOR, 'a#add_row.btn.text-green')
    # 保存
    save_loc = (By.CSS_SELECTOR, '#editCraftInfoDiv > div > div.box-footer > button.btn.btn-primary')

    # 输入车船号数据
    def send_car_boat_num(self):
        return self.find_element(*self.car_boat_num_loc).send_keys('京O00001')

    # 输入发货数量
    def send_goods_number(self):
        return self.find_element(*self.goods_number_loc).send_keys('1000')

    # 输入生产批次号
    def send_goods_batch(self):
        return self.find_element(*self.goods_batch_loc).send_keys('200A')

    # 输入原料
    def send_yuanliao(self):
        return self.find_element(*self.yuanliao_loc).send_keys('金克拉')

    # 输入工艺
    def send_gongyi(self):
        return self.find_element(*self.gongyi_loc).send_keys('烧制')

    # 输入出场质量检验
    def send_chuchang(self):
        return self.find_element(*self.chuchang_loc).send_keys('合格')

    # 上传附件
    def send_fujian(self):
        return self.find_element(*self.shangchuan_loc).send_keys('E:/TWOSC_autotest/TWOSC_autotest_web\data/11.JPG')

    # 点击保存
    def click_save(self):
        return self.find_element(*self.save_loc).click()



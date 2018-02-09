#coding=utf-8

from selenium.webdriver.common.by import By
from base_page.base import Page
from time import sleep

class login(Page):

    '''用户登陆页面'''

    login_username_loc = (By.CSS_SELECTOR, 'input#userid')
    login_password_loc = (By.CSS_SELECTOR, 'input[placeholder="输入密码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button#logintSubBut')

    #   输入用户名
    def log_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    #   输入密码
    def log_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #   点击登陆按钮
    def log_button(self):
        self.find_element(*self.login_btn_loc).click()

    #   统一登陆入口
    def user_login(self, username='username', password='password'):

        '''获取用户名和密码登陆'''

        self.open()
        self.log_username(username)
        self.log_password(password)
        self.log_button()
        sleep(2)

    #   工区业务人员登陆成功loc
    gongquyewu_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #   工区验收人员登陆成功loc
    gongquyanshou_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  工区实验人员登陆成功loc
    gongqushiyan_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  工区物资部长登陆成功loc
    gongquwuzibuzhang_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  供应商登陆成功loc
    gongyingshang_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  监理单位登陆成功loc
    jianlidanwei_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  标段业务人员登陆成功loc
    biaoduanyewu_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  标段物资部长登陆成功loc
    biaoduanwuzibuzhang_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  指挥部财务人员登陆成功loc
    zhihuibucaiwu_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  指挥部业务人员登陆成功loc
    zhihuibuyewu_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  服务机构登陆成功loc
    fuwujigou_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')
    #  物资设备部登陆成功loc
    wuZiSheBeiBu_login_loc = (By.XPATH, '//*[@id="dropdownMenu_op"]')


    def gongquyewu_main_login(self):
        text = self.find_element(*self.gongquyewu_login_loc).text
        return text

    def gongquyanshou_main_login(self):
        text = self.find_element(*self.gongquyanshou_login_loc).text
        return text

    def gongqushiyan_main_login(self):
        text = self.find_element(*self.gongquyanshou_login_loc).text
        return text

    def gongquwuzibuzhang_main_login(self):
        text = self.find_element(*self.gongquwuzibuzhang_login_loc).text
        return text

    def gongyingshang_main_login(self):
        text = self.find_element(*self.gongyingshang_login_loc).text
        return text

    def jianlidanwei_main_login(self):
        text = self.find_element(*self.jianlidanwei_login_loc).text
        return text

    def biaoduanyewu_main_login(self):
        text = self.find_element(*self.biaoduanyewu_login_loc).text
        return text

    def biaoduanwuzibuzhang_main_login(self):
        text = self.find_element(*self.biaoduanwuzibuzhang_login_loc).text
        return text

    def zhihuibucaiwu_main_login(self):
        text = self.find_element(*self.zhihuibucaiwu_login_loc).text
        return text

    def zhihuibuyewu_main_login(self):
        text = self.find_element(*self.zhihuibuyewu_login_loc).text
        return text

    def fuwujigou_main_login(self):
        text = self.find_element(*self.fuwujigou_login_loc).text
        return text

    def wuzishebeibu_main_login(self):
        text = self.find_element(*self.wuZiSheBeiBu_login_loc).text
        return text
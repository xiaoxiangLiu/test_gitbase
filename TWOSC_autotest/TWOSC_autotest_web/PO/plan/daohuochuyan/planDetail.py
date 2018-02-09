__author__ = '38720'
# coding=utf-8

from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanDetail(Page):

    '''到货初验详情页'''

    # 发货单名称
    plan_name_loc = (By.XPATH,  '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/form/div/div[1]/div')
    # 发货单基本信息，发货单状态
    plan_status_loc = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/form/div/div[8]/div')
    # 第一列确认数量
    first_affirm_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(1)')
    # 第二列确认数量
    second_affirm_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(2) > td:nth-child(10) > a:nth-child(1)')
    # 第三列确认数量
    thrid_affirm_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(3) > td:nth-child(10) > a:nth-child(1)')
    # 确认数量弹出框，实收数量
    affirm_accept_count_loc = (By.XPATH, '//*[@id="formSub"]/div/div/div[2]/div/div[6]/div[1]/div/input')
    # 确认数量弹出框，保存
    affirm_primary_loc = (By.CSS_SELECTOR, '#submit')
    # 确认数量弹出框，确定
    affirm_submit_loc = (By.CSS_SELECTOR, '#popup_ok')
    # 所有的确认数量
    all_affirm_loc = (By.LINK_TEXT, '确认数量')
    # 第一列加号
    first_plus_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(1) > td:nth-child(1) > a > i')
    # 第一列物资创建问题
    first_goods_great_question_loc = (By.XPATH, '//*[@id="acceptMaterialTable"]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/a')
    # 第二列加号
    second_plus_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(2) > td:nth-child(1) > a > i')
    # 第二列物资创建问题
    second_goods_great_question_loc = (By.XPATH, '//*[@id="acceptMaterialTable"]/tbody/tr[3]/td/table/tbody/tr[2]/td[3]/a')
    # 所有的加号
    all_plus_loc = (By.CSS_SELECTOR, 'a.glyphicon.glyphicon-plus.icon-plus')
    # 第一列到货数量
    first_goods_daohuo_number_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(1) > td:nth-child(9)')
    # 第二列到货数量
    second_goods_daohuo_number_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(2) > td:nth-child(9)')
    # 第三列到货数量
    thrid_goods_daohuo_number_loc = (By.CSS_SELECTOR, '#acceptMaterialTable > tbody > tr:nth-child(3) > td:nth-child(9)')
    # 第一列物资创建问题的标题
    first_goods_question_title_loc = (By.CSS_SELECTOR, '#questionTable > tbody > tr > td:nth-child(1)')
    # 第一个问题，解决问题
    first_question_solve_loc = (By.CSS_SELECTOR, '#questionTable > tbody > tr > td:nth-child(9) > a')
    # 现场指挥部添加审批人员
    xianchang_zhihuibu_shenpi_loc = (By.XPATH, '//*[@id="addActor"]/tr[5]/td[2]/a')
    # 备注
    remark_loc = (By.CSS_SELECTOR, '#remark')
    # 提交
    primary_loc = (By.LINK_TEXT, '提交')
    # 确定
    submit_loc = (By.CSS_SELECTOR, '#popup_ok')






    # 点击第一列确认数量
    def click_first_affirm(self):
        return self.find_element(*self.first_affirm_loc).click()

    # 点击第二列确认数量
    def click_second_affirm(self):
        return self.find_element(*self.second_affirm_loc).click()

    # 确认数量提示框填入数量
    def send_accept_count(self):
        return self.find_element(*self.affirm_accept_count_loc).send_keys('10')

    # 点击确认数量提示框保存按钮
    def click_affirm_primary(self):
        return self.find_element(*self.affirm_primary_loc).click()

    # 点击确认数量框确定
    def click_affirm_submit(self):
        return self.find_element(*self.affirm_submit_loc).click()

    # 文本，第一列物资实收数量
    def text_first_goods_daohuo_number(self):
        return self.find_element(*self.first_goods_daohuo_number_loc).text

    # 文本，第二列物资实收数量
    def text_second_goods_daohuo_number(self):
        return self.find_element(*self.second_goods_daohuo_number_loc).text

    # 文本，第三列物资实收数量
    def text_thrid_goods_daohuo_number(self):
        return self.find_element(*self.thrid_goods_daohuo_number_loc).text

    # 下拉滚动条到第二列确认数量
    def down_second_affirm(self):
        return self.down_scroll_bar(self.find_element(*self.second_affirm_loc))

    # 下拉滚动条到第三列确认数量
    def down_thrid_affirm(self):
        return self.down_scroll_bar(self.find_element(*self.second_affirm_loc))

    # 点击第三列确认数量
    def click_thrid_affirm(self):
        self.find_element(*self.thrid_affirm_loc).click()

    # 点击所有的确认数量并输入
    def click_send_all_affirm(self):
        all_affirm = self.find_elements(*self.all_affirm_loc)
        if len(all_affirm) >= 1:
            for i in all_affirm:
                self.find_element(*self.all_affirm_loc).click()
                self.find_element(*self.affirm_accept_count_loc).clear()
                self.find_element(*self.affirm_accept_count_loc).send_keys('3')
                self.find_element(*self.affirm_primary_loc).click()
                self.find_element(*self.affirm_submit_loc).click()

    # 点击第一列加号
    def click_first_plus(self):
        return self.find_element(*self.first_plus_loc).click()

    # 点击第一列创建问题
    def click_first_goods_great_question(self):
        return self.find_element(*self.first_goods_great_question_loc).click()

    # 点击第二列加号
    def click_second_plus(self):
        return self.find_element(*self.second_plus_loc).click()

    # 点击第二列创建问题
    def click_second_great_question(self):
        return self.find_element(*self.second_goods_great_question_loc).click()

    # 文本，第一列物资创建问题的标题
    def text_first_goods_question_title(self):
        return self.find_element(*self.first_goods_question_title_loc).text

    # 点击第一个问题的解决问题
    def click_first_question_solve(self):
        return self.find_element(*self.first_question_solve_loc).click()

    # 点击现场指挥部添加审批人员
    def click_xianchang_zhihuibu_shenpi(self):
        return self.find_element(*self.xianchang_zhihuibu_shenpi_loc).click()

    # 添加备注信息
    def send_remark(self):
        return self.find_element(*self.remark_loc).send_keys('自动化测试备注')

    # 点击提交
    def click_primary(self):
        return self.find_element(*self.primary_loc).click()

    # 点击确定
    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    # 文本，发货单状态
    def text_plan_status(self):
        return self.find_element(*self.plan_status_loc).text






__author__ = '38720'
# coding=utf-8
from base_page.base import Page
from selenium.webdriver.common.by import By



class PlanThird(Page):

    '''联采比较价-第三页'''

    # 文本，进度
    text_point_loc = (By.CSS_SELECTOR, '#label_preview > p')
    # 筛选区-合同编号选择
    select_contract_number_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm_step4 > div > div:nth-child(1) > div > select')
    # 筛选区-标段选择
    select_biaoduan_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm_step4 > div > div:nth-child(2) > div > select')
    # 筛选区-物资选择
    select_goods_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm_step4 > div > div:nth-child(3) > div > select')
    # 筛选区-规格型号
    input_type_model_loc = (By.CSS_SELECTOR, '#dispatchBillParamsForm_step4 > div > div:nth-child(4) > div > input')
    # 搜索按钮
    button_search_loc = (By.XPATH, '//*[@id="dispatchBillParamsForm_step4"]/div/div[5]/div/button[1]')

    # 文本，第一列合同编号
    text_first_contract_number_loc = (By.CSS_SELECTOR, '#importGoodsPriceInformationTable_step4 > tbody > tr > td:nth-child(1)')
    # 文本，第一列标段
    text_first_biaoduan_loc = (By.CSS_SELECTOR, '#importGoodsPriceInformationTable_step4 > tbody > tr > td:nth-child(2)')
    # 文本，第一列物资
    text_first_goods_loc = (By.CSS_SELECTOR, '#importGoodsPriceInformationTable_step4 > tbody > tr > td:nth-child(3)')
    # 文本，第一列规格型号
    text_first_type_model_loc = (By.CSS_SELECTOR, '#importGoodsPriceInformationTable_step4 > tbody > tr > td:nth-child(4)')

    # 保存并发布
    button_next_loc = (By.CSS_SELECTOR, '#section_preview > div.box-footer.text-center > a:nth-child(2)')
    # 点击确认
    button_submit_loc = (By.CSS_SELECTOR, '#popup_ok')

    # 文本，进度
    def text_point(self):
        return self.find_element(*self.text_point_loc).text

    # 选择合同编号
    def select_contract_number(self):
        self.select_by_text(self.find_element(*self.select_contract_number_loc), '15.38(15.38)')
        return self

    # 选择标段
    def select_biaoduan(self):
        self.select_by_text(self.find_element(*self.select_biaoduan_loc), 'MHTJ-23标一工区')
        return self

    # 选择物资
    def select_goods(self):
        self.select_by_text(self.find_element(*self.select_goods_loc), '光圆(HPB300)')
        return self

    # 输入规格型号
    def send_type_model(self):
        self.find_element(*self.input_type_model_loc).send_keys('10')
        return self

    # 点击，搜索
    def click_search(self):
        self.find_element(*self.button_search_loc).click()
        return self

    # 点击，保存并发布
    def click_next(self):
        self.find_element(*self.button_next_loc).click()
        return self

    # 文本，第一列合同编号
    def text_first_contract_number(self):
        return self.find_element(*self.text_first_contract_number_loc).text

    # 文本，第一列标段
    def text_first_biaoduan(self):
        return self.find_element(*self.text_first_biaoduan_loc).text

    # 文本，第一列物资
    def text_first_goods(self):
        return self.find_element(*self.text_first_goods_loc).text

    # 文本，第一列规格型号
    def text_first_type_model(self):
        return self.find_element(*self.text_first_type_model_loc).text

    # 点击确认
    def click_submit(self):
        self.find_element(*self.button_submit_loc).click()
        return self





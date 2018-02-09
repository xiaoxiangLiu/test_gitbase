__author__ = '38720'
# coding=utf-8


from NewFramework.BasePage import Page



class BaiDuTest(Page):

    input_user_css = Page().visibility_by_element(css='#userid')
    input_password_css = Page().visibility_by_element(css='#loginForm > div.box-body.form-horizontal > div > div.col-xs-10 > div:nth-child(2) > input')
    button_login_css = Page().visibility_by_element(css='#logintSubBut')
    button_myoffice_link = Page().visibility_by_element(link_text='我的办公室')


    def login(self):
        self.send_element(assert_word=self.input_user_css, text='13843502630')
        self.send_element(assert_word=self.input_password_css, text='123456')
        self.click_element(self.button_login_css)
        return True



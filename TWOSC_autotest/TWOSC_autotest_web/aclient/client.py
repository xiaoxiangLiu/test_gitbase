__author__ = '38720'
# coding=utf-8

import requests



METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):

    '''当传入的参数不支持时抛出此异常'''

    pass


class HTTPClient(object):

    '''http请求的client,接受url, method等参数'''

    pass



    def __init__(self, url, method='GET', headers=None, cookies=None):

        '''四个参数，url网址，method默认GET，head默认无，cookie默认无'''

        self.url = url
        self.method = method.upper()
        self.session = requests.session()
        if self.method not in METHODS:
            raise UnSupportMethodException('not support method : %s'%self.method)


    def set_heads(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)


    def send(self, params=None, data=None, **kwargs):

        respones = self.session.request(self.method, self.url, params, data, **kwargs)
        respones.encoding = 'utf-8'
        return respones






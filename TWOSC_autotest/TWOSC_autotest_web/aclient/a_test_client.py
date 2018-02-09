__author__ = '38720'
# coding=utf-8
import unittest
from aclient.client import HTTPClient



class baiDu(unittest.TestCase):

    '''测试接口测试基础类'''

    url = 'http://menghua_test.dev.sjgtw.net:48097/'

    def setUp(self):

        self.client = HTTPClient(url=self.url, method='GET')

    def test_one(self):
        res = self.client.send()
        self.assertEqual(res.text, '蒙华铁路')

if __name__ == '__main__':
    unittest.main()


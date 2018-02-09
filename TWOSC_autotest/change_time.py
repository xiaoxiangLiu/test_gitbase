__author__ = '38720'
# coding=utf-8

import time
import requests
from bs4 import BeautifulSoup
import pymysql



class ChangeTime(object):

    '''修改合同中的到货初验时间'''

    def __init__(self, chang_time, id):
        self.time = chang_time
        self.id = id

    def ChangSolrTime(self):

        '''把时间转换成时间戳，并get到solr服务器'''

        solr_url = 'http://192.168.1.254:48080/solr/index.html#/DispatchBillVO/documents'
        time_1 = int(time.mktime(time.strptime(self.time, '%Y-%m-%d %H:%M:%S')))
        send_time = int(time_1)+000
        print(send_time)
        json = {
            'id': self.id,
            'earlyAcceptFinishTime': {
                'set': send_time
            }
        }
        respones = requests.get(solr_url, json)
        print(respones.status_code)
        assert_solr_url = 'http://192.168.1.254:48080/solr/DispatchBillVO/select?q=id:'+self.id
        assert_word = requests.get(assert_solr_url)
        soup = BeautifulSoup(assert_word.text, 'html.parser')
        longs = soup.find_all('long')
        for i in longs:
            print(i.string)
        if longs[5].string == send_time:
            print('改好了')
        else:
            print('没改好')
        return True






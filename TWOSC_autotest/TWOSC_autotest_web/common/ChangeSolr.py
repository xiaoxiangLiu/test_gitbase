__author__ = '38720'
# coding=utf-8

from selenium import webdriver
import time
import json


class ChangeSolr(object):

    def __init__(self, ChangeTime, ContractId):

        self.ChangeTime = str(ChangeTime)
        self.ContractId = str(ContractId)

    def ChangeSolrTime(self):

        ChangeTime = int(time.mktime(time.strptime(self.ChangeTime, '%Y-%m-%d %H:%M:%S')))*1000
        print(ChangeTime)
        print(self.ContractId)
        solr_json = {
            'id': self.ContractId,
            'earlyAcceptFinishTime': {
                'set': ChangeTime,
            }
        }
        solr_json = json.dumps(solr_json)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('http://192.168.1.254:48080/solr/index.html#/DispatchBillVO/documents')
        driver.find_element_by_css_selector('#document').send_keys(solr_json)
        driver.find_element_by_css_selector('#submit').click()
        time.sleep(2)
        assert_url = 'http://192.168.1.254:48080/solr/DispatchBillVO/select?q=id:'+str(self.ContractId)
        driver.get(assert_url)
        time.sleep(1)
        text = driver.find_element_by_css_selector('#collapsible4 > div.expanded > div.collapsible-content > div:nth-child(13) > span.text').text
        print(text)
        if int(text) == ChangeTime:
            print('改好了')
        else:
            print('没改好')
        driver.quit()

if __name__ == '__main__':
    test = ChangeSolr('2017-12-3 1:1:1', '96133705953000')
    test.ChangeSolrTime()


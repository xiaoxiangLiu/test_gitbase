__author__ = '38720'
# coding=utf-8
import pysolr
import requests


response= requests.get('http://192.168.1.254:48080/solr/DemandSupplyPlanVO/select?q=id:96827471576000')
print(type(response))
print(response.text)
print(response.status_code)
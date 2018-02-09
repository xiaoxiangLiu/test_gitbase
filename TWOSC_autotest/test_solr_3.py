__author__ = '38720'
# coding=utf-8
import json
import requests


r = requests.get('http://192.168.1.254:48080/solr/admin/cores?_=1518167698143&indexInfo=false&wt=json')
print(type(r))
print(r.status_code)
print(r.text)

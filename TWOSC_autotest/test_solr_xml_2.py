__author__ = '38720'
# coding=utf-8
import requests
import json


xml = '<add>' \
      '<doc commitWithin="1" overwrite=true boost=1>' \
      '<field name="id">97517790921000</field>' \
      '<field name="earlyAcceptFinishTime" update="set">1517508122000</field>' \
      '</doc>' \
      '<commit></commit>' \
      '</add>'
print(type(xml))
print(xml)
params = {"boost": 1.0, "overwrite": "true", "commitWithin": 1}
headers = {"Content-Type": "application/xml"}
url = 'http://192.168.1.254:48080/solr/index.html/DispatchBillVO/documents/update/?wt=json'
r = requests.post(url, data=xml, headers=headers)
print(r.status_code)
print(r.text)


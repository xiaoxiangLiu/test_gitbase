__author__ = '38720'
# coding=utf-8

import requests

# 传参 字典
payload = {
    'key':'value',
    'key2':'value',
}
r = requests.get('http://httpbin.org/get', params=payload)

# 返回url
print(r.url)
# 返回二进制结果
print(r.content)
# 返回json格式
print(r.json())
# 返回状态码
print(r.status_code)
# 返回文本
print(r.text)
r_read = requests.get('https://api.github.com/events', stream=True)
print(r_read.raw.read())
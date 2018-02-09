__author__ = '38720'
# coding=utf-8


tuple = ("early_accept_finish_time = '2017-12-01'", "id = '123456789'")
blank = " "
list_1 = list(tuple)
# print(len(list_1))
list_blank = []
for row in list_1:
    list_blank.append(blank + row + blank)
str_word = ','.join(list_blank)
print(str_word)
'''

tuple = ("id = '123456'","create_time = '2018-02-10 1:01:01")
print(type(tuple))
print(type(str(tuple)))
print(str(tuple))
str = str(tuple)
print(str[1:-2])
'''
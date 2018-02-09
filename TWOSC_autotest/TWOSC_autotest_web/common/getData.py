__author__ = '38720'
# coding=utf-8

import xlrd

class NotFoundExcel(object):
    '''找不到excel的异常'''
    pass

PLAYER_FILE = 'user.xlsx'
DATA_FILE = 'data.xlsx'

class GetExcel(object):

    def __init__(self, filename='/TWOSC_autotest/TWOSC_autotest_web/data/'+PLAYER_FILE, sheetname=None, col=None, row=None):

        self._filename = filename
        self._col = col
        self._row = row
        self._sheet = sheetname

    def GetDataByInt(self):

        workbook = xlrd.open_workbook(filename=self._filename)
        sheet = workbook.sheet_by_name(self._sheet)
        value = sheet.cell_value(self._row, self._col)
        return int(value)

    def GetDataByStr(self):
        workbook = xlrd.open_workbook(filename=self._filename)
        sheet = workbook.sheet_by_name(self._sheet)
        value = sheet.cell_value(self._row, self._col)
        return str(value)

if __name__ == '__main__':

    excel = GetExcel(sheetname='user', col=0, row=3)
    # data_int = excel.GetDataByInt()
    # print(type(data_int), data_int)
    data_str = excel.GetDataByStr()
    print(type(data_str), data_str)


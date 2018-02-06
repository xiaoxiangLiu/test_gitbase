__author__ = '38720'
# coding=utf-8
import pymysql

UPDATE = "UPDATE"
SET = "SET"
WHERE = "WHERE"
INSERT = "INSERT"
DATABASE = 'wuzi_test'
HOST = '192.168.1.211'
PORT = 3310
USER = 'wuzi'
PASSWORD = 'w123456'
BLANK = " "

class ChangeMysql(object):

    def __init__(self, sqlTable, sqlId, *sqlRows):

        self._sqlTable = BLANK + sqlTable + BLANK
        self._sqlId = BLANK + sqlId + BLANK
        if len(sqlRows) <= 1:
            str_sqlRows = str(sqlRows)
            self._sqlRows = BLANK + str_sqlRows[2:-3] + BLANK
        else:
            list_blank = []
            for row in list(sqlRows):
                list_blank.append(BLANK + row + BLANK)
            rows_word = ','.join(list_blank)
            self._sqlRows = rows_word
        print(self._sqlRows)
        # 链接数据库
        self.connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            db=DATABASE,
        )

    def ChangeMysqlByUpdate(self):

        # 拼接mysql语句
        self._sqlWord_by_update = UPDATE + self._sqlTable + SET + self._sqlRows + WHERE + self._sqlId
        print(self._sqlWord_by_update)
        # 获取游标及执行
        self.cur = self.connection.cursor()
        self.cur.execute(self._sqlWord_by_update)
        self.connection.commit()
        self.cur.close()
        self.connection.close()

    def ChangeMysqlByInsert(self):

        self._sqlWord_by_insert = INSERT

if __name__ == '__main__':

    test = ChangeMysql("gt_dispatch_bill", "id='97519179571000'", "early_accept_finish_time = '2017-12-10 1:01:01'", \
                       "create_time = '2018-02-03 1:01:01'")
    test.ChangeMysqlByUpdate()

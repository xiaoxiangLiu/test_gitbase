# coding=utf-8
from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, unittest, time, os



#   定义发送邮件
def send_mail(file_new):
    address = ('38720034@qq.com')
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP_SSL()
    smtp.connect('smtp.qq.com')
    smtp.login('38720034@qq.com', 'ozbeabsssxkzbiei')
    smtp.sendmail('38720034@qq.com', address,  msg.as_string())
    smtp.close()
    print('email has send out!')

#   查找测试报告目录，找到最新的测试报告文件

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '//' +fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='智慧供应链自动化测试',  description='环境：win10 浏览器：chrome')
    discover = unittest.defaultTestLoader.discover('./testCase/', pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./report/')
    #  send_mail(file_path)


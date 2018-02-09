__author__ = '38720'
# coding=utf-8

import logging





logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logfile = 'logger.txt'
handler = logging.FileHandler(logfile, mode='w', encoding='utf8')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is error')
logging.critical('this is critical')



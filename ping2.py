#coding=utf-8
import os
import sys
import ctypes
import datetime
import logging
import subprocess
import signal
import urllib.request

def getname():
    pcName = ctypes.c_char_p(''.encode('utf-8'))
    pcSize = 16
    pcName = ctypes.cast(pcName, ctypes.c_char_p)
    try:
        ctypes.windll.kernel32.GetComputerNameA(pcName, ctypes.byref(ctypes.c_int(pcSize)))
    except Exception:
        print("Sth wrong in getname!")
    return pcName.value.decode('utf-8')

if __name__ == '__main__':

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with urllib.request.urlopen('http://www.lanhi.com.cn/getip/getip.php?data=data') as response:
            html = response.read().decode('utf-8')
            logging.basicConfig(level=logging.INFO, filename='./log.log')
            logging.info( nowTime + "---" + html)
    except :
        logging.info(nowTime+"错误---")




'''iplist = list()
ip = 'oa.lanhaijx.com'
tep = []
send = False

while True:
    backinfo = os.system('ping -n 2 %s' % ip)
    print(backinfo)
    time.sleep(5)
'''


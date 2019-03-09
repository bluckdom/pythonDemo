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
    try:
        pcname =getname()
        path = os.path.split(os.path.realpath(__file__))[0]+"\ping2.exe"
        st = subprocess.STARTUPINFO
        st.dwFlags = subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow = subprocess.SW_HIDE
        print(path)
        #最小化执行DOS
        #HOURLY
        #minute
        #subprocess.Popen("chcp 437", shell=True)
        cmd = "schtasks /create /tn \"updateip\" /tr "+path+" /sc HOURLY  /mo 2"
        #cmd = "schtasks /query"
        updateip = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,startupinfo=st)
        output = updateip.communicate(input="N".encode())


    except :
        print("错误---")
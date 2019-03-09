#coding=utf-8

import re
import urllib.request
import urllib.parse
import ssl
from multiprocessing import Process
import wx
import io
import json
import http.cookiejar
import requests
import datetime
import os
import time
import win32api
import threading
from threading import Thread

download_path = os.getcwd() + "\download"

class TestThread(Thread):
    def __init__(self,gethttp,btn):
        self.tsurl = gethttp.tsurl
        self.echo = gethttp.echo
        self.btn = btn
        self.filename = gethttp.filename.Value + ".ts"
        Thread.__init__(self)
        self.start()

    def del_file(self,path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.del_file(c_path)
            else:
                os.remove(c_path)
    def run(self):
        if os.path.exists(download_path):
            self.del_file(download_path)
        self.echo("共有" + str(len(self.tsurl)) + "个片段\n正在下载中，请稍候....\n")
        for url in self.tsurl:
            res = requests.get(url, timeout=500)
            with open(download_path + "\\" + url.split("/")[-1], 'ab') as f:
                self.echo(url.split("/")[-1] + "-下载完成")
                f.write(res.content)
                f.flush()
        self.echo("片段全部下载完成,正在拼接视频文件....")

        filename = self.filename
        if os.path.exists(filename):
            os.remove(filename)
        for url in self.tsurl:
            with open(filename, 'ab') as f:
                fileadd = download_path + "\\" + url.split("/")[-1]
                file = open(fileadd, 'rb')
                f.write(file.read())
                file.close()
                f.flush()
        self.echo("视频处理完成,名称：" + filename)
            #wx.CallAfter(self.postTime, i)'''
        self.btn.Enable()
class GETHTTP(wx.Frame):
    def __init__(self, parent, title):
        super(GETHTTP, self).__init__(parent, title=title, size=(600, 600),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)
        #self.SetMaxClientSize((600,600))
        vbox = wx.BoxSizer(wx.VERTICAL)
        exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        self.icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)

        self.SetIcon(self.icon)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.l1 = wx.StaticText(panel, -1, "微吼ID(视频播放页URL最后一串数字)：")
        hbox1.Add(self.l1,wx.ALIGN_CENTER| wx.ALL , 5)

        self.t1 = wx.TextCtrl(panel, value="558760645")#349644211,259006896
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.passtxt = wx.StaticText(panel, -1, "播放密码：")
        hbox1.Add(self.passtxt,wx.ALIGN_CENTER| wx.ALL , 5)

        self.passwd = wx.TextCtrl(panel,value = "weaver2018")
        hbox1.Add(self.passwd,1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL,5 )

        self.button = wx.Button(panel, -1, "确定")
        hbox1.Add(self.button,  1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.button.Bind(wx.EVT_BUTTON, self.Onbind)
        vbox.Add(hbox1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.filenamestaic = wx.StaticText(panel, -1, "文件保存名：")
        hbox2.Add(self.filenamestaic, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.filename = wx.TextCtrl(panel)
        hbox2.Add(self.filename, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.resultTc = wx.TextCtrl(panel,size = (600,600),style= wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        hbox3.Add(self.resultTc, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        vbox.Add(hbox3)


        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()
    def Onbind(self,event):
        if(self.filename.Value == ""):
            self.echo("请输入文件名称")
            return ""

        btn = event.GetEventObject()
        label = btn.GetLabel()
        btn.Disable()
        id = self.t1.Value

        try:
            html = self.getHtml("http://live.vhall.com/"+id)
            index = html.find("'streamname':'")
            streamname = ""
            if index == -1:
                result = self.getLogin(id)
                if result == "0" :
                    return
                else:
                    streamname = self.getSteanme(result)
            else:
                streamname = self.getSteanme(html)
            self.echo("地址流获取成功："+streamname+"\n")
            self.tsurl = self.GetTsUrl(streamname)

            TestThread(self, btn)

        except IOError:
            self.echo("出现错误，已终止")

    def getSteanme(self,str):
        start = str.rfind("'streamname':'")
        end = str.rfind("msg_url")
        str = str[start:end]
        str = str[str.find("//"):str.rfind("m3u8")]
        return "http:" + str + "m3u8"
    def getHtml (self,url):
        html = urllib.request.urlopen(url).read()
        html = html.decode("utf-8")
        return html
    def echo(self,str):
        self.resultTc.AppendText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S-') + str + "\n")
    def getLogin(self,id):
        domain = "http://live.vhall.com/"
        joinbypass = domain + "webinar/joinbypass"
        headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000",
            'Referer' : "http://live.vhall.com/"+id,
            'Content-Type' : "application/x-www-form-urlencoded; charset=UTF-8"
        }
        values = {
            "webinar_id" : id,
            "password" : self.passwd.Value
        }

        session = requests.Session()
        resp = session.post(joinbypass, data=values, headers = headers).content.decode("utf-8")
        obj = json.loads(resp)
        code = obj['code']
        if code == "1005":
            self.echo("密码错误")
        elif code == "1010":
            url = domain + id
            html = session.get(url).content.decode("utf-8")
            return html
        else:
            self.echo("程序错误")
        return "0"
    def GetTsUrl(self,url):
        tsurl = []
        filename = self.filename.Value + ".ts"
        try:
            os.remove(download_path+"/"+filename)
        except:
            pass
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        all_content = requests.get(url).text  # 获取M3U8的文件内容
        file_line = all_content.split("\n")  # 读取文件里的每一行
        # 通过判断文件头来确定是否是M3U8文件
        if file_line[0] != "#EXTM3U":
            raise BaseException("非M3U8的链接")
        else:
            unknow = True  # 用来判断是否找到了下载的地址
            length = str(int((len(file_line)-6)/2))
            for index, line in enumerate(file_line):
                if "EXTINF" in line:
                    unknow = False
                    # 拼出ts片段的URL
                    domain = url.rsplit("/", 1)[0]
                    domain = domain[0:domain.rfind("//")]
                    if(file_line[index + 1].find("/") == 0):
                        pd_url = domain + file_line[index + 1]
                    else:
                        pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]

                    #c_fule_name = str(file_line[index + 1]).split("/")[-1]
                    tsurl.append(pd_url)
                    # self.dowTs(pd_url, c_fule_name, filename, length)

            if unknow:
                raise BaseException("未找到对应的下载链接")
            else:
                return tsurl


app = wx.App()
GETHTTP(None, "微吼播放地址查询器    Powered by:www.xjjsz.com")
app.MainLoop()
#coding = utf-8
import urllib.request
from bs4 import BeautifulSoup
import requests
import os
import time
import wx
from threading import Thread
from wx.lib.pubsub import pub
import datetime


class WxFrame(wx.Frame):
    def __init__(self,parent=None,title="图片获取器"):
        super(WxFrame,self).__init__(parent, title = title,  style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.s1 = wx.StaticText(panel, -1,  "网址:")
        hbox.Add(self.s1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL , 5)

        self.tc1 = wx.TextCtrl(panel,size=(280,30),value = "http://www.lanhi.com.cn")
        hbox.Add(self.tc1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.bt1 = wx.Button(panel, -1, "获取")
        hbox.Add(self.bt1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.bt1.Bind(wx.EVT_BUTTON, self.OnClick)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.gu = wx.Gauge(panel,-1, 100, (100,20),(385,23))
        hbox2.Add(self.gu)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.consoleBox = wx.TextCtrl(panel,size = (385, 200), style= wx.TE_MULTILINE | wx.CB_READONLY)
        self.consoleBox.SetBackgroundColour(panel.BackgroundColour)
        hbox3.Add(self.consoleBox)

        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(hbox)
        vBox.Add(hbox2)
        vBox.Add(hbox3)

        panel.SetSizer(vBox)
        self.Center()
        self.Show()
        self.Fit()
        pub.subscribe(self.updateGauge, "update")
        pub.subscribe(self.echo, "echo")
    def updateGauge(self, msg):
        t = msg
        if isinstance(t, int):  # 如果是数字，说明线程正在执行，显示数字
            self.gu.SetValue(t)

        else:  # 否则线程未执行，将按钮重新开启
            self.btn.Enable()
    def OnClick(self,event):
        self.btn = event.GetEventObject()
        self.btn.Disable()
        beauty = BeautifulPicture(self.tc1.Value)
        #btn.Enable()
    def echo(self,str):
        s = str
        self.consoleBox.AppendText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S-') + s + "\n")
class BeautifulPicture(Thread, WxFrame):
    def __init__(self, url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.url = url
        self.folder_path = os.getcwd() + "\BeautifulPicture"
        Thread.__init__(self)
        self.start()

    def run(self):
        print("解析成功")
        r = self.request(self.url)
        print("开始获取img标签")
        all_img = BeautifulSoup(r.text, "html.parser").find_all('img')
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        img_len = len(all_img)
        for i in range(img_len):
            src = all_img[i]['src']
            msg = int(((i + 1) / img_len) * 100)
            if i == img_len - 1:
                msg = 100
            wx.CallAfter(pub.sendMessage, "update", msg=msg)
            self.save_img(src)
        os.chdir("..")

    def request(self, url):
        r = requests.get(url)
        return r

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
    def save_img(self, url):
        url = self.url + "/" + url
        filename = url.split("/")[-1]
        img = self.request(url)
        f = open(filename, 'ab')
        f.write(img.content)
        f.close()
        print(filename + "下载完成")

app = wx.App()
WxFrame()
app.MainLoop()
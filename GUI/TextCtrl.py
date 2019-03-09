#coding = utf-8

import wx

class TextCtrl(wx.Frame):
    def __init__(self, parent, title):
        super(TextCtrl, self).__init__(parent, title = title, size = (600, 600))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(panel, -1, "文本域")

        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.TextCtrl(panel)
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        vbox.Add(hbox1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "密码文本框")
        self.t2 = wx.TextCtrl(panel, style = wx.TE_PASSWORD)
        self.t2.Bind(wx.EVT_TEXT_MAXLEN, self.OnMaxLen)
        self.t2.SetMaxLength(5)
        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(panel, -1, "只读文本")
        self.l3 = wx.TextCtrl(panel, value="默认初始值",style=wx.TE_READONLY)
        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)
        hbox3.Add(self.l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)

        panel.SetSizer(vbox)
        self.Center()
        self.Show()
        self.Fit()
    def OnKeyTyped(self,event):
        print(event)

    def OnMaxLen(self, event):
            print(event)
app = wx.App()
TextCtrl(None, "TextCtrl 实例")
app.MainLoop()


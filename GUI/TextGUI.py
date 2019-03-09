import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(600, 600))
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, -1, style=wx.ALIGN_CENTER)
        txt1 = "Python GUI development"
        txt2 = "using wxPython"
        txt3 = "Python port of wxWidget "
        txt = txt1 + "\n" + txt2 + "\n" + txt3

        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        lbl.SetFont(font)
        lbl.SetLabel(txt)
        box.Add(lbl, 0, wx.ALIGN_CENTER)

        lblwrap = wx.StaticText(panel, -1, style=wx.ALIGN_RIGHT)
        txt = txt1 + txt2 + txt3
        lblwrap.SetLabel(txt)
        lblwrap.Wrap(200)
        box.Add(lblwrap, 0, wx.ALIGN_LEFT)

        lbl1 = wx.StaticText(panel, -1, style=wx.ALIGN_RIGHT )
        lbl1.SetLabel("这是新增加的LABEL")
        font1 = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        lbl1.SetFont(font1)
        lbl1.SetForegroundColour((255, 0, 0))
        lbl1.SetBackgroundColour((0, 0, 0))
        box.Add(lbl1, 0, wx.ALIGN_LEFT)

        txtctrl = wx.TextCtrl(panel, -1,"默认初始值", size = (400,100), style = wx.TE_MULTILINE)
        box.Add(txtctrl, 0, wx.ALIGN_CENTER)



        panel.SetSizer(box)
        self.Centre()
        self.Show()

app = wx.App()
Mywin(None, 'StaticText demo')
app.MainLoop()
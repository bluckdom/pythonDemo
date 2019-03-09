#conding = utf-8
import wx
class RadioButton(wx.Frame):
    def __init__(self, parent, title):
        super(RadioButton, self).__init__(parent, title= title, size = (500,500))
        self.InitUI()
    def InitUI(self):
        pnl = wx.Panel(self)

        self.rb1 = wx.RadioButton(pnl, 11, label = "数值1", pos = (10, 10), style = wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, 22, label = "数值2", pos = (10, 40))
        self.rb3 = wx.RadioButton(pnl, 33, label = "数值3", pos = (10, 70))
        self.Bind(wx.EVT_RADIOBUTTON, self. OnRadiogroup)

        lblList = ['参1', '参2','参3']
        self.rbox = wx.RadioButton(pnl, label = 'RadioBox', pos = (80,10), choices  = lblList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.OnRadioBox)
        self.Center()
        self.Show()
    def OnRadioBox(self, e):
        print(self.rbox.GetStringSelection(),'is clicked from radio box')
    def OnRadiogroup(self, e):
        rb = e.GetEventObject()
        print(rb.GetLabel(),' is click from radion group')
ex = wx.App()
RadioButton(None, "Radio")
ex.MainLoop()
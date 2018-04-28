#-*-coding:utf-8-*-
__author__ = 'Administrator'
#!/usr/bin/env python

import wx


class Frame(wx.Frame):   #2 wx.Frame子类
    """Frame class that displays an image."""

    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='Hello, wxPython!'): #3图像参数
        """Create a Frame instance and display image."""
#4 显示图像
        temp = image.ConvertToBitmap()
        size = temp.GetWidth()+10, temp.GetHeight()+100
        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self,-1)
        wx.StaticText(panel,-1,"像素坐标:",pos=(size[0]/2-60,0),size=(60,20))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(size[0]/2,0),size=(60,20))
        self.bmp = wx.StaticBitmap(parent=panel, bitmap=temp,pos=(0,50) )
        self.bmp.Bind(wx.EVT_MOTION,self.OnMove)

    def OnMove(self,event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("(%s,%s)" % (pos.x,pos.y))

class App(wx.App):  #5 wx.App子类
    """Application class."""

    def OnInit(self):
#6 图像处理
        image = wx.Image('back.jpg', wx.BITMAP_TYPE_JPEG)

        self.frame = Frame(image)

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():  #7
    app = App()
    app.MainLoop()

if __name__ == '__main__':
     main()
import wx

class Main(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))
        # Caixa de texto
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        # Carrega o fonte na caixa de texto
        self.control.SetLabel(file('wx01.py', 'rb').read())
        # Mostra a janela
        self.Show(True)


app = wx.App()
frame = Main(None, wx.ID_ANY, 'Fonte')
app.MainLoop()
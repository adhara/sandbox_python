#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class Main(wx.Frame):
    def __init__(self, parent, id, title):
        # Cria janela
        wx.Frame.__init__(self, parent, id, title, size=(300, 150))
        self.Centre()
        self.Show(True)
        # Cria um texto est�tico
        self.text = wx.StaticText(self, pos=(10, 10), label='Entre com uma express�o:')
        # Cria uma caixa de edi��o de texto
        self.edit = wx.TextCtrl(self, size=(250, -1), pos=(10, 30))
        # Cria um bot�o
        self.button = wx.Button(self, label='ok', pos=(10, 60))
        # Conecta um m�todo ao bot�o
        self.button.Bind(wx.EVT_BUTTON, self.on_button)

    def on_button(self, event):
        # Pega o valor da caixa de texto
        txt = self.edit.GetValue()
        try:
            wx.MessageBox(txt + ' = ' + str(eval(txt)), 'Resultado')
        except:
            wx.MessageBox('Express�o inv�lida', 'Erro...')


app = wx.App()
Main(None, wx.ID_ANY, 'Teste de MessageBox')
app.MainLoop()
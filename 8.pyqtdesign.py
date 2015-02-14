#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt4 import QtCore, QtGui
from dialog import Ui_Dialog

class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect(self.ui.msg, QtCore.SIGNAL('clicked()'), self.show_msg)
    
    def show_msg(self):
        reply = QtGui.QMessageBox.question(self, 'Messagem', 'Hora: ' + time.asctime().split()[3], QtGui.QMessageBox.Ok)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
 
 
class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("2nd PyQt.ui", self)
        self.ui.show()
 
    @pyqtSlot()
    def button_01(self):
        self.ui.label.setText("첫번째 버튼")
 
    @pyqtSlot()
    def button_02(self):
        self.ui.label.setText("두번째 버튼")
 
    @pyqtSlot()
    def button_03(self):
        self.ui.label.setText("세번째 버튼")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())

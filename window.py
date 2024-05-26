import json
import os
import sys
import subprocess

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
from qt_material import apply_stylesheet

from main_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        pass

def buildApp():
    app = QApplication(sys.argv)
    win = Window()
    apply_stylesheet(app, theme='dark_blue.xml')
    win.show()
    sys.exit(app.exec())

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from mexui.edit_command_ui import Ui_Dialog

import mex_functions
from mex_functions import loadConfig

class Window(QDialog, Ui_Dialog):
    def __init__(self, command=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.config = mex_functions.loadConfig()
        if command:
            self.command = command
            self.insertValues()

    def insertValues(self):
        self.commandNameEdit.setText(self.command)
        self.comboBox.setCurrentIndex(2)
        section = self.config[self.command]
        if section["type"] == ("terminal"):
            self.comboBox.setCurrentIndex(1)
        else:
            self.comboBox.setCurrentIndex(2)
        self.plainTextEdit.setPlainText(section["command"])

    def connectSignalsSlots(self):
        self.saveButton.pressed.connect(self.saveCommand)

    def saveCommand(self):
        print("save")
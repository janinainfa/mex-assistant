from PyQt5.QtWidgets import QDialog, QMessageBox
from mexui.edit_command_ui import Ui_Dialog
import os
from mex_functions import loadConfig, openDialog

class Window(QDialog, Ui_Dialog):
    def __init__(self, command=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.config = loadConfig()
        if command:
            self.command = command
            self.insertValues()
        else:
            self.command = None

    def insertValues(self):
        self.commandNameEdit.setText(self.command)
        self.commandTypeBox.setCurrentIndex(2)
        section = self.config[self.command]
        if section["type"] == ("terminal"):
            self.commandTypeBox.setCurrentIndex(1)
        else:
            self.commandTypeBox.setCurrentIndex(2)
        self.commandEdit.setPlainText(section["command"])

    def connectSignalsSlots(self):
        self.saveButton.pressed.connect(self.saveCommand)

    def saveCommand(self):
        commandType = self.commandTypeBox.currentText()
        commandName = self.commandNameEdit.text()
        if self.checkValues(commandType, commandName):
            if self.command:
                self.config.remove_section(self.command)
            commandContents = {'type': self.commandTypeBox.currentText().lower(),
                                'command': self.commandEdit.toPlainText()}
            self.config[commandName] = commandContents
            with open(os.path.expanduser("~") + "/mexassistant/config.ini", "w") as f:
                self.config.write(f)
            self.reject()

    def checkValues(self, commandType, commandName):
        if commandName.rstrip() == "":
            openDialog("Nazwa komendy nie może być pusta", "information")
            return False
        if commandType == "Wybierz...":
            openDialog("Najpierw wybierz rodzaj komendy", "information")
            return False
        if (commandName in self.config.sections()) and (not commandName == self.command):
            dialogResult = openDialog("Taka komenda już istnieje. Czy chcesz ją zamienić?", "confirmation")
            return dialogResult == QMessageBox.Yes
        return True
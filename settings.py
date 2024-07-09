import subprocess

from PyQt5 import QtWidgets, sip
from PyQt5.QtWidgets import QDialog, QMessageBox
from mexui.settings_ui import Ui_Settings

import edit_command
from mex_functions import loadConfig, openDialog

class Window(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.config = loadConfig()
        self.createCommandLabelsAndButtons()
        self.setupComboBox()


    def setupComboBox(self):
        lang = self.config["DEFAULT"]["voice_lang"]
        if lang == "pl-PL":
            self.comboBox.setCurrentIndex(1)
        self.comboBox.activated.connect(self.changeLanguage)

    def changeLanguage(self):
        self.config["DEFAULT"]["voice_lang"] = self.comboBox.currentText()
        with open("/etc/mexassistant/config.ini", "w") as f:
            self.config.write(f)

    def createCommandLabelsAndButtons(self):
        self.commandsLayout = QtWidgets.QGridLayout()
        self.commandsLayout.setObjectName("commandsLayout")
        sections = self.config.sections()
        for row, i in enumerate(sections):
            label = QtWidgets.QLabel(self)
            label.setText(i.capitalize())
            label.setProperty("class", "command_label")
            self.commandsLayout.addWidget(label, row + 2, 0)
            self.createCommandButton("edit", "Edytuj", i, row + 2, 1)
            self.createCommandButton("delete", "Usuń", i, row + 2, 2)


        self.newCommandButton = QtWidgets.QPushButton(self)
        self.newCommandButton.setText("Dodaj nową komendę")
        self.newCommandButton.pressed.connect(lambda: self.buttonClicked("edit"))
        self.commandsLayout.addWidget(self.newCommandButton, len(sections) + 2, 0, 1, 3)
        self.openConfigFileButton = QtWidgets.QPushButton(self)
        self.openConfigFileButton.setText("Otwórz plik konfiguracyjny")
        self.openConfigFileButton.pressed.connect(lambda: subprocess.Popen(["xed", "/etc/mexassistant/config.ini"]))
        self.commandsLayout.addWidget(self.openConfigFileButton, len(sections) + 3, 0, 1, 3)

        self.gridLayout.addLayout(self.commandsLayout, 2, 0, 1, 3)

    def buttonClicked(self, action, button=None):
        if action == "edit":
            if button:
                editCommandDialog = edit_command.Window(button.property("command"))
            else:
                editCommandDialog = edit_command.Window()
            editCommandDialog.exec()
            self.refreshCommands()
        elif action == "delete":
            command = button.property("command")
            self.deleteCommand(command)

    def createCommandButton(self, action, actionName, command, row, column):
        button = QtWidgets.QPushButton(self)
        button.setText(actionName)
        button.setProperty("class", "command_button")
        button.setProperty("command", command)
        button.pressed.connect(lambda button=button: self.buttonClicked(action, button))
        self.commandsLayout.addWidget(button, row, column)

    def deleteCommand(self, command):
        dialogResult = openDialog("Na pewno? Tej czynności nie będzie można cofnąć.", "confirmation")
        if dialogResult == QMessageBox.Yes:
            self.config.remove_section(command)
            with open("/etc/mexassistant/config.ini", "w") as f:
                self.config.write(f)
            self.refreshCommands()

    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)

    def refreshCommands(self):
        self.config = loadConfig()
        self.deleteLayout(self.commandsLayout)
        self.createCommandLabelsAndButtons()
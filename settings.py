from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from mexui.settings_ui import Ui_Settings

import edit_command
from mex_functions import loadConfig

class Window(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.createCommandLabelsAndButtons()

    def createCommandLabelsAndButtons(self):
        config = loadConfig()
        sections = config.sections()
        for row, i in enumerate(sections):
            label = QtWidgets.QLabel(self)
            label.setText(i.capitalize())
            label.setProperty("class", "command_label")
            self.gridLayout.addWidget(label, row + 2, 0)
            self.createButton("edit", "Edytuj", i, row + 2, 1)
            self.createButton("delete", "Usuń", i, row + 2, 2)


        self.newCommandButton = QtWidgets.QPushButton(self)
        self.newCommandButton.setText("Dodaj nową komendę")
        self.newCommandButton.pressed.connect(lambda: self.buttonClicked("edit"))
        self.gridLayout.addWidget(self.newCommandButton, len(sections) + 2, 0, 1, 3)

    def buttonClicked(self, action, button=None):
        if action == "edit":
            if button:
                editCommandDialog = edit_command.Window(button.property("command"))
            else:
                editCommandDialog = edit_command.Window()
            editCommandDialog.exec()
        elif action == "delete":
            print("delete")

    def createButton(self, action, actionName, command, row, column):
        button = QtWidgets.QPushButton(self)
        button.setText(actionName)
        button.setProperty("class", "command_button")
        button.setProperty("command", command)
        button.pressed.connect(lambda button=button: self.buttonClicked(action, button))
        self.gridLayout.addWidget(button, row, column)
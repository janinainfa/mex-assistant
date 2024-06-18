from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from mexui.settings_ui import Ui_Settings
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

            button = QtWidgets.QPushButton(self)
            button.setText("Edytuj")
            button.setProperty("class", "command_button")
            button.setProperty("command", i)
            button.pressed.connect(lambda button=button: self.buttonClicked(button))
            self.gridLayout.addWidget(button, row + 2, 2)

        self.newCommandButton = QtWidgets.QPushButton(self)
        self.newCommandButton.setText("Dodaj nową komendę")
        self.newCommandButton.pressed.connect(self.addNewCommand)
        self.gridLayout.addWidget(self.newCommandButton, len(sections) + 2, 0, 1, 3)

    def buttonClicked(self, button):
        print(button.property("command"))


    def addNewCommand(self):
        pass

    def connectSignalsSlots(self):
        pass

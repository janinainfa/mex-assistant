from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from mexui.settings_ui import Ui_Settings


class Window(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def createCommandLabelAndButtons(self):
        pass

    def connectSignalsSlots(self):
        pass

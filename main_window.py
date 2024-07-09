import sys


from PyQt5.QtWidgets import QApplication, QMainWindow

from qt_material import apply_stylesheet

from mexui.main_ui import Ui_MainWindow

import settings


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, command_processing, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.commandProcessing = command_processing


    def connectSignalsSlots(self):
        self.action_Zakoncz.triggered.connect(self.close)
        self.action_Ustawienia.triggered.connect(self.openSettings)
        self.speakButton.pressed.connect(lambda: self.commandProcessing.processCommand(self))

    def openSettings(self):
        settingsWindow = settings.Window()
        settingsWindow.exec()



def buildApp(command_processing):
    app = QApplication(sys.argv)
    win = MainWindow(command_processing)
    apply_stylesheet(app, theme='dark_blue.xml', css_file='custom.css')
    win.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget

def showMessageBox(title, text, icon="NoIcon", buttons=False, buttonsText=[],callback=None):
    qmb = QMessageBox()
    qmb.setText(text)
    qmb.setWindowTitle(title)
    if icon == "NoIcon":
        qmb.setIcon(QMessageBox.NoIcon)
    if icon == "Information":
        qmb.setIcon(QMessageBox.Information)
    if icon == "Warning":
        qmb.setIcon(QMessageBox.Warning)
    if icon == "Critical":
        qmb.setIcon(QMessageBox.Critical)
    if icon == "Question":
        qmb.setIcon(QMessageBox.Question)

    if buttons == True:
        qmb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if len(buttonsText) == 2:
            qmb.button(QMessageBox.Ok).setText(buttonsText[0])
            qmb.button(QMessageBox.Cancel).setText(buttonsText[1])
    else:
        if len(buttonsText) == 1:
            qmb.setStandardButtons(QMessageBox.Ok)
            qmb.button(QMessageBox.Ok).setText(buttonsText[0])

    if qmb.exec() == QMessageBox.Ok:
        if callback:
            return callback()
        else:
            return None
    else:
        return None

def returnTrue():
    print("Callback started")
    return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("PyQt App")
    w.show()
    r=showMessageBox("Erasing records", "Are you absolutely sure you want to erase the selected records? This operation is not reversible", "Warning", True, ["Yes, erase them", "No, don't do it"], returnTrue)
    print(r)
    sys.exit(app.exec_())

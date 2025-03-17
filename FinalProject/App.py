from PyQt6.QtWidgets import QApplication, QMainWindow

from FinalProject.UI.MainLoginWindow import LoginMainWindowExt

app = QApplication([])
mainwindow = QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()

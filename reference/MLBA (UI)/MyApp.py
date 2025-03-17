from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.AdminEx import AdminEx

app=QApplication([])
myWindow = AdminEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
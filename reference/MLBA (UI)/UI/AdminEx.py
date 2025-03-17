from UI.Admin import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Connectors.Connector import Connector
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui


class AdminEx(Ui_MainWindow):
    def __init__(self):
        self.connector = Connector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.labelPassword.setPixmap(QtGui.QPixmap('images/ic_lock.png'))
        self.labelUserName.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelLogo.setPixmap(QtGui.QPixmap('images/ic_techcombank.png'))

        self.pushButtonRegister.clicked.connect(self.processRegister)
        self.pushButtonLogin.clicked.connect(self.processLogin)
        self.pushButtonExit.clicked.connect(self.processExit)
        self.ckbShow.stateChanged.connect(self.processChecked)
        self.pushButtonForgetPassword.clicked.connect(self.processForget)
    def processLogin(self):
        self.connectDatabase()
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        if (username == '') or (password == ''):
            msg = QMessageBox()
            msg.setText("You need to fill enough information")
            msg.exec()
        else:
            sql = "SELECT username, password FROM admin WHERE username = '%s'"%username
            df = self.connector.queryDataset(sql)
            if df.empty:
                msg = QMessageBox()
                msg.setText("Incorrect Username")
                msg.exec()
            else:
                if df.iloc[0]['password'] == password:
                    self.MainWindow.close()
                    self.processOption()
                else:
                    msg = QMessageBox()
                    msg.setText("Incorrect Password")
                    msg.exec()
    def connectDatabase(self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "credit_card_transaction"
        self.connector.username = "root"
        self.connector.password = ""
        self.connector.connect()
    def processOption(self):
        from UI.OptionEx import OptionEx
        self.mainUI = OptionEx()
        self.mainUI.setupUi(QMainWindow())
        self.mainUI.show()
    def processRegister(self):
        from UI.RegisterEx import RegisterEx
        self.MainWindow.close()
        self.mainUI = RegisterEx()
        self.mainUI.setupUi(QMainWindow())
        self.mainUI.show()
    def processExit(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to close the app?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processChecked(self,value):
        state=Qt.CheckState(value)
        if state==Qt.CheckState.Checked:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        elif state==Qt.CheckState.Unchecked:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    def processForget(self):
        from UI.GetPasswordEx import GetPasswordEx
        self.MainWindow.close()
        self.mainUI = GetPasswordEx()
        self.mainUI.setupUi(QMainWindow())
        self.mainUI.show()
    def show(self):
        self.MainWindow.show()
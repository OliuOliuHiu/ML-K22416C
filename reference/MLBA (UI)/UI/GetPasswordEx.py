from UI.GetPassword import Ui_MainWindow
from Connectors.Connector import Connector
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6 import QtGui

class GetPasswordEx(Ui_MainWindow):
    def __init__(self):
        self.connector = Connector()
        self.phone = ''
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.labelFirstName.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelLastName.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelPassword.setPixmap(QtGui.QPixmap('images/ic_lock.png'))
        self.labelConfirm.setPixmap(QtGui.QPixmap('images/ic_lock.png'))
        self.labelLogo.setPixmap(QtGui.QPixmap('images/ic_techcombank.png'))
        self.labelPhone.setPixmap(QtGui.QPixmap('images/ic_phone.png'))

        self.pushButtonChange.clicked.connect(self.processChange)
        self.pushButtonLogin.clicked.connect(self.processLogin)
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonRegister.clicked.connect(self.processRegister)
    def connectDatabase(self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "credit_card_transaction"
        self.connector.username = "root"
        self.connector.password = ""
        self.connector.connect()
    def processChange(self):
        firstname = self.lineEditFirstName.text()
        lastname = self.lineEditLastName.text()
        self.phone = self.lineEditPhone.text()
        if (firstname == '') or (lastname == '') or (self.phone == ''):
            msg = QMessageBox()
            msg.setText("You need to fill enough information")
            msg.exec()
        elif len(self.phone) != 10:
            msg = QMessageBox()
            msg.setText('Phone number need to have exactly 10 digits')
            msg.exec()
        else:
            self.connectDatabase()
            sql = "SELECT FirstName, LastName FROM ADMIN WHERE phone = '%s'" %self.phone
            df = self.connector.queryDataset(sql)
            if df.empty:
                msg = QMessageBox()
                msg.setText("Incorrect Phone")
                msg.exec()
            else:
                if df.iloc[0]['FirstName'] == firstname and df.iloc[0]['LastName'] == lastname:
                    self.lineEditPassword.setPlaceholderText("Enter Your New Password")
                    self.lineEditConfirm.setPlaceholderText("Confirm Your New Password")
                    self.lineEditPassword.setReadOnly(False)
                    self.lineEditConfirm.setReadOnly(False)
                else:
                    msg = QMessageBox()
                    msg.setText("First Name or Last Name is incorrect")
                    msg.exec()
    def processSave(self):
        password = self.lineEditPassword.text()
        password2 = self.lineEditConfirm.text()
        if (password2 == '') or (password == ''):
            msg = QMessageBox()
            msg.setText("You need to fill enough information")
            msg.exec()
        elif password != password2:
            msg = QMessageBox()
            msg.setText("Password do not match with confirmation password")
            msg.exec()
        elif password == password2:
            self.connectDatabase()
            sql = ("UPDATE ADMIN "
                   "SET password = '%s' where phone = '%s'") % (password, self.phone)
            self.connector.queryDataset(sql, fetch_data=False)
            self.processLogin()
    def processLogin(self):
        from UI.AdminEx import AdminEx
        self.MainWindow.close()
        self.adminUI = AdminEx()
        self.adminUI.setupUi(QMainWindow())
        self.adminUI.show()
    def processExit(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to close the app?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processRegister(self):
        from UI.RegisterEx import RegisterEx
        self.MainWindow.close()
        self.mainUI = RegisterEx()
        self.mainUI.setupUi(QMainWindow())
        self.mainUI.show()
    def show(self):
        self.MainWindow.show()
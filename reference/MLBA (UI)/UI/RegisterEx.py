from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Connectors.Connector import Connector
from UI.Register import Ui_MainWindow
from PyQt6 import QtGui

class RegisterEx(Ui_MainWindow):
    def __init__(self):
        self.connector = Connector()
        self.accounts=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.labelFirstName.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelLastName.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelUsername.setPixmap(QtGui.QPixmap('images/ic_person.png'))
        self.labelPassword.setPixmap(QtGui.QPixmap('images/ic_lock.png'))
        self.labelConfirm.setPixmap(QtGui.QPixmap('images/ic_lock.png'))
        self.labelLogo.setPixmap(QtGui.QPixmap('images/ic_techcombank.png'))
        self.labelPhone.setPixmap(QtGui.QPixmap('images/ic_phone.png'))

        self.pushButtonRegister.clicked.connect(self.processRegister)
        self.pushButtonLogin.clicked.connect(self.processLogin)
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonForget.clicked.connect(self.processForget)
    def processRegister(self):
        firstname = self.lineEditFirstName.text()
        lastname = self.lineEditLastName.text()
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        password2 = self.lineEditConfirm.text()
        phone = self.lineEditPhone.text()
        if (firstname == '') or (lastname == '') or (username == '') or (password == '') or (password2 == ''):
            msg = QMessageBox()
            msg.setText("You need to fill enough information")
            msg.exec()
        elif len(phone) != 10:
            msg = QMessageBox()
            msg.setText('Phone number need to have exactly 10 digits')
            msg.exec()
        elif password != password2:
            msg = QMessageBox()
            msg.setText("Password do not match with confirmation password")
            msg.exec()
        elif password == password2:
            msg = QMessageBox()
            msg.setText("Are you sure all information correct")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            button = msg.exec()
            if button == QMessageBox.StandardButton.Yes:
                self.connectDatabase()
                sql = "SELECT MAX(AdminID) FROM admin"
                result = self.connector.queryDataset(sql)
                adminid = int(result.iloc[0,0]) + 1
                sql1 = ("INSERT INTO admin(AdminID,FirstName,LastName,UserName,Password,Phone) "
                        "VALUES (%s,'%s','%s','%s','%s','%s')") % (adminid,firstname,lastname,username,password,phone)
                self.connector.queryDataset(sql1, fetch_data=False)
                self.processLogin()
        else:
            pass
    def processExit(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to close the app?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
    def processLogin(self):
        from UI.AdminEx import AdminEx
        self.MainWindow.close()
        self.adminUI = AdminEx()
        self.adminUI.setupUi(QMainWindow())
        self.adminUI.show()
    def processForget(self):
        from UI.GetPasswordEx import GetPasswordEx
        self.MainWindow.close()
        self.mainUI = GetPasswordEx()
        self.mainUI.setupUi(QMainWindow())
        self.mainUI.show()
    def connectDatabase(self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "credit_card_transaction"
        self.connector.username = "root"
        self.connector.password = ""
        self.connector.connect()
    def show(self):
        self.MainWindow.show()


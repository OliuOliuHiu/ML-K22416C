# Form implementation generated from reading ui file 'D:\UEL\HỌC KÌ 6\ML\K22416C\Assignment\LearnQListWidgetEmployee-18\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 776)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 250, 671, 91))
        self.groupBox.setObjectName("groupBox")
        self.pushButtonNew = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonNew.setGeometry(QtCore.QRect(30, 30, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\UEL\\HỌC KÌ 6\\ML\\K22416C\\Assignment\\LearnQListWidgetEmployee-18\\images/ic_add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNew.setIcon(icon)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSave.setGeometry(QtCore.QRect(200, 30, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\UEL\\HỌC KÌ 6\\ML\\K22416C\\Assignment\\LearnQListWidgetEmployee-18\\images/ic_save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave.setIcon(icon1)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonDelete.setGeometry(QtCore.QRect(360, 30, 101, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\UEL\\HỌC KÌ 6\\ML\\K22416C\\Assignment\\LearnQListWidgetEmployee-18\\images/ic_delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon2)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonClose.setGeometry(QtCore.QRect(530, 30, 101, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\UEL\\HỌC KÌ 6\\ML\\K22416C\\Assignment\\LearnQListWidgetEmployee-18\\images/ic_close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon3)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 370, 681, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidgetEmployee = QtWidgets.QListWidget(parent=self.groupBox_2)
        self.listWidgetEmployee.setGeometry(QtCore.QRect(10, 30, 661, 281))
        self.listWidgetEmployee.setObjectName("listWidgetEmployee")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 70, 691, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEditName.setGeometry(QtCore.QRect(70, 40, 611, 22))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEditEmail.setGeometry(QtCore.QRect(70, 90, 611, 22))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 55, 16))
        self.label_4.setObjectName("label_4")
        self.radWoman = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radWoman.setGeometry(QtCore.QRect(230, 130, 95, 20))
        self.radWoman.setObjectName("radWoman")
        self.radMan = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radMan.setGeometry(QtCore.QRect(350, 130, 95, 20))
        self.radMan.setObjectName("radMan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Employee Management"))
        self.groupBox.setTitle(_translate("MainWindow", "Action:"))
        self.pushButtonNew.setText(_translate("MainWindow", "New"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List of Employee:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Employee Information:"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Email:"))
        self.radWoman.setText(_translate("MainWindow", "Woman"))
        self.radMan.setText(_translate("MainWindow", "Man"))

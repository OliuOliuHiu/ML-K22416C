import sys
from Salemanagement.ui.MainProgramMainWindow import Ui_MainWindow

class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):  # Fix: Change "SetupUi" to "setupUi"
        super().setupUi(MainWindow)  # Calls parent setupUi method
        self.MainWindow = MainWindow  # Ensure MainWindow is stored
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
    def xuly_thoat(self):
        sys.exit(0)
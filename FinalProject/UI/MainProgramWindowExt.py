from FinalProject.UI.FINAL_MAINWINDOW import Ui_MainWindow


class MainProgramWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def showWindow(self):
        self.MainWindow.show()

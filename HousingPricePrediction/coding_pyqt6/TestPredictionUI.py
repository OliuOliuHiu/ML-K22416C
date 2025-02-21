from PyQt6.QtWidgets import QApplication, QMainWindow

from HousingPricePrediction.coding_pyqt6.HousingPricePredictionWindowExt import HousingPricePredictionWindowExt

app = QApplication([])
mainwindow = QMainWindow()
myui = HousingPricePredictionWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6 import QtGui
from UI.Option import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from UI.ChartHandle import ChartHandle
from UI.DatabaseConnectEx import DatabaseConnectEx
import pandas as pd

from Model.MLModel import MLModel
class OptionEx(QMainWindow, Ui_MainWindow):  # Kế thừa từ QMainWindow và Ui_MainWindow
    def __init__(self):
        super().__init__()  # Gọi hàm khởi tạo của QMainWindow
        self.setupUi(self)  # Thiết lập giao diện UI

        self.chartHandle = ChartHandle()
        self.databaseConnectEx = DatabaseConnectEx()
        self.databaseConnectEx.parent = self
        self.model = MLModel()
        self.connect_to_database = False
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.labelSLogo.setPixmap(QtGui.QPixmap('images/ic_logored.png'))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelSName.setFont(font)

        self.setupPlot()
        self.actionConnect_Databse.triggered.connect(self.openDatabaseConnectUI)
        self.pushButtonReality.clicked.connect(self.showRealityDistribution)
        self.pushButtonCar.clicked.connect(self.showCarDistribution)
        self.pushButtonGender.clicked.connect(self.showGenderDistribution)
        self.pushButtonYear.clicked.connect(self.showYearDistribution)
        self.pushButtonAge.clicked.connect(self.showAgeDistribution)
        self.pushButtonMonth.clicked.connect(self.showMonthDistribution)
        self.pushButtonInType.clicked.connect(self.showIncomeType)
        self.pushButtonEduType.clicked.connect(self.showEducationType)
        self.pushButtonFalType.clicked.connect(self.showFamilyType)
        self.pushButtonPredict.clicked.connect(self.processPredict)
        self.pushButtonTrain.clicked.connect(self.processTrainModel)
        self.pushButtonEvaluate.clicked.connect(self.processEvaluate)
        self.checkEnableWidget(False)
    def checkEnableWidget(self, flag=True):
        self.pushButtonReality.setEnabled(flag)
        self.pushButtonCar.setEnabled(flag)
        self.pushButtonGender.setEnabled(flag)
        self.pushButtonYear.setEnabled(flag)
        self.pushButtonAge.setEnabled(flag)
        self.pushButtonMonth.setEnabled(flag)
        self.pushButtonInType.setEnabled(flag)
        self.pushButtonEduType.setEnabled(flag)
        self.pushButtonFalType.setEnabled(flag)
        self.pushButtonPredict.setEnabled(flag)
        self.pushButtonTrain.setEnabled(flag)
        self.pushButtonEvaluate.setEnabled(flag)
    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        # adding tool bar to the layout
        self.verticalLayoutPlot.addWidget(self.toolbar)
        # adding canvas to the layout
        self.verticalLayoutPlot.addWidget(self.canvas)
    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()
    def processNotYetConnected(self):
        if self.connect_to_database == False:
            msg = QMessageBox()
            msg.setText("You need to connect database first!")
            msg.exec()
    def showDataIntoTableWidget(self,df,table):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            table.insertRow(row)
            j=0
            for data in arr:
                table.setItem(row, j, QTableWidgetItem(str(data)))
                j=j+1
            row = row + 1
    def showRealityDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processRealityDistribution()

        df = self.model.dfReality
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)

        # Đảm bảo rằng tên cột chính xác
        columnLabel = "TARGET"
        columnY1 = "Y_percentage"
        columnY2 = "N_percentage"
        title = "Distribution of Reality by Target"
        self.chartHandle.visualizeStackedBarChart(self.figure, self.canvas, df, columnLabel, columnY1, columnY2, title)
    def showCarDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processCarDistribution()

        df = self.model.dfCar
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)

        # Đảm bảo rằng tên cột chính xác
        columnLabel = "TARGET"
        columnY1 = "Y_percentage"
        columnY2 = "N_percentage"
        title = "Distribution of Car by Target"
        self.chartHandle.visualizeStackedBarChart(self.figure, self.canvas, df, columnLabel, columnY1, columnY2, title)
    def showGenderDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processGenderDistribution()

        df = self.model.dfGender
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)

        # Đảm bảo rằng tên cột chính xác
        columnLabel = "TARGET"
        columnY1 = "F_percentage"
        columnY2 = "M_percentage"
        title = "Distribution of Gender by Target"
        self.chartHandle.visualizeStackedBarChart(self.figure, self.canvas, df, columnLabel, columnY1, columnY2, title,
                                                  'Female', 'Male')
    def showYearDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        fromYear = int(self.lineEditfromYear.text())
        toYear = int(self.lineEdittoYear.text())
        self.model.processYearDistribution(fromYear,toYear)

        df = self.model.dfYears
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarPlot(self.figure, self.canvas, df,'YEARS_EMPLOYED','Counts',
                                          'TARGET','Distribution of Years_Employed by Target')
    def showAgeDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        fromAge = int(self.lineEditfromAge.text())
        toAge = int(self.lineEdittoAge.text())
        self.model.processAgeDistribution(fromAge,toAge)

        df = self.model.dfAges
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarPlot(self.figure, self.canvas, df, 'AGE','Counts',
                                           'TARGET','Distribution of Age by Target')
    def showMonthDistribution(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        fromMonth = int(self.lineEditfromMonth.text())
        toMonth = int(self.lineEdittoMonth.text())
        self.model.processMonthDistribution(fromMonth, toMonth)

        df = self.model.dfMonths
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarPlot(self.figure, self.canvas, df,'BEGIN_MONTH','Counts',
                                          'TARGET','Distribution of Months by Target')
    def showIncomeType(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processIncomeType()

        df = self.model.dfIncomeType
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarComparison(self.figure ,self.canvas, df, 'INCOME_TYPE',
                                                'Income Type Distribution (Fraud)',
                                                'Income Type Distribution (Not Fraud)')
    def showEducationType(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processEducationType()

        df = self.model.dfEduType
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarComparison(self.figure, self.canvas, df, 'EDUCATION_TYPE',
                                                'Education Type Distribution (Fraud)',
                                                'Education Type Distribution (Not Fraud)')
    def showFamilyType(self):
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.processFamilyType()

        df = self.model.dfFamilyType
        self.showDataIntoTableWidget(df,self.tableWidgetStatistic)

        # Verify the column names in df
        print(df.columns)
        self.chartHandle.visualizeBarComparison(self.figure, self.canvas, df, 'FAMILY_TYPE',
                                                'Family Type Distribution (Fraud)',
                                                'Family Type Distribution (Not Fraud)')
    def processTrainModel(self):
        algorithm = self.cboAlgorithm.currentText()
        technique = self.cboTechnique.currentText()
        random_state = int(self.lineEditRState.text())
        k = int(self.lineEditKFold.text())
        self.model.connector = self.databaseConnectEx.connector
        self.model.execCCFD()
        self.model.preProcess()
        self.model.processResampling(technique,random_state)
        self.model.processAlgorithm(algorithm,random_state,k)
    def processEvaluate(self):
        df = self.model.processEvaluation(self.model.trained_model)
        self.showDataIntoTableWidget(df,self.tableWidgetMetrics)
    def processPredict(self):
        child = int(self.lineEditChild.text())
        income = float(self.lineEditIncome.text())
        falsize = int(self.lineEditFalSize.text())
        month = int(self.lineEditBeginMonth.text())
        age = int(self.lineEditAge.text())
        year = int(self.lineEditYears.text())
        gender = pd.Series(self.cboGender.currentText()).map(
            {'Male':1, 'Female':0}
        ).iloc[0]
        car = pd.Series(self.cboCar.currentText()).map(
            {'No':0, 'Yes':1}
        ).iloc[0]
        reality = pd.Series(self.cboReality.currentText()).map(
            {'No':0, 'Yes':1}
        ).iloc[0]
        intype = pd.Series(self.cboInType.currentText()).map(
            {'Commercial associate':0,
             'Pensioner':1,
             'State servant':2,
             'Student':3,
             'Working':4}
        ).iloc[0]
        edutype = pd.Series(self.cboEduType.currentText()).map(
            {'Academic degree':0,
             'Higher education':1,
             'Incomplete higher':2,
             'Lower secondary':3,
             'Secondary / secondary special':4}
        ).iloc[0]
        faltype = pd.Series(self.cboFalType.currentText()).map(
            {'Civil marriage':0,
             'Married':1,
             'Separated':2,
             'Single / not married':3,
             'Widow':4}
        ).iloc[0]
        housetype = pd.Series(self.cboHouType.currentText()).map(
            {'Co-op apartment':0,
             'House / apartment':1,
             'Municipal apartment':2,
             'Office apartment':3,
             'Rented apartment':4,
             'With parents':5   }
        ).iloc[0]
        work_phone = pd.Series(self.cboWorkPhone.currentText()).map(
            {'No': 0, 'Yes': 1}
        ).iloc[0]
        phone = pd.Series(self.cboPhone.currentText()).map(
            {'No': 0, 'Yes': 1}
        ).iloc[0]
        email = pd.Series(self.cboWorkPhone.currentText()).map(
            {'No': 0, 'Yes': 1}
        ).iloc[0]

        new_sample = [[gender,car,reality,child,income,intype,edutype,faltype,
                       housetype,work_phone,phone,email,falsize,month,age,year]]
        model = self.model.trained_model
        target = model.predict(new_sample)
        if target == 0:
            target = 'This customer is not a fraudster'
        else:
            target = 'This customer have probably a fraudster'
        self.lineEditTarget.setText(target)

    def show(self):
        self.MainWindow.show()
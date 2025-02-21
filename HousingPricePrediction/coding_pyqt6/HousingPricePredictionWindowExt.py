import os
import pickle
from HousingPricePrediction.coding_pyqt6.HousingPricePredictionWindow import Ui_MainWindow


class HousingPricePredictionWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

        # Liệt kê các tệp trong thư mục và thêm vào comboBoxTrainedModel
        self.populate_model_list()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        # Kết nối sự kiện nhấn nút dự đoán
        self.pushButtonPredict.clicked.connect(self.processpredict)

    def populate_model_list(self):
        # Liệt kê các tệp mô hình trong thư mục
        trainemodelLink = '../TrainedModel'
        for filename in os.listdir(trainemodelLink):
            if os.path.isfile(os.path.join(trainemodelLink, filename)) and filename.endswith('.zip'):
                self.comboBoxTrainedModel.addItem(filename)

    def processpredict(self):
        # Lấy giá trị nhập từ giao diện người dùng
        AvgAreaIncome = float(self.lineEditAreaIncome.text())
        AvgAreaHouseAge = float(self.lineEditAreaHouseAge.text())
        AvgAreaNumberofRooms = float(self.lineEditNumberofRooms.text())
        AvgAreaNumberofBedrooms = float(self.lineEditNumberofBedrooms.text())
        AreaPopulation = float(self.lineEditAreaPopulation.text())

        # Lấy tên mô hình đã chọn
        modelname = '../TrainedModel/housingmodel.zip'  # Mô hình mặc định

        # Kiểm tra nếu có lựa chọn mô hình từ comboBox
        if self.comboBoxTrainedModel.currentIndex() != -1:
            modelname = f"../TrainedModel/{self.comboBoxTrainedModel.currentText()}"

        try:
            # Tải mô hình từ tệp đã chọn
            with open(modelname, 'rb') as f:
                trainmodel = pickle.load(f)

            # Dự đoán giá trị
            prediction = trainmodel.predict(
                [[AvgAreaIncome, AvgAreaHouseAge, AvgAreaNumberofRooms, AvgAreaNumberofBedrooms, AreaPopulation]])

            # Hiển thị kết quả dự đoán trên giao diện
            print("Kết quả: ", prediction)
            self.lineEditPredictedHousePrice.setText(f"{prediction[0]}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.lineEditPredictedHousePrice.setText("Lỗi khi tải mô hình!")

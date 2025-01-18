from PyQt6.QtWidgets import QMessageBox, QMainWindow
from Salemanagement.ui.LoginMainWindow import Ui_MainWindow
from Salemanagement.ui.MainprogramMainWindow import Ui_MainWindow as MainProgramWindow


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = None  # Để lưu màn hình chính

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow  # Lưu tham chiếu đến cửa sổ chính
        self.signinButton.clicked.connect(self.handle_login)  # Gắn sự kiện cho nút "Đăng nhập"

    def handle_login(self):
        # Lấy thông tin đăng nhập
        username = self.Line_Edit_usernam.text()
        password = self.Line_Edit_password.text()

        # Kiểm tra đăng nhập tạm thời
        if username == "admin" and password == "123":
            QMessageBox.information(self.MainWindow, "Thông báo", "Đăng nhập thành công!")
            self.show_main_program()  # Chuyển sang giao diện chính
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

    def show_main_program(self):
        # Hiển thị giao diện màn hình chính
        self.main_window = QMainWindow()
        main_program_ui = MainProgramWindow()
        main_program_ui.setupUi(self.main_window)
        self.main_window.show()
        self.MainWindow.close()  # Đóng giao diện đăng nhập

from PyQt6.QtWidgets import QApplication, QMainWindow
from Salemanagement.ui.LoginMainWindowExt import LoginMainWindowExt

if __name__ == "__main__":
    app = QApplication([])

    # Tạo cửa sổ chính và giao diện đăng nhập
    login_window = QMainWindow()
    login_ui = LoginMainWindowExt()
    login_ui.setupUi(login_window)
    login_window.show()  # Hiển thị giao diện đăng nhập

    app.exec()

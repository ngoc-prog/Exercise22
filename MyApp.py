import sys
from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowExt

if __name__ == "__main__":
    # Khởi tạo ứng dụng Qt
    app = QApplication(sys.argv)

    # Tạo cửa sổ chính
    main_window = MainWindowExt()

    # Hiển thị cửa sổ
    main_window.show()

    # Chạy ứng dụng Qt
    sys.exit(app.exec())

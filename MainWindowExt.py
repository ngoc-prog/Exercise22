from PyQt6 import QtCore, QtGui, QtWidgets
from math import comb

from MODULE1.Exercise22.MainWindow import Ui_MainWindow


class MainWindowExt(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonTinh.clicked.connect(self.calculate_probability)

    def calculate_probability(self):
        try:
            N_text = self.ui.lineEditN.text()
            D_text = self.ui.lineEditD.text()
            M_text = self.ui.lineEditM.text()

            N = self.validate_input(N_text)
            D = self.validate_input(D_text)
            M = self.validate_input(M_text)

            if N <= 0 or D < 0 or M <= 0 or D > N or M > N:
                raise ValueError(
                    "Dữ liệu nhập không hợp lệ! (Các giá trị phải thỏa mãn: N > 0, D >= 0, D <= N, M <= N)")

            # Tính xác suất theo phân phối hypergeometric
            probability = self.hypergeometric_probability(N, D, M)

            # Hiển thị kết quả
            self.ui.lineEditKetqua.setText(f"{probability:.4f}")
            self.ui.labelError.setText("")  # Xóa thông báo lỗi nếu có

        except ValueError as e:
            # Hiển thị lỗi nếu có
            self.ui.lineEditKetqua.setText("")
            self.ui.labelError.setText(str(e))

    def validate_input(self, text):
        """Kiểm tra xem đầu vào có phải là số nguyên hợp lệ không"""
        try:
            value = int(text)
            return value
        except ValueError:
            raise ValueError("Vui lòng nhập số nguyên hợp lệ!")

    def hypergeometric_probability(self, N, D, M):
        """
        Tính xác suất theo phân phối hypergeometric:
        P(X=1) = C(D, 1) * C(N - D, M - 1) / C(N, M)
        """
        comb_D_1 = comb(D, 1)
        comb_N_minus_D_M_minus_1 = comb(N - D, M - 1)
        comb_N_M = comb(N, M)

        # Tính xác suất
        probability = (comb_D_1 * comb_N_minus_D_M_minus_1) / comb_N_M
        return probability

# Form implementation generated from reading ui file 'D:\KTLT_NGUYENVONHUNGOC_EXERCISE\MODULE1\Exercise22\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 434)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 601, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditN.setGeometry(QtCore.QRect(430, 20, 161, 20))
        self.lineEditN.setObjectName("lineEditN")
        self.lineEditD = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditD.setGeometry(QtCore.QRect(430, 50, 161, 20))
        self.lineEditD.setObjectName("lineEditD")
        self.lineEditM = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditM.setGeometry(QtCore.QRect(430, 80, 161, 20))
        self.lineEditM.setObjectName("lineEditM")
        self.pushButtonTinh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTinh.setGeometry(QtCore.QRect(270, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonTinh.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT_NGUYENVONHUNGOC_EXERCISE\\MODULE1\\Exercise22\\image/2530794_accounting_calculate_calculation_calculator_general_icon (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTinh.setIcon(icon)
        self.pushButtonTinh.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonTinh.setObjectName("pushButtonTinh")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 401, 41))
        self.label_5.setObjectName("label_5")
        self.lineEditKetqua = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditKetqua.setGeometry(QtCore.QRect(430, 30, 161, 20))
        self.lineEditKetqua.setObjectName("lineEditKetqua")
        self.labelError = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(10, 350, 601, 31))
        self.labelError.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditN, self.lineEditD)
        MainWindow.setTabOrder(self.lineEditD, self.lineEditM)
        MainWindow.setTabOrder(self.lineEditM, self.pushButtonTinh)
        MainWindow.setTabOrder(self.pushButtonTinh, self.lineEditKetqua)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tính xác suất chọn bóng đèn hỏng"))
        self.label_2.setText(_translate("MainWindow", "Số lượng bóng đèn trong hộp (N):"))
        self.label_3.setText(_translate("MainWindow", "Số bóng đèn bị hỏng (D):"))
        self.label_4.setText(_translate("MainWindow", "Số bóng đèn được chọn (M):"))
        self.pushButtonTinh.setText(_translate("MainWindow", "Tính"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Results:"))
        self.label_5.setText(_translate("MainWindow", "Xác suất chọn 1 bóng đèn hỏng là:"))

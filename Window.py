from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 240, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ListPorts = QtWidgets.QComboBox(self.layoutWidget)
        self.ListPorts.setObjectName("ListPorts")
        self.horizontalLayout.addWidget(self.ListPorts)
        self.ButOpenPort = QtWidgets.QPushButton(self.layoutWidget)
        self.ButOpenPort.setObjectName("ButOpenPort")
        self.horizontalLayout.addWidget(self.ButOpenPort)
        self.ButClosePort = QtWidgets.QPushButton(self.layoutWidget)
        self.ButClosePort.setObjectName("ButClosePort")
        self.horizontalLayout.addWidget(self.ButClosePort)
        self.SlidePower = QtWidgets.QSlider(self.centralwidget)
        self.SlidePower.setGeometry(QtCore.QRect(200, 50, 160, 22))
        self.SlidePower.setOrientation(QtCore.Qt.Horizontal)
        self.SlidePower.setObjectName("SlidePower")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Window"))
        self.ButOpenPort.setText(_translate("MainWindow", "открыть порт"))
        self.ButClosePort.setText(_translate("MainWindow", "закрыть порт"))

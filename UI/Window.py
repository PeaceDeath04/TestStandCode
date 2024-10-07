from PyQt5 import QtCore, QtGui, QtWidgets
from data_processing.Data import localData, export_to_json, import_from_json, create_json,key_to_Graphs
from arduino_processing.packet_processing import *
from arduino_processing.SerialManager import read_data,open_port,close_port,update_port_list,serial
from arduino_processing.ProjectProcessing import TxToARDU
from data_processing.GraphHandler import *
import globals
from globals import read_ready


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1598, 966)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 1601, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_Layout.setContentsMargins(0, 0, 0, 0)
        self.graph_Layout.setObjectName("graph_Layout")
        self.debugWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugWindow.setEnabled(True)
        self.debugWindow.setGeometry(QtCore.QRect(20, 810, 1361, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugWindow.sizePolicy().hasHeightForWidth())
        self.debugWindow.setSizePolicy(sizePolicy)
        self.debugWindow.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.debugWindow.setObjectName("debugWindow")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 981, 280))
        self.layoutWidget.setObjectName("layoutWidget")
        self.GlobalMenu = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.GlobalMenu.setContentsMargins(0, 0, 0, 0)
        self.GlobalMenu.setObjectName("GlobalMenu")
        self.MenuPorts = QtWidgets.QHBoxLayout()
        self.MenuPorts.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.MenuPorts.setContentsMargins(-1, 0, -1, -1)
        self.MenuPorts.setSpacing(6)
        self.MenuPorts.setObjectName("MenuPorts")
        self.ListPorts = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListPorts.sizePolicy().hasHeightForWidth())
        self.ListPorts.setSizePolicy(sizePolicy)
        self.ListPorts.setObjectName("ListPorts")
        self.MenuPorts.addWidget(self.ListPorts)
        self.ButOpenPort = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButOpenPort.sizePolicy().hasHeightForWidth())
        self.ButOpenPort.setSizePolicy(sizePolicy)
        self.ButOpenPort.setObjectName("ButOpenPort")
        self.MenuPorts.addWidget(self.ButOpenPort)
        self.ButClosePort = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButClosePort.sizePolicy().hasHeightForWidth())
        self.ButClosePort.setSizePolicy(sizePolicy)
        self.ButClosePort.setObjectName("ButClosePort")
        self.MenuPorts.addWidget(self.ButClosePort)
        self.MenuPorts.setStretch(0, 1)
        self.MenuPorts.setStretch(1, 2)
        self.MenuPorts.setStretch(2, 2)
        self.GlobalMenu.addLayout(self.MenuPorts)
        self.butRefresh = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRefresh.sizePolicy().hasHeightForWidth())
        self.butRefresh.setSizePolicy(sizePolicy)
        self.butRefresh.setObjectName("butRefresh")
        self.GlobalMenu.addWidget(self.butRefresh)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButTarTraction = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButTarTraction.sizePolicy().hasHeightForWidth())
        self.ButTarTraction.setSizePolicy(sizePolicy)
        self.ButTarTraction.setObjectName("ButTarTraction")
        self.horizontalLayout.addWidget(self.ButTarTraction)
        self.ButTarWeight = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButTarWeight.sizePolicy().hasHeightForWidth())
        self.ButTarWeight.setSizePolicy(sizePolicy)
        self.ButTarWeight.setObjectName("ButTarWeight")
        self.horizontalLayout.addWidget(self.ButTarWeight)
        self.GlobalMenu.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ButCalibTraction = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalibTraction.sizePolicy().hasHeightForWidth())
        self.ButCalibTraction.setSizePolicy(sizePolicy)
        self.ButCalibTraction.setObjectName("ButCalibTraction")
        self.horizontalLayout_3.addWidget(self.ButCalibTraction)
        self.ButCalibWeight = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalibWeight.sizePolicy().hasHeightForWidth())
        self.ButCalibWeight.setSizePolicy(sizePolicy)
        self.ButCalibWeight.setObjectName("ButCalibWeight")
        self.horizontalLayout_3.addWidget(self.ButCalibWeight)
        self.GlobalMenu.addLayout(self.horizontalLayout_3)
        self.ButCalib = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalib.sizePolicy().hasHeightForWidth())
        self.ButCalib.setSizePolicy(sizePolicy)
        self.ButCalib.setObjectName("ButCalib")
        self.GlobalMenu.addWidget(self.ButCalib)
        self.ButSaveExl = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButSaveExl.sizePolicy().hasHeightForWidth())
        self.ButSaveExl.setSizePolicy(sizePolicy)
        self.ButSaveExl.setObjectName("ButSaveExl")
        self.GlobalMenu.addWidget(self.ButSaveExl)
        self.MenuChangeGas = QtWidgets.QVBoxLayout()
        self.MenuChangeGas.setObjectName("MenuChangeGas")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBoxMin = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxMin.sizePolicy().hasHeightForWidth())
        self.spinBoxMin.setSizePolicy(sizePolicy)
        self.spinBoxMin.setObjectName("spinBoxMin")
        self.horizontalLayout_2.addWidget(self.spinBoxMin)
        self.spinBoxMax = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxMax.sizePolicy().hasHeightForWidth())
        self.spinBoxMax.setSizePolicy(sizePolicy)
        self.spinBoxMax.setObjectName("spinBoxMax")
        self.horizontalLayout_2.addWidget(self.spinBoxMax)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.SlidePower = QtWidgets.QSlider(self.layoutWidget)
        self.SlidePower.setMaximum(50)
        self.SlidePower.setPageStep(0)
        self.SlidePower.setProperty("value", 50)
        self.SlidePower.setOrientation(QtCore.Qt.Horizontal)
        self.SlidePower.setObjectName("SlidePower")
        self.verticalLayout.addWidget(self.SlidePower)
        self.valueGas = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueGas.sizePolicy().hasHeightForWidth())
        self.valueGas.setSizePolicy(sizePolicy)
        self.valueGas.setAutoFillBackground(False)
        self.valueGas.setAlignment(QtCore.Qt.AlignCenter)
        self.valueGas.setObjectName("valueGas")
        self.verticalLayout.addWidget(self.valueGas)
        self.MenuChangeGas.addLayout(self.verticalLayout)
        self.GlobalMenu.addLayout(self.MenuChangeGas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1598, 21))
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
        self.debugWindow.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ButOpenPort.setText(_translate("MainWindow", "открыть порт"))
        self.ButClosePort.setText(_translate("MainWindow", "закрыть порт"))
        self.butRefresh.setText(_translate("MainWindow", "Обновить список портов"))
        self.ButTarTraction.setText(_translate("MainWindow", "Тарирование тяги"))
        self.ButTarWeight.setText(_translate("MainWindow", "Тарирование веса"))
        self.ButCalibTraction.setText(_translate("MainWindow", "Калибровка тяги"))
        self.ButCalibWeight.setText(_translate("MainWindow", "Калибровка веса"))
        self.ButCalib.setText(_translate("MainWindow", " Калибровка мотора"))
        self.ButSaveExl.setText(_translate("MainWindow", "Начать запись параметров"))
        self.valueGas.setText(_translate("MainWindow", "TextLabel"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        serial.readyRead.connect(read_data)
        self.spinBoxMin.valueChanged.connect(self.GetRangeGas)
        self.spinBoxMax.valueChanged.connect(self.GetRangeGas)
        self.ButOpenPort.clicked.connect(self.open_port)
        self.ButClosePort.clicked.connect(self.close_port)
        self.butRefresh.clicked.connect(self.update_ports)
        self.SlidePower.valueChanged.connect(self.get_gas_value)
        self.ButSaveExl.clicked.connect(self.toggle_read)

        self.ButTarTraction.clicked.connect(lambda: but_taring("Traction"))
        self.ButTarWeight.clicked.connect(lambda: but_taring("Weight"))

        self.ButCalib.clicked.connect(lambda: TxToARDU(ButCalibMotor=0))
        self.ButCalibTraction.clicked.connect(lambda:get_kef_tenz("Traction"))
        self.ButCalibWeight.clicked.connect(lambda:get_kef_tenz("Weight"))

        self.ButSaveExl.setCheckable(True)


        self.read = False
        self.step_size = 10  # По умолчанию шаг 10, но будет пересчитываться динамически

        create_json("save_file.json",localData)
        create_json("keys_graphs.json",key_to_Graphs)
        graphs.update(add_graphs())
        self.add_to_lay()

        self.onStartUp()

    def get_gas_percentage(self):
        try:
            a, b, c = localData.get("gas_min"), localData.get("gas_max"), localData.get("gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    def toggle_read(self):
        #Изменяем состояние read при каждом нажатии кнопки
        self.read = not self.read
        globals.read_ready = self.read
        if self.read:
            recorder.start_new_recording()
            self.ButSaveExl.setText("Остановить запись")
        else:
            self.ButSaveExl.setText("начать запись в data.csv")
            recorder.convert_csv_to_xlsx()
            
    def GetRangeGas(self):
        """Обновление диапазона слайдера при изменении Min и Max значений."""
        gas_min = self.spinBoxMin.value()
        gas_max = self.spinBoxMax.value()

        if gas_min >= gas_max:
            gas_min = 0

        self.SlidePower.setMinimum(gas_min)
        self.SlidePower.setMaximum(gas_max)
        self.SlidePower.setValue(gas_min)

        # Вычисление шага на основе текущих минимального и максимального значений
        self.step_size = (gas_max - gas_min) // 10  # шаг изменения ползунка в процентах
        if self.step_size == 0:
            self.step_size = 1  # Защита от деления на 0
        localData["gas_min"],localData["gas_max"] = gas_min,gas_max
        TxToARDU(gas_min=gas_min, gas_max=gas_max)
        export_to_json(name_file="save_file.json",gas_max=gas_max,gas_min= gas_min)

    def get_gas_value(self):
        """Корректировка значения слайдера по ближайшему шагу."""
        current_value = self.SlidePower.value()
        # Округление до ближайшего кратного значения шага
        corrected_value = round(current_value / self.step_size) * self.step_size
        localData["gas"] = corrected_value
        TxToARDU(gas=corrected_value)

        self.SlidePower.blockSignals(True)  # Отключаем сигналы, чтобы избежать рекурсии
        self.SlidePower.setValue(corrected_value)  # Устанавливаем скорректированное значение
        self.SlidePower.blockSignals(False)  # Включаем сигналы обратно

        # Отправляем скорректированное значение контроллеру и обновляем интерфейс
        export_to_json(gas=corrected_value,name_file="save_file.json")
        gas_percentage = self.get_gas_percentage()
        self.valueGas.setText(str(gas_percentage))

    def onStartUp(self):
        """Инициализация начальных параметров при запуске приложения."""
        gas_min, gas_max, gas = import_from_json("save_file.json", "gas_min", "gas_max", "gas")
        self.spinBoxMin.setMaximum(999999)
        self.spinBoxMin.setValue(0)
        self.spinBoxMax.setMaximum(999999)
        self.spinBoxMax.setValue(0)
        self.spinBoxMin.setValue(gas_min)
        self.spinBoxMax.setValue(gas_max)
        self.SlidePower.setMinimum(gas_min)
        self.SlidePower.setMaximum(gas_max)
        self.SlidePower.setValue(gas)
        self.SlidePower.setProperty("value", gas)

        # Пересчитываем шаг и корректируем начальное значение
        self.GetRangeGas()
        self.get_gas_value()

    def open_port(self):
        port_name = self.ListPorts.currentText()
        result = open_port(port_name)
        self.sendDb(result)

    def close_port(self):
        result = close_port()
        self.sendDb(result)

    def update_ports(self):
        ports = update_port_list()
        self.ListPorts.clear()
        self.ListPorts.addItems(ports)
        self.sendDb("Список портов обновлен")

    def sendDb(self, text):
        self.debugWindow.append(text)

    def add_to_lay(self):
        for nameGraph,params in graphs.items():
            for obj in params.values():
                if isinstance(obj,Graph):
                    self.graph_Layout.addWidget(obj.canvas)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtTest import QTest
from openpyxl.styles.builtins import percent
from wheel.cli.convert import convert

from UI.settings_window import SettingsWindow
from data_processing.Data import localData, export_to_json, import_from_json, create_json,key_to_Graphs
from arduino_processing.packet_processing import *
from arduino_processing.SerialManager import read_data,open_port,close_port,update_port_list,serial
from arduino_processing.ProjectProcessing import TxToARDU
from data_processing.GraphHandler import *
import globals
from data_processing.Tables import FigureCanvas
from UI.WindowAutoTest import IterationDialog
from UI.settings_window import SettingsWindow
from globals import read_ready


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 935)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("QWidget {\n"
                                 "        background-color: #1e1e1e;  /* Очень темный фон */\n"
                                 "        color: #d3d3d3;  /* Светло-серый цвет текста */\n"
                                 "        font-family: Arial, sans-serif;\n"
                                 "        font-size: 12px;\n"
                                 "    }\n"
                                 "    QPushButton {\n"
                                 "        background-color: #2d2d2d;  /* Темный фон для кнопок */\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 5px;\n"
                                 "        font-weight: bold;\n"
                                 "    }\n"
                                 "    QPushButton:hover {\n"
                                 "        background-color: #00b894;  /* Светло-зеленый при наведении */\n"
                                 "        color: #1e1e1e;\n"
                                 "    }\n"
                                 "    QComboBox {\n"
                                 "        border: 1px solid #2d2d2d;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        background-color: #2d2d2d;\n"
                                 "    }\n"
                                 "    QTextBrowser {\n"
                                 "        background-color: #2d2d2d;  /* Темный фон для окна вывода */\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 5px;\n"
                                 "    }\n"
                                 "    QLabel {\n"
                                 "        color: #d3d3d3;  /* Мягкий серый цвет для текста */\n"
                                 "        font-weight: bold;\n"
                                 "        font-size: 14px;\n"
                                 "    }\n"
                                 "    QSpinBox {\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        color: #d3d3d3;\n"
                                 "    }\n"
                                 "    QDoubleSpinBox{\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        color: #d3d3d3;\n"
                                 "}\n"
                                 "\n"
                                 "    QSlider {\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border-radius: 5px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 1861, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_Layout.setContentsMargins(0, 0, 0, 0)
        self.graph_Layout.setObjectName("graph_Layout")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1561, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.GlobalMenu = QtWidgets.QVBoxLayout()
        self.GlobalMenu.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.GlobalMenu.setContentsMargins(-1, -1, -1, 0)
        self.GlobalMenu.setSpacing(0)
        self.GlobalMenu.setObjectName("GlobalMenu")
        self.MenuPorts = QtWidgets.QHBoxLayout()
        self.MenuPorts.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.MenuPorts.setContentsMargins(-1, 0, 0, 0)
        self.MenuPorts.setSpacing(6)
        self.MenuPorts.setObjectName("MenuPorts")
        self.ListPorts = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListPorts.sizePolicy().hasHeightForWidth())
        self.ListPorts.setSizePolicy(sizePolicy)
        self.ListPorts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ListPorts.setObjectName("ListPorts")
        self.MenuPorts.addWidget(self.ListPorts)
        self.ButOpenPort = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButOpenPort.sizePolicy().hasHeightForWidth())
        self.ButOpenPort.setSizePolicy(sizePolicy)
        self.ButOpenPort.setMinimumSize(QtCore.QSize(0, 0))
        self.ButOpenPort.setAutoDefault(False)
        self.ButOpenPort.setDefault(False)
        self.ButOpenPort.setFlat(False)
        self.ButOpenPort.setObjectName("ButOpenPort")
        self.MenuPorts.addWidget(self.ButOpenPort)
        self.GlobalMenu.addLayout(self.MenuPorts)
        self.butRefresh = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRefresh.sizePolicy().hasHeightForWidth())
        self.butRefresh.setSizePolicy(sizePolicy)
        self.butRefresh.setObjectName("butRefresh")
        self.GlobalMenu.addWidget(self.butRefresh)
        self.horizontalLayout_4.addLayout(self.GlobalMenu)
        self.settings_lay = QtWidgets.QVBoxLayout()
        self.settings_lay.setSpacing(0)
        self.settings_lay.setObjectName("settings_lay")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButTarTraction = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButTarTraction.sizePolicy().hasHeightForWidth())
        self.ButTarTraction.setSizePolicy(sizePolicy)
        self.ButTarTraction.setObjectName("ButTarTraction")
        self.horizontalLayout.addWidget(self.ButTarTraction)
        self.ButTarWeight = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButTarWeight.sizePolicy().hasHeightForWidth())
        self.ButTarWeight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ButTarWeight.setFont(font)
        self.ButTarWeight.setObjectName("ButTarWeight")
        self.horizontalLayout.addWidget(self.ButTarWeight)
        self.settings_lay.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ButCalibTraction = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalibTraction.sizePolicy().hasHeightForWidth())
        self.ButCalibTraction.setSizePolicy(sizePolicy)
        self.ButCalibTraction.setObjectName("ButCalibTraction")
        self.horizontalLayout_3.addWidget(self.ButCalibTraction)
        self.ButCalibWeight = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalibWeight.sizePolicy().hasHeightForWidth())
        self.ButCalibWeight.setSizePolicy(sizePolicy)
        self.ButCalibWeight.setObjectName("ButCalibWeight")
        self.horizontalLayout_3.addWidget(self.ButCalibWeight)
        self.settings_lay.addLayout(self.horizontalLayout_3)
        self.ButCalib = QtWidgets.QPushButton(self.layoutWidget)
        self.ButCalib.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButCalib.sizePolicy().hasHeightForWidth())
        self.ButCalib.setSizePolicy(sizePolicy)
        self.ButCalib.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ButCalib.setFont(font)
        self.ButCalib.setMouseTracking(False)
        self.ButCalib.setTabletTracking(False)
        self.ButCalib.setIconSize(QtCore.QSize(16, 16))
        self.ButCalib.setAutoDefault(False)
        self.ButCalib.setDefault(False)
        self.ButCalib.setFlat(False)
        self.ButCalib.setObjectName("ButCalib")
        self.settings_lay.addWidget(self.ButCalib)
        self.horizontalLayout_4.addLayout(self.settings_lay)
        self.MenuChangeGas = QtWidgets.QVBoxLayout()
        self.MenuChangeGas.setObjectName("MenuChangeGas")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBoxMin = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxMin.sizePolicy().hasHeightForWidth())
        self.spinBoxMin.setSizePolicy(sizePolicy)
        self.spinBoxMin.setObjectName("spinBoxMin")
        self.horizontalLayout_2.addWidget(self.spinBoxMin)
        self.spinBoxMax = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxMax.sizePolicy().hasHeightForWidth())
        self.spinBoxMax.setSizePolicy(sizePolicy)
        self.spinBoxMax.setObjectName("spinBoxMax")
        self.horizontalLayout_2.addWidget(self.spinBoxMax)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.valueGas = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueGas.sizePolicy().hasHeightForWidth())
        self.valueGas.setSizePolicy(sizePolicy)
        self.valueGas.setAutoFillBackground(False)
        self.valueGas.setScaledContents(False)
        self.valueGas.setAlignment(QtCore.Qt.AlignCenter)
        self.valueGas.setObjectName("valueGas")
        self.verticalLayout.addWidget(self.valueGas)
        self.SlidePower = QtWidgets.QSlider(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SlidePower.sizePolicy().hasHeightForWidth())
        self.SlidePower.setSizePolicy(sizePolicy)
        self.SlidePower.setAutoFillBackground(False)
        self.SlidePower.setMaximum(50)
        self.SlidePower.setPageStep(0)
        self.SlidePower.setProperty("value", 50)
        self.SlidePower.setOrientation(QtCore.Qt.Horizontal)
        self.SlidePower.setObjectName("SlidePower")
        self.verticalLayout.addWidget(self.SlidePower)
        self.MenuChangeGas.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.MenuChangeGas)
        self.LayAutoTest = QtWidgets.QVBoxLayout()
        self.LayAutoTest.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.LayAutoTest.setContentsMargins(-1, 0, -1, 0)
        self.LayAutoTest.setSpacing(6)
        self.LayAutoTest.setObjectName("LayAutoTest")
        self.ButSaveExl = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButSaveExl.sizePolicy().hasHeightForWidth())
        self.ButSaveExl.setSizePolicy(sizePolicy)
        self.ButSaveExl.setObjectName("ButSaveExl")
        self.LayAutoTest.addWidget(self.ButSaveExl)
        self.ButAutoTest = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButAutoTest.sizePolicy().hasHeightForWidth())
        self.ButAutoTest.setSizePolicy(sizePolicy)
        self.ButAutoTest.setObjectName("ButAutoTest")
        self.LayAutoTest.addWidget(self.ButAutoTest)
        self.horizontalLayout_4.addLayout(self.LayAutoTest)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.ActionSettings = QtWidgets.QAction(MainWindow)
        self.ActionSettings.setObjectName("ActionSettings")
        self.menu.addAction(self.ActionSettings)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Window"))
        self.ButOpenPort.setText(_translate("MainWindow", "открыть порт"))
        self.butRefresh.setText(_translate("MainWindow", "Обновить список портов"))
        self.ButTarTraction.setText(_translate("MainWindow", "Тарирование тяги"))
        self.ButTarWeight.setText(_translate("MainWindow", "Тарирование веса"))
        self.ButCalibTraction.setText(_translate("MainWindow", "Калибровка тяги"))
        self.ButCalibWeight.setText(_translate("MainWindow", "Калибровка веса"))
        self.ButCalib.setText(_translate("MainWindow", "Калибровка мотора"))
        self.label.setText(_translate("MainWindow", "Установка оффсета мощности"))
        self.valueGas.setText(_translate("MainWindow", "Значение газа"))
        self.ButSaveExl.setText(_translate("MainWindow", "Начать запись параметров"))
        self.ButAutoTest.setText(_translate("MainWindow", "Начать автотест"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "настройки"))
        self.action_2.setText(_translate("MainWindow", "настройки параметров"))
        self.ActionSettings.setText(_translate("MainWindow", "настройки"))

    def __init__(self):
        super().__init__()
        self.window_settings = SettingsWindow()
        self.setupUi(self)
        serial.readyRead.connect(read_data)
        self.spinBoxMin.valueChanged.connect(self.GetRangeGas)
        self.spinBoxMax.valueChanged.connect(self.GetRangeGas)
        self.ButOpenPort.clicked.connect(self.toggle_port)
        self.butRefresh.clicked.connect(self.update_ports)
        self.SlidePower.valueChanged.connect(self.get_gas_value)
        self.ButSaveExl.clicked.connect(self.toggle_read)
        self.ButTarTraction.clicked.connect(lambda: but_taring("Traction"))
        self.ButTarWeight.clicked.connect(lambda: but_taring("Weight"))
        self.ButCalib.clicked.connect(lambda: TxToARDU(ButCalibMotor=0))
        self.ButAutoTest.clicked.connect(self.auto_test)
        self.ButCalibTraction.clicked.connect(lambda:get_kef_tenz("Traction"))
        self.ButCalibWeight.clicked.connect(lambda:get_kef_tenz("Weight"))
        self.ActionSettings.triggered.connect(self.open_settings)

        """     self.calib_weight_spinbox.valueChanged.connect(self.change_weight)
                self.spinbox_change_step.valueChanged.connect(self.change_step)"""

        self.ButSaveExl.setCheckable(True)
        self.read = False
        self.port_open = False
        self.step_size = 10  # По умолчанию шаг 10, но будет пересчитываться динамически

        self.last_value = 0
        self.corrected_value = 0

        self.selected_graph = None # сохраняем нажатый график

        create_json("save_file.json",localData)
        create_json("keys_graphs.json",key_to_Graphs)
        graphs.update(add_graphs())
        self.add_to_lay()

        self.onStartUp()

    def open_settings(self):
        self.window_settings.show()

    def get_gas_percentage(self):
        try:
            a, b, c = localData.get("gas_min"), localData.get("gas_max"), localData.get("gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    def calculate_value_from_percentage(self,percentage):
        """
        Вычисляет число в заданном диапазоне для определенного процента.

        :param percentage: Процент (int или float, 0-100)
        :return: Число, соответствующее percentage% от диапазона
        """
        try:
            if not (0 <= percentage <= 100):
                return "Ошибка: процент должен быть в диапазоне от 0 до 100"

            return int(self.spinBoxMin.value() + (percentage / 100) * (self.spinBoxMax.value() - self.spinBoxMin.value()))
        except TypeError:
            return "Ошибка: переданы некорректные значения"

    def auto_test(self):
        points = import_js("timings.json")

        recorder.base_filename = "AutoTest"
        TxToARDU(ResetTime=0)
        self.toggle_read()

        for point in points.values():
            for gas,time in point.items():
                gas,time = int(gas), int(time)
                gas = self.calculate_value_from_percentage(gas)
                self.SlidePower.setValue(gas)
                QTest.qWait(time)
        self.toggle_read()
        self.SlidePower.setValue(self.spinBoxMin.value())

    def toggle_port(self):
        self.port_open = not self.port_open
        if self.port_open:
            self.open_port()
            self.ButOpenPort.setText("Закрыть порт")
        else:
            close_port()
            self.ButOpenPort.setText("открыть порт")

    def change_weight(self):
        globals.calib_weight = self.calib_weight_spinbox.value()

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
        self.step_size = globals.step_size  # шаг изменения ползунка в процентах

        if self.step_size == 0:
            self.step_size = 1  # Защита от деления на 0
        localData["gas_min"],localData["gas_max"] = gas_min,gas_max
        TxToARDU(gas_min=gas_min, gas_max=gas_max)
        export_to_json(name_file="save_file.json",gas_max=gas_max,gas_min= gas_min)

    def get_gas_value(self):
        """Корректировка значения слайдера по ближайшему шагу."""
        current_value = self.SlidePower.value()

        # Округление до ближайшего кратного значения шага
        self.corrected_value = round(current_value / globals.step_size) * globals.step_size
        self.SlidePower.blockSignals(True)  # Отключаем сигналы, чтобы избежать рекурсии
        self.SlidePower.setValue(self.corrected_value)  # Устанавливаем скорректированное значение
        self.SlidePower.blockSignals(False)  # Включаем сигналы обратно

        if self.last_value != self.corrected_value:
            # Отправляем скорректированное значение контроллеру и обновляем интерфейс
            localData["gas"] = self.corrected_value
            TxToARDU(gas=self.corrected_value)
            export_to_json(gas=self.corrected_value, name_file="save_file.json")
            gas_percentage = self.get_gas_percentage()
            self.valueGas.setText(
                f"Значение газа в процентах: {str(gas_percentage)}    Численное значние: {self.corrected_value}")
            self.last_value = self.corrected_value

    def onStartUp(self):
        """Инициализация начальных параметров при запуске приложения."""
        gas_min, gas_max, gas = import_from_json("save_file.json", "gas_min", "gas_max", "gas")
        self.spinBoxMin.setMaximum(999999)
        self.spinBoxMin.setValue(0)
        self.spinBoxMax.setMaximum(999999)
        self.spinBoxMax.setValue(0)

        """self.calib_weight_spinbox.setMaximum(999999)
        self.calib_weight_spinbox.setValue(globals.calib_weight)

        self.spinbox_change_step.setMaximum(999999)"""


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

    def close_port(self):
        result = close_port()

    def update_ports(self):
        ports = update_port_list()
        self.ListPorts.clear()
        self.ListPorts.addItems(ports)

    def eventFilter(self, source, event):
        """Обрабатывает клики и прокрутку колесика для изменения масштаба графика"""

        # Обрабатываем клик мыши для выбора графика
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                if isinstance(source, FigureCanvas):
                    # Проходим по всем графикам
                    for name_graph, params in graphs.items():
                        obj = params.get("ObjectClass")
                        if obj and source == obj.canvas:
                            print(f"Выбран график: {name_graph}")
                            # Сохраняем выбранный график
                            self.selected_graph = obj
                            break
                return True  # Событие обработано

        # Обрабатываем прокрутку колесика для масштабирования
        if event.type() == QtCore.QEvent.Wheel:
            if isinstance(source, FigureCanvas):
                # Проверяем, что график был выбран ранее
                if self.selected_graph and source == self.selected_graph.canvas:
                    # Определяем направление прокрутки
                    delta = event.angleDelta().y()
                    if delta > 0:
                        # Прокрутка вверх — увеличиваем масштаб на 0.1
                        self.selected_graph.scale_graph(-0.1)  # Увеличиваем масштаб
                    else:
                        # Прокрутка вниз — уменьшаем масштаб на 0.1
                        self.selected_graph.scale_graph(0.1)  # Уменьшаем масштаб

                    return True  # Событие обработано
        return super().eventFilter(source, event)

    def add_to_lay(self):
        for nameGraph, params in graphs.items():
            for obj in params.values():
                if isinstance(obj, Graph):
                    self.graph_Layout.addWidget(obj.canvas)  # Добавляем график в layout
                    obj.canvas.installEventFilter(self)



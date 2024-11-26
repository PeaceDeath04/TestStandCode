import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from data_processing.Data import export_to_json, create_json, import_from_json, import_js
from globals import json_dir
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox
import globals


class SettingsWindow(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1240, 536)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
                           "    background-color: #1e1e1e;  /* Очень темный фон */\n"
                           "    color: #d3d3d3;  /* Светло-серый цвет текста */\n"
                           "    font-family: Arial, sans-serif;\n"
                           "    font-size: 12px;\n"
                           "}\n"
                           "\n"
                           "QPushButton {\n"
                           "    background-color: #2d2d2d;  /* Темный фон для кнопок */\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5px;\n"
                           "    padding: 5px;\n"
                           "    font-weight: bold;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover {\n"
                           "    background-color: #00b894;  /* Светло-зеленый при наведении */\n"
                           "    color: #1e1e1e;\n"
                           "}\n"
                           "\n"
                           "QComboBox {\n"
                           "    border: 1px solid #2d2d2d;\n"
                           "    border-radius: 5px;\n"
                           "    padding: 2px;\n"
                           "    background-color: #2d2d2d;\n"
                           "}\n"
                           "\n"
                           "QTextBrowser {\n"
                           "    background-color: #2d2d2d;  /* Темный фон для окна вывода */\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5px;\n"
                           "    padding: 5px;\n"
                           "}\n"
                           "\n"
                           "QLabel {\n"
                           "    color: #d3d3d3;  /* Мягкий серый цвет для текста */\n"
                           "    font-weight: bold;\n"
                           "    font-size: 14px;\n"
                           "}\n"
                           "\n"
                           "QSpinBox {\n"
                           "    background-color: #2d2d2d;\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5px;\n"
                           "    padding: 2px;\n"
                           "    color: #d3d3d3;\n"
                           "}\n"
                           "\n"
                           "QDoubleSpinBox {\n"
                           "    background-color: #2d2d2d;\n"
                           "    border: 1px solid #1e1e1e;\n"
                           "    border-radius: 5px;\n"
                           "    padding: 2px;\n"
                           "    color: #d3d3d3;\n"
                           "}\n"
                           "\n"
                           "QSlider {\n"
                           "    background-color: #2d2d2d;\n"
                           "    border-radius: 5px;\n"
                           "}\n"
                           "\n"
                           "QScrollArea {\n"
                           "    border: none;\n"
                           "}\n"
                           "\n"
                           "QScrollBar:vertical {\n"
                           "    background: rgb(45, 45, 45);\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:vertical {\n"
                           "    background: rgb(0, 184, 148);\n"
                           "    min-width: 20px;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                           "    background: none;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
                           "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
                           "    background: transparent;  /* Убирает стрелки вверх и вниз */\n"
                           "    width: 0px;  /* Убирает размеры кнопок */\n"
                           "    height: 0px;  /* Убирает размеры кнопок */\n"
                           "}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 80, 189, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.lay_change_step_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.lay_change_step_5.setContentsMargins(0, 0, 0, 0)
        self.lay_change_step_5.setObjectName("lay_change_step_5")
        self.text_change_step_5 = QtWidgets.QLabel(self.layoutWidget)
        self.text_change_step_5.setAlignment(QtCore.Qt.AlignCenter)
        self.text_change_step_5.setObjectName("text_change_step_5")
        self.lay_change_step_5.addWidget(self.text_change_step_5)
        self.spinbox_change_step = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinbox_change_step.setObjectName("spinbox_change_step")
        self.lay_change_step_5.addWidget(self.spinbox_change_step)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 20, 220, 47))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.lay_params = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.lay_params.setContentsMargins(0, 0, 0, 0)
        self.lay_params.setObjectName("lay_params")
        self.calib_label = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calib_label.sizePolicy().hasHeightForWidth())
        self.calib_label.setSizePolicy(sizePolicy)
        self.calib_label.setAutoFillBackground(False)
        self.calib_label.setScaledContents(False)
        self.calib_label.setAlignment(QtCore.Qt.AlignCenter)
        self.calib_label.setObjectName("calib_label")
        self.lay_params.addWidget(self.calib_label)
        self.calib_weight_spinbox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.calib_weight_spinbox.setObjectName("calib_weight_spinbox")
        self.lay_params.addWidget(self.calib_weight_spinbox)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 351, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LaySettingsAutoTest = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LaySettingsAutoTest.setContentsMargins(0, 0, 0, 0)
        self.LaySettingsAutoTest.setObjectName("LaySettingsAutoTest")
        self.LabelNumberItteration = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelNumberItteration.sizePolicy().hasHeightForWidth())
        self.LabelNumberItteration.setSizePolicy(sizePolicy)
        self.LabelNumberItteration.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelNumberItteration.setObjectName("LabelNumberItteration")
        self.LaySettingsAutoTest.addWidget(self.LabelNumberItteration)
        self.LabelComment = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.LabelComment.setObjectName("LabelComment")
        self.LaySettingsAutoTest.addWidget(self.LabelComment)
        self.scroll_area = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scroll_area.setEnabled(True)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 349, 349))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.LaySettingsAutoTest.addWidget(self.scroll_area)

        # Виджет внутри ScrollArea
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)
        self.LaySettingsAutoTest.addWidget(self.scroll_area)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.LaySettingsAutoTest.addWidget(self.pushButton)
        self.SaveBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SaveBut.setObjectName("SaveBut")
        self.LaySettingsAutoTest.addWidget(self.SaveBut)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 140, 291, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.lay_read_settings = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.lay_read_settings.setContentsMargins(0, 0, 0, 0)
        self.lay_read_settings.setSpacing(0)
        self.lay_read_settings.setObjectName("lay_read_settings")
        self.label_to_read = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_to_read.setAlignment(QtCore.Qt.AlignCenter)
        self.label_to_read.setObjectName("label_to_read")
        self.lay_read_settings.addWidget(self.label_to_read)
        self.T_flach_E = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_flach_E.sizePolicy().hasHeightForWidth())
        self.T_flach_E.setSizePolicy(sizePolicy)
        self.T_flach_E.setObjectName("T_flach_E")
        self.lay_read_settings.addWidget(self.T_flach_E)
        self.T_flash_O = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_flash_O.sizePolicy().hasHeightForWidth())
        self.T_flash_O.setSizePolicy(sizePolicy)
        self.T_flash_O.setObjectName("T_flash_O")
        self.lay_read_settings.addWidget(self.T_flash_O)
        self.Voltage = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Voltage.sizePolicy().hasHeightForWidth())
        self.Voltage.setSizePolicy(sizePolicy)
        self.Voltage.setObjectName("Voltage")
        self.lay_read_settings.addWidget(self.Voltage)
        self.ShuntVoltage = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShuntVoltage.sizePolicy().hasHeightForWidth())
        self.ShuntVoltage.setSizePolicy(sizePolicy)
        self.ShuntVoltage.setObjectName("ShuntVoltage")
        self.lay_read_settings.addWidget(self.ShuntVoltage)
        self.Temp = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Temp.sizePolicy().hasHeightForWidth())
        self.Temp.setSizePolicy(sizePolicy)
        self.Temp.setObjectName("Temp")
        self.lay_read_settings.addWidget(self.Temp)
        self.Traction = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Traction.sizePolicy().hasHeightForWidth())
        self.Traction.setSizePolicy(sizePolicy)
        self.Traction.setObjectName("Traction")
        self.lay_read_settings.addWidget(self.Traction)
        self.Weight = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Weight.sizePolicy().hasHeightForWidth())
        self.Weight.setSizePolicy(sizePolicy)
        self.Weight.setObjectName("Weight")
        self.lay_read_settings.addWidget(self.Weight)
        self.Weight_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Weight_1.sizePolicy().hasHeightForWidth())
        self.Weight_1.setSizePolicy(sizePolicy)
        self.Weight_1.setObjectName("Weight_1")
        self.lay_read_settings.addWidget(self.Weight_1)
        self.Weight_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Weight_2.sizePolicy().hasHeightForWidth())
        self.Weight_2.setSizePolicy(sizePolicy)
        self.Weight_2.setObjectName("Weight_2")
        self.lay_read_settings.addWidget(self.Weight_2)
        self.Time = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time.sizePolicy().hasHeightForWidth())
        self.Time.setSizePolicy(sizePolicy)
        self.Time.setObjectName("Time")
        self.lay_read_settings.addWidget(self.Time)
        self.gas = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gas.sizePolicy().hasHeightForWidth())
        self.gas.setSizePolicy(sizePolicy)
        self.gas.setObjectName("gas")
        self.lay_read_settings.addWidget(self.gas)
        self.gas_min = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gas_min.sizePolicy().hasHeightForWidth())
        self.gas_min.setSizePolicy(sizePolicy)
        self.gas_min.setObjectName("gas_min")
        self.lay_read_settings.addWidget(self.gas_min)
        self.gas_max = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gas_max.sizePolicy().hasHeightForWidth())
        self.gas_max.setSizePolicy(sizePolicy)
        self.gas_max.setObjectName("gas_max")
        self.lay_read_settings.addWidget(self.gas_max)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.text_change_step_5.setText(_translate("Form", "Изменить шаг подачи газа"))
        self.calib_label.setText(_translate("Form", "Изменить калибровочный вес"))
        self.LabelNumberItteration.setText(_translate("Form", "Настройка автотеста"))
        self.LabelComment.setText(_translate("Form", "                   Газ в %                        время в с."))
        self.pushButton.setText(_translate("Form", "+"))
        self.SaveBut.setText(_translate("Form", "сохранить"))
        self.label_to_read.setText(_translate("Form", "Данные для чтения выделите галочкой"))
        self.T_flach_E.setText(_translate("Form", "T_flach_E"))
        self.T_flash_O.setText(_translate("Form", "T_flash_O"))
        self.Voltage.setText(_translate("Form", "Voltage"))
        self.ShuntVoltage.setText(_translate("Form", "ShuntVoltage"))
        self.Temp.setText(_translate("Form", "Temp"))
        self.Traction.setText(_translate("Form", "Traction"))
        self.Weight.setText(_translate("Form", "Weight"))
        self.Weight_1.setText(_translate("Form", "Weight_1"))
        self.Weight_2.setText(_translate("Form", "Weight_2"))
        self.Time.setText(_translate("Form", "Time"))
        self.gas.setText(_translate("Form", "gas"))
        self.gas_min.setText(_translate("Form", "gas_min"))
        self.gas_max.setText(_translate("Form", "gas_max"))

        self.T_flash_O.isChecked()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.create_time_point)
        self.SaveBut.clicked.connect(self.save_values)

        self.calib_weight_spinbox.valueChanged.connect(self.change_weight)
        self.spinbox_change_step.valueChanged.connect(self.change_step)

        self.values = {} # тут хранятся значения газ,время
        self.points = {} # тут упорядочный словарь по индексу в котором хронятся значения

        # путь сохранения для автотеста
        self.name_file = "timings.json"
        self.full_path = os.path.join(json_dir, self.name_file)

        # путь сохранения для чтения параметров
        self.name_file_ToRead = "ToRead.json"
        self.full_path_ToRead = os.path.join(json_dir,self.name_file_ToRead)

        create_json(name_file=self.name_file,data=self.values)

        # Список для хранения чекбоксов
        self.checkboxes = self.get_all_checkboxes_from_layout(self.lay_read_settings)

        # подключаем события
        self.connect_checkboxes()

        # устанавливаем состояние чекбоксов
        self.load_state_check_box()

    def create_time_point(self):
        # Создаём новый слой с двумя SpinBox
        layer_widget = QtWidgets.QWidget(self.scroll_widget)
        layer_widget.setFixedHeight(50)  # Фиксированная высота
        layer_layout = QtWidgets.QHBoxLayout(layer_widget)

        spinBox_gas = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        spinBox_gas.setRange(0, 10000)
        spinBox_gas.setObjectName("spinBox_1")

        spinBox_time = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        spinBox_time.setRange(0, 100000)
        spinBox_time.setObjectName("spinBox_2")

        #добавляем в словарь
        self.values[spinBox_gas] = spinBox_time

        #Настраиваем позицию элементов
        layer_widget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        spinBox_gas.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        spinBox_time.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        layer_layout.addWidget(spinBox_gas)
        layer_layout.addWidget(spinBox_time)

        # Добавляем новый слой в основной макет
        self.scroll_layout.addWidget(layer_widget)

    def save_values(self):

        for index, (gas, time) in enumerate(self.values.items()):
            # Формируем структуру для текущей пары gas и time
            self.points[f"Number operation {index}"] = {
                gas.value(): time.value() * 1000
            }

            # Вывод текущих данных
            print(f"Индекс: {index}, значение газа (x): {gas.value()}, значение времени (y): {time.value()}")

        # Экспортируем итоговый JSON , если таковой имеется то удаляем
        if os.path.isfile(self.full_path):  # Проверяем, существует ли файл по указанному пути
            try:
                os.remove(self.full_path)  # Удаляем файл
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        create_json("timings.json", self.points)

    def change_weight(self):
        globals.calib_weight = self.calib_weight_spinbox.value()

    # изменение шага в процентах
    def change_step(self):
        step_size = self.spinbox_change_step.value()
        gas_min,gas_max = import_from_json("save_file.json","gas_min","gas_max")
        globals.step_size = (gas_max - gas_min) // step_size

    # Метод для фильтрации только чекбоксов
    def get_all_checkboxes_from_layout(self, layout):
        checkboxes = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            # Если это виджет и это QCheckBox
            if item.widget() and isinstance(item.widget(), QCheckBox):
                checkboxes.append(item.widget())
            # Если это вложенный слой
            elif item.layout():
                checkboxes.extend(self.get_all_checkboxes_from_layout(item.layout()))
        return checkboxes

    # подключаем события к чекбоксам
    def connect_checkboxes(self):
        for box in self.checkboxes:
            box.stateChanged.connect(self.save_state_check_box)

    # сохраняем состояние чекбокса
    def save_state_check_box(self, state):
        sender = self.sender()  # Определяем, какой чекбокс отправил сигнал
        if sender:
            # Сохраняем состояние чекбокса в JSON
            data = {}
            data[sender.text()] = sender.isChecked()
            export_to_json(self.full_path_ToRead, **data)

    # подгружаем из json файла состояние кнопок на последний момент при запуске программы
    def load_state_check_box(self):
        if os.path.isfile(self.full_path_ToRead):
            try:
                data = import_js(self.full_path_ToRead)
                for name, state in data.items():
                    for box in self.checkboxes:
                        if name == box.text():
                            if state:
                                box.setChecked(True)
                            else:
                                box.setChecked(False)
            except Exception as e:
                print(e)
        else:
            pass

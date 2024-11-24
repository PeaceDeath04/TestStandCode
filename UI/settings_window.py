from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from UI.Window import Ui_MainWindow
from data_processing.Data import export_to_json,create_json
import sys


class SettingsWindow(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(719, 535)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
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
        self.scroll_area = QtWidgets.QScrollArea(self.verticalLayoutWidget)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 347, 402))
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
        self.SaveBut = QtWidgets.QPushButton(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.SaveBut.setFont(font)

        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setIconSize(QtCore.QSize(16,16))

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setObjectName("SaveBut")

        self.LaySettingsAutoTest.addWidget(self.pushButton)
        self.LaySettingsAutoTest.addWidget(self.SaveBut)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text_change_step_5.setText(_translate("Form", "Изменить шаг подачи газа"))
        self.calib_label.setText(_translate("Form", "Изменить калибровочный вес"))
        self.LabelNumberItteration.setText(_translate("Form", "Настройка автотеста"))
        self.pushButton.setText(_translate("Form", "+"))
        self.SaveBut.setText(_translate("Form","Сохранить"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_time_point)
        self.SaveBut.clicked.connect(self.save_values)

        self.values = {} # тут хранятся значения газ,время
        self.points = {} # тут упорядочный словарь по индексу в котором хронятся значения

        create_json(name_file="timings.json",data=self.values)

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
                "gas on percent": gas.value(),
                "wait time": time.value()
            }

            # Вывод текущих данных
            print(f"Индекс: {index}, значение газа (x): {gas.value()}, значение времени (y): {time.value()}")

        # Экспортируем итоговый JSON
        export_to_json("timings.json", **self.points)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets


class SettingsWindow(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1540, 833)
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
        self.layoutWidget.setGeometry(QtCore.QRect(790, 70, 189, 47))
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
        self.layoutWidget_2.setGeometry(QtCore.QRect(790, 10, 220, 47))
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 349, 347))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.LaySettingsAutoTest.addWidget(self.scroll_area)

        # Виджет внутри ScrollArea
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)
        self.LaySettingsAutoTest.addWidget(self.scroll_area)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ButDeletePoint = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButDeletePoint.setObjectName("ButDeletePoint")
        self.horizontalLayout_2.addWidget(self.ButDeletePoint)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.LaySettingsAutoTest.addLayout(self.horizontalLayout_2)
        self.SaveBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SaveBut.setObjectName("SaveBut")
        self.LaySettingsAutoTest.addWidget(self.SaveBut)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(790, 130, 291, 331))
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(390, 10, 351, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.LaySettingsAutoTest_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.LaySettingsAutoTest_2.setContentsMargins(0, 0, 0, 0)
        self.LaySettingsAutoTest_2.setObjectName("LaySettingsAutoTest_2")
        self.NameTable = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameTable.sizePolicy().hasHeightForWidth())
        self.NameTable.setSizePolicy(sizePolicy)
        self.NameTable.setAlignment(QtCore.Qt.AlignCenter)
        self.NameTable.setObjectName("NameTable")
        self.LaySettingsAutoTest_2.addWidget(self.NameTable)
        self.LabelComment_Graphs = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.LabelComment_Graphs.setObjectName("LabelComment_Graphs")
        self.LaySettingsAutoTest_2.addWidget(self.LabelComment_Graphs)
        self.scroll_area_2 = QtWidgets.QScrollArea(self.verticalLayoutWidget_3)
        self.scroll_area_2.setEnabled(True)
        self.scroll_area_2.setWidgetResizable(True)
        self.scroll_area_2.setObjectName("scroll_area_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 349, 347))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scroll_area_2.setWidget(self.scrollAreaWidgetContents_3)
        self.LaySettingsAutoTest_2.addWidget(self.scroll_area_2)

        # Виджет внутри настройки графиков
        self.scroll_widget_graphs = QtWidgets.QWidget()
        self.scroll_layout_graphs = QtWidgets.QVBoxLayout(self.scroll_widget_graphs)
        self.scroll_layout_graphs.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area_2.setWidget(self.scroll_widget_graphs)
        self.LaySettingsAutoTest_2.addWidget(self.scroll_area_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.But_AddGraph = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.But_AddGraph.setFont(font)
        self.But_AddGraph.setIconSize(QtCore.QSize(16, 16))
        self.But_AddGraph.setObjectName("But_AddGraph")
        self.horizontalLayout_3.addWidget(self.But_AddGraph)
        self.LaySettingsAutoTest_2.addLayout(self.horizontalLayout_3)
        self.But_SaveGraphs = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.But_SaveGraphs.setObjectName("But_SaveGraphs")
        self.LaySettingsAutoTest_2.addWidget(self.But_SaveGraphs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text_change_step_5.setText(_translate("Form", "Изменить шаг подачи газа"))
        self.calib_label.setText(_translate("Form", "Изменить калибровочный вес"))
        self.LabelNumberItteration.setText(_translate("Form", "Настройка автотеста"))
        self.LabelComment.setText(_translate("Form", "                   Газ в %                        время в с."))
        self.ButDeletePoint.setText(_translate("Form", "-"))
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
        self.NameTable.setText(_translate("Form", "Настройка графиков"))
        self.LabelComment_Graphs.setText(_translate("Form", "                   Ось X                        Ось Y."))
        self.pushButton_2.setText(_translate("Form", "-"))
        self.But_AddGraph.setText(_translate("Form", "+"))
        self.But_SaveGraphs.setText(_translate("Form", "сохранить"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Aidy"))
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
        self.setupUi(self)
from UI import SettingsWindow,MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QComboBox
from JsonHandler import *

class UiController:
    def __init__(self,controller):
        # ui (обертка главного окна)
        self.ui_main = MainWindow()

        # ui (обертка окна настроек)
        self.ui_settings = SettingsWindow()


        # получаем существующий экземпляр класса главного контроллера
        self.controller = controller

        # Список для хранения чекбоксов ( чекбоксами являются ui элементы при нажатии которых выбранный параметр (Traction,Weight...) будет отображается в exel таблицах)
        self.checkboxes = self.get_all_checkboxes_from_layout(self.ui_settings.lay_read_settings)

        # шаг изменения ползунка слайдера в процентах
        self.step_size = 1

        # отображение главного окна
        self.ui_main.show()

        # для работы с автотестом
        self.values = {}  # тут хранятся значения газ,время
        self.points = {}  # тут упорядочный словарь по индексу в котором хронятся значения

        # ключи графиков ( используется для списка возможных отображений графика по выбранной оси)
        self.keys_to_graph = ["T_flach_E", "T_flash_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight","Weight_1","Weight_2", "Time"]

        # хранит в себе ключ значние где ключ это QWidget для оси x аналогично по оси y (self.graphs[comboBox_x] = comboBox_y)
        self.graphs = {}

        # хранит в себе последнее значение газа для послед определения в большую или меньшую часть изменилось
        self.last_value_gas = None

    def clear_layout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def OnStartUp(self):
        # это максимальное число которое можно будет ввести
        max_value = 1000000

        #вводим максимальное значение для ввода
        self.ui_main.spinBoxMin.setMaximum(max_value)
        self.ui_main.spinBoxMax.setMaximum(max_value)

        self.ui_settings.calib_weight_spinbox.setMaximum(max_value)

        self.load_graphs()
        self.save_graphs()

        self.load_calib_weight()

        self.load_state_check_box()

        self.load_time_point()

        self.load_offset_gas()

        self.ui_main.SlidePower.setValue(self.ui_main.spinBoxMin.value())

        # подключаем события у главного окна
        self.connect_events_main()

        # подключаем события для окна настроек
        self.connect_events_settings()
        self.load_step_size()

    #region Работа с портами

    def toggle_port(self):
        is_open = self.controller.open_port(self.ui_main.ListPorts.currentText())
        if is_open:
            self.ui_main.ButOpenPort.setText("Закрыть порт")
        else:
            self.ui_main.ButOpenPort.setText("Открыть порт")

    def refresh_port_list(self):
        self.ui_main.ListPorts.clear()
        ports = self.controller.update_port_list()
        self.ui_main.ListPorts.addItems(ports)

    #endregion

    #regionработа с газом

    def range_gas_changed(self):
        gas_min, gas_max = self.ui_main.spinBoxMin.value(), self.ui_main.spinBoxMax.value()
        if gas_min >= gas_max:
            return
        self.controller.offset_gas_changed(gas_min=gas_min,gas_max=gas_max)

    def gas_changed(self):
        current_value = self.ui_main.SlidePower.value()
        current_value = (current_value * 100) // self.step_size
        print(self.get_value_from_percentage(current_value))

        self.controller.gas_changed(current_value)

    def get_value_from_percentage(self, percent):
        """Вычисляет значение газа на основе процента"""
        # Получаем минимальное и максимальное значения диапазона
        gas_min = self.ui_main.spinBoxMin.value()
        gas_max = self.ui_main.spinBoxMax.value()

        try:
            # Проверка, чтобы диапазон был корректным
            if gas_max == gas_min:
                raise ValueError("Диапазон некорректный: минимальное и максимальное значение равны")

            # Вычисляем значение газа
            gas = gas_min + (percent / 100) * (gas_max - gas_min)
            return round(gas)

        except Exception as e:
            return f"Ошибка при вычислении значения: {e}"

    def load_offset_gas(self):
        offset_gas = import_from_json("save_file.json", "gas_min", "gas_max")
        self.ui_main.spinBoxMin.setValue(offset_gas[0])
        self.ui_main.spinBoxMax.setValue(offset_gas[1])
    #endregion

    #regionработа с событиями

    def connect_events_main(self):
        """Подключение событий для главного окна"""

        # подключение по работе с газом
        self.ui_main.spinBoxMin.valueChanged.connect(self.range_gas_changed)
        self.ui_main.spinBoxMax.valueChanged.connect(self.range_gas_changed)
        self.ui_main.SlidePower.sliderMoved.connect(self.gas_changed)

        # подключение работы с портом
        self.ui_main.ButOpenPort.clicked.connect(self.toggle_port)
        self.ui_main.butRefresh.clicked.connect(self.refresh_port_list)

        # подключение показа настройки
        self.ui_main.ActionSettings.triggered.connect(self.ui_settings.show)

        # подключение работы автотеста
        self.ui_main.ButAutoTest.clicked.connect(self.controller.start_auto_test)

        # подключение записи параметров
        self.ui_main.ButSaveExl.clicked.connect(self.controller.switch_recording)

        # подключение настроек тарирования
        self.ui_main.ButTarTraction.clicked.connect(lambda :self.controller.set_value_for_taring(key_param="Traction"))
        self.ui_main.ButTarWeight.clicked.connect(lambda :self.controller.set_value_for_taring(key_param="Weight"))

        # подключение настроек калибровки
        self.ui_main.ButCalib.clicked.connect(lambda :self.controller.transceiver.send_data(ButCalibMotor=0))
        self.ui_main.ButCalibTraction.clicked.connect(lambda :self.controller.set_value_for_calib(key_param="Traction"))
        self.ui_main.ButCalibWeight.clicked.connect(lambda :self.controller.set_value_for_calib(key_param="Weight"))

    def connect_events_settings(self):
        # подключение по созданию временной точки автотеста
        self.ui_settings.pushButton.clicked.connect(self.create_time_point)  # кнопка + при создании точки

        # подключаем сохранение точек в json
        self.ui_settings.SaveBut.clicked.connect(self.save_values)

        # подключаем удаление последней временной точки в автотесте
        self.ui_settings.ButDeletePoint.clicked.connect(self.remove_last_spinbox_layer)

        # подключаем обновление калибровочного веса
        self.ui_settings.calib_weight_spinbox.valueChanged.connect(self.change_weight)

        # подключаем обновление шага ползунка слайдера в процентах
        self.ui_settings.spinbox_change_step.valueChanged.connect(self.change_step)

        self.ui_settings.But_AddGraph.clicked.connect(self.create_graph)
        self.ui_settings.But_SaveGraphs.clicked.connect(self.save_graphs)
        self.ui_settings.pushButton_2.clicked.connect(self.remove_last_graph_layer)
    #endregion

    #region Настройка Автотеста

    def create_time_point(self):
        # Создаём новый слой с двумя SpinBox
        layer_widget = QtWidgets.QWidget(self.ui_settings.scroll_widget)
        layer_widget.setFixedHeight(50)  # Фиксированная высота
        layer_layout = QtWidgets.QHBoxLayout(layer_widget)

        spinBox_gas = QtWidgets.QSpinBox(self.ui_settings.verticalLayoutWidget)
        spinBox_gas.setRange(0, 10000)
        spinBox_gas.setObjectName("spinBox_1")

        spinBox_time = QtWidgets.QSpinBox(self.ui_settings.verticalLayoutWidget)
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
        self.ui_settings.scroll_layout.addWidget(layer_widget)

    def save_values(self):

        for index, (gas, time) in enumerate(self.values.items()):
            # Формируем структуру для текущей пары gas и time
            self.points[f"Number operation {index}"] = {
                gas.value(): time.value() * 1000
            }

        # Экспортируем итоговый JSON , если таковой имеется то удаляем
        if os.path.isfile(path_timings):  # Проверяем, существует ли файл по указанному пути
            try:
                os.remove(path_timings)  # Удаляем файл
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        create_json("timings.json", self.points)

    def load_time_point(self):
        if not os.path.exists(path_timings):
            return
        data = import_js("timings.json")

        if data is None:
            return

        for i in range(len(data)):
            self.create_time_point()

        gas_percents = []
        time_ms = []

        for point in data.values():
            for gas,time in point.items():
                gas_percents.append(int(gas))
                time_ms.append(time//1000)

        for percent,wait in self.values.items():
            percent.setValue(gas_percents[0])
            wait.setValue(time_ms[0])

            gas_percents.pop(0)
            time_ms.pop(0)

    # удаление последней точки автотеста в ui
    def remove_last_spinbox_layer(self):
        if self.values:  # Проверяем, есть ли слои для удаления
            # Получаем последний добавленный элемент
            last_spinBox_gas = list(self.values.keys())[-1]
            last_spinBox_time = self.values[last_spinBox_gas]

            # Удаляем виджеты из макета
            for i in range(self.ui_settings.scroll_layout.count() - 1, -1, -1):
                item = self.ui_settings.scroll_layout.itemAt(i).widget()
                if item and last_spinBox_gas in item.children() and last_spinBox_time in item.children():
                    self.ui_settings.scroll_layout.removeWidget(item)
                    item.deleteLater()  # Удаляем виджет
                    break

            # Удаляем элемент из словаря
            del self.values[last_spinBox_gas]
        else:
            print("Нет слоёв с SpinBox для удаления.")

    #endregion

    # region Настройка читаемых параметров

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
            export_to_json("ToRead.json", **data)

    # подгружаем из json файла состояние кнопок на последний момент при запуске программы
    def load_state_check_box(self):
        if os.path.isfile(path_ToRead):
            try:
                data = import_js(path_ToRead)
                for name, state in data.items():
                    for box in self.checkboxes:
                        if name == box.text():
                            if state:
                                box.setChecked(True)
                            else:
                                box.setChecked(False)
            except Exception as e:
                print("файл с чекбоксами найден , но не имеет элементов. Exception:",e)

    #endregion

    #region изменение переменных на прямую

    # Изменение калибровочного веса
    def change_weight(self):
        self.controller.local_data.calib_weight = self.ui_settings.calib_weight_spinbox.value()

    def load_calib_weight(self):
        try:
            self.controller.local_data.calib_weight = import_from_json("save_file.json", "calib_weight")[0]
            self.ui_settings.calib_weight_spinbox.setValue(self.controller.local_data.calib_weight)
        except Exception as e:
            print(f"Ошибка при загрузке калибровочного веса , текст ошибки: {e}")

    # изменение шага в процентах
    def change_step(self):
        self.step_size = 100 // self.ui_settings.spinbox_change_step.value()
        print(self.step_size)
        self.ui_main.SlidePower.setMaximum(self.step_size)

    def load_step_size(self):
        self.ui_settings.spinbox_change_step.setValue(import_from_json("save_file.json","step_size")[0])

    #endregion

    # region Настройка графиков

    def load_graphs(self):
        if os.path.isfile(full_path_ToGraphs):
            try:
                data = import_js(full_path_ToGraphs)

                # извлекаем из словаря json параметры и создаем combobox на их основе которые передаем в self.graphs
                for name, graph in data.items():
                    comboBox_graphs = []

                    for key, value in graph.items():

                        if key == "x":
                            comboBox_x = QtWidgets.QComboBox(self.ui_settings.verticalLayoutWidget_3)
                            comboBox_x.setObjectName("comboBox_x")
                            comboBox_x.addItems(self.keys_to_graph)
                            comboBox_x.setCurrentText(value)
                            comboBox_graphs.append(comboBox_x)

                        else:
                            comboBox_y = QtWidgets.QComboBox(self.ui_settings.verticalLayoutWidget_3)
                            comboBox_y.setObjectName("comboBox_y")
                            comboBox_y.addItems(self.keys_to_graph)
                            comboBox_y.setCurrentText(value)
                            comboBox_graphs.append(comboBox_y)

                    self.graphs[comboBox_graphs[0]] = comboBox_graphs[1]

                # добавляем на слой
                for x, y in self.graphs.items():
                    # Создаём новый слой с двумя SpinBox
                    layer_widget = QtWidgets.QWidget(self.ui_settings.scroll_widget_graphs)
                    layer_widget.setFixedHeight(50)  # Фиксированная высота
                    layer_layout = QtWidgets.QHBoxLayout(layer_widget)

                    # Настраиваем позицию элементов
                    layer_widget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                    x.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                    y.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

                    layer_layout.addWidget(x)
                    layer_layout.addWidget(y)

                    # Добавляем новый слой в основной макет
                    self.ui_settings.scroll_layout_graphs.addWidget(layer_widget)

            except Exception as e:
                print(e)

    def create_graph(self):
        # Создаём новый слой с двумя SpinBox
        layer_widget = QtWidgets.QWidget(self.ui_settings.scroll_widget_graphs)
        layer_widget.setFixedHeight(50)  # Фиксированная высота
        layer_layout = QtWidgets.QHBoxLayout(layer_widget)

        comboBox_x = QtWidgets.QComboBox(self.ui_settings.verticalLayoutWidget_3)
        comboBox_x.setObjectName("comboBox_x")

        comboBox_y = QtWidgets.QComboBox(self.ui_settings.verticalLayoutWidget_3)
        comboBox_y.setObjectName("comboBox_y")

        # начальный текст
        comboBox_x.addItem("Выберите параметр X")
        comboBox_x.model().item(0).setEnabled(False)  # Отключение выбора первого элемента
        # добавляем ключи
        comboBox_x.addItems(self.keys_to_graph)

        # начальный текст
        comboBox_y.addItem("Выберите параметр Y")
        comboBox_y.model().item(0).setEnabled(False)  # Отключение выбора первого элемента
        # добавляем ключи
        comboBox_y.addItems(self.keys_to_graph)

        self.graphs[comboBox_x] = comboBox_y

        # Настраиваем позицию элементов
        layer_widget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        comboBox_x.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        comboBox_y.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        layer_layout.addWidget(comboBox_x)
        layer_layout.addWidget(comboBox_y)

        # Добавляем новый слой в основной макет
        self.ui_settings.scroll_layout_graphs.addWidget(layer_widget)

    def save_graphs(self):
        if self.graphs:
            self.controller.graph_controller.graphs.clear()
            if os.path.isfile(full_path_ToGraphs):
                os.remove(full_path_ToGraphs)
            data = {}
            for x, y in self.graphs.items():
                if isinstance(x, QtWidgets.QComboBox) and isinstance(y, QtWidgets.QComboBox):
                    name = f"{x.currentText()} / {y.currentText()}"
                    data[name] = {"x": x.currentText(), "y": y.currentText()}

                    # добавляем в список графиков
                    self.controller.graph_controller.create_graph(name, x.currentText(), y.currentText())

            # сохраняем в json
            create_json("keys_graphs.json", data)

            # обновляем в ui список графиков
            self.controller.update_graphs_widget()

    def remove_last_graph_layer(self):
        if self.graphs:  # Проверяем, есть ли слои для удаления
            # Получаем последний добавленный элемент
            last_combo_x = list(self.graphs.keys())[-1]
            last_combo_y = self.graphs[last_combo_x]

            # Удаляем виджеты из макета
            for i in range(self.ui_settings.scroll_layout_graphs.count() - 1, -1, -1):
                item = self.ui_settings.scroll_layout_graphs.itemAt(i).widget()
                if item and last_combo_x in item.children() and last_combo_y in item.children():
                    self.ui_settings.scroll_layout_graphs.removeWidget(item)
                    item.deleteLater()  # Удаляем виджет
                    break

            # Удаляем элемент из словаря
            del self.graphs[last_combo_x]
        else:
            print("Нет графиков для удаления.")

    # endregion







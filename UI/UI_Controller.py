import controller
from controller import Controller
from .UI import SettingsWindow,MainWindow

class UiController:
    def __init__(self,controller):
        self.ui_main = MainWindow()
        self.ui_settings = SettingsWindow()

        self.controller = controller

        self.setup_ui()

        # стиль ui
        self.styleSheet = ("QWidget {\n"
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

        self.step_size = 1

    def setup_ui(self):
        self.ui_main.setupUi(self.ui_main)
        self.ui_settings.setupUi(self.ui_settings)

    def add_graph(self):
        """Метод для добавления обьекта класса Graph на ui слой в главном окне"""

    """Работа с портами"""

    def toggle_port(self):
        is_open = self.controller.open_port(self.ui_main.ListPorts.currentText())
        if is_open:
            self.ui_main.ButOpenPort.setText("Закрыть")
        else:
            self.ui_main.ButOpenPort.setText("Открыть")

    def refresh_port_list(self):
        self.ui_main.ListPorts.clear()
        ports = self.controller.update_port_list()
        self.ui_main.ListPorts.addItems(ports)

    """#работа с газом"""

    def range_gas_changed(self):
        gas_min, gas_max = self.ui_main.spinBoxMin.value(), self.ui_main.spinBoxMax.value()
        if gas_min >= gas_max:
            return

        self.ui_main.SlidePower.setMinimum(gas_min)
        self.ui_main.SlidePower.setMaximum(gas_max)
        self.ui_main.SlidePower.setValue(gas_min)

        self.controller.transceiver.send_data(gas_min=gas_min, gas_max=gas_max)

    def gas_changed(self):
        current_value = self.ui_main.SlidePower.value()
        adjusted_value = self.calculate_step_value(current_value)
        self.ui_main.SlidePower.blockSignals(True)
        self.ui_main.SlidePower.setValue(adjusted_value)
        self.ui_main.SlidePower.blockSignals(False)
        self.controller.transceiver.send_data(gas=adjusted_value)

        gas_percent = self.get_gas_percentage()
        self.ui_main.valueGas.setText(f"Значение газа в процентах: {gas_percent}    Численное значние: {adjusted_value}")

    def calculate_step_value(self, current_value):
        """Рассчитывает ближайшее значение шага для слайдера"""
        gas_min = self.ui_main.spinBoxMin.value()
        gas_max = self.ui_main.spinBoxMax.value()
        step_size = self.step_size

        range_size = gas_max - gas_min
        step_value = range_size * step_size / 100

        # Найти ближайший шаг
        lower_bound = (current_value // step_value) * step_value
        upper_bound = lower_bound + step_value

        # Определить, к какому шагу ближе
        if abs(current_value - lower_bound) < abs(current_value - upper_bound):
            return round(lower_bound + gas_min)
        else:
            return round(upper_bound + gas_min)

    def get_gas_percentage(self):
        """Узнает текущее значение газа в процентах"""
        gas_min,gas,gas_max = self.ui_main.spinBoxMin.value(),self.ui_main.SlidePower.value(),self.ui_main.spinBoxMax.value()
        try:
            per = ((gas - gas_min) / (gas_max - gas_min)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    """работа с событиями"""

    def connect_events_main(self):
        """Подключение событий для главного окна"""

        # подключение по работе с газом
        self.ui_main.spinBoxMin.valueChanged.connect(self.range_gas_changed)
        self.ui_main.spinBoxMax.valueChanged.connect(self.range_gas_changed)
        self.ui_main.SlidePower.valueChanged.connect(self.gas_changed)

        # подключение работы с портом
        self.ui_main.ButOpenPort.clicked.connect(self.toggle_port)
        self.ui_main.butRefresh.clicked.connect(self.refresh_port_list)

        # подключение показа настройки
        self.ui_main.ActionSettings.triggered.connect(self.ui_settings.show)

        # подключение работы автотеста
        self.ui_main.ButAutoTest.clicked.connect("Нажата кнопка автотеста")

        # подключение записи параметров
        self.ui_main.ButSaveExl.clicked.connect("Начать запись параметров")

        # подключение настроек тарирования
        self.ui_main.ButTarTraction.clicked.connect("Нажата кнопка тарирования Traction")
        self.ui_main.ButTarWeight.clicked.connect("Нажата кнопка тарирования веса")

        # подключение настроек калибровки
        self.ui_main.ButCalib.clicked.connect(lambda :self.controller.transceiver.send_data(ButCalibMotor=0))
        self.ui_main.ButCalibTraction.clicked.connect("Нажата кнопка калибровки Traction")
        self.ui_main.ButCalibWeight.clicked.connect("Нажата кнопка калибрвоки веса")

    def connect_events_settings(self):
        pass





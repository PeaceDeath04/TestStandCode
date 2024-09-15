from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from saving import JsonHandler
import traceback
from ProjectProcessing import processing
import numpy as np
import datetime as dt
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Класс для таблицы с данными X, Y
class Table:
    def __init__(self, parent=None, max_points=100):
        self.fig = Figure()  # Создаем объект Figure для графика
        self.canvas = FigureCanvas(self.fig)  # Холст для графика
        self.ax = self.fig.add_subplot(111)  # Добавляем ось

        self.x_data = []  # Данные по оси X
        self.y_data = []  # Данные по оси Y
        self.max_points = max_points  # Максимальное количество точек на графике

        # Настройка осей графика
        self.ax.set_xlabel('X Axis')
        self.ax.set_ylabel('Y Axis')
        self.line, = self.ax.plot([], [], label='Data', marker='o', linestyle='-')  # Линия на графике с маркерами
        self.ax.legend()

    def add_data(self, x, y):
        """Добавляем данные в график и обновляем его"""
        self.x_data.append(x)
        self.y_data.append(y)

        # Ограничиваем количество точек до max_points (например, 100)
        if len(self.x_data) > self.max_points:
            self.x_data = self.x_data[-self.max_points:]
            self.y_data = self.y_data[-self.max_points:]

        self.update_graph()

    def update_graph(self):
        """Обновляем график"""
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()  # Обновляем лимиты осей
        self.ax.autoscale_view()  # Масштабируем график
        self.canvas.draw()  # Перерисовываем график

# Класс с таймером для обновления оси X (время)
class TableWithTimer(Table):
    def __init__(self, interval=1, parent=None, max_points=50):
        super().__init__(parent, max_points)
        self.start_time = dt.datetime.now()  # Начальное время
        self.timer = QTimer()  # Создаем таймер для обновления X
        self.timer.setInterval(interval)  # Интервал обновления в миллисекундах
        self.timer.timeout.connect(self._update_x)  # Подключаем таймер к функции обновления
        self.timer.start()
        self.save = JsonHandler()

    def _update_x(self):
        """Обновляем ось X временем и вызываем обновление графика"""
        elapsed_time = (dt.datetime.now() - self.start_time).total_seconds()  # Время от старта
        new_y = self.save.import_from_json("Traction")  # Случайное значение для Y
        self.add_data(elapsed_time, new_y)  # Добавляем данные на график

    def update_y(self, new_y):
        """Метод для обновления значения по оси Y вручную"""
        elapsed_time = (dt.datetime.now() - self.start_time).total_seconds()
        self.add_data(elapsed_time, new_y)


class Controller:
    def __init__(self, log_function=None):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.buffer = ""
        self.log_function = log_function
        self.processing = processing(self.serial)
        self.save = JsonHandler()

        self.table_with_timer = TableWithTimer(interval=1, max_points=50)  # Показывать только 50 последних точек
        #self.graph_Layout.addWidget(self.table_with_timer.canvas)  # Добавляем холст графика в окно

    def open_port(self, port_name):
        # Закрываем текущий порт, если он открыт
        if self.serial.isOpen():
            if self.serial.portName() != port_name:
                self.serial.close()
                print(f"Закрытие порта {self.serial.portName()} перед открытием нового")

        # Устанавливаем и открываем новый порт
        self.serial.setPortName(port_name)
        if self.serial.open(QIODevice.ReadWrite):
            return f"Порт {port_name} открыт"
        else:
            return f"Не удалось открыть порт {port_name} , т.к он уже используется"

    def close_port(self):
        if self.serial.isOpen():
            self.serial.close()
            return "Порт закрыт"
        return "Порт уже закрыт"

    def update_port_list(self):
        ports = QSerialPortInfo.availablePorts()
        return [port.portName() for port in ports]

    def read_data(self):
        try:
            rx = self.serial.readAll()
            rxs = str(rx, 'utf-8', errors='ignore')
            self.buffer += rxs

            if ';' in self.buffer:
                packets = self.buffer.split(';')
                for packet in packets[:-1]:
                    if packet:
                        data = packet.strip().split(",")
                        if all(item != '' for item in data):
                            self.save.ardu_to_json(data)
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc()

    def get_gas_percentage(self):
        try:
            a = self.save.import_from_json("gas_min")
            b = self.save.import_from_json("gas_max")
            c = self.save.import_from_json("gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"


"""
    def set_gas_range(self, gas_min, gas_max):
        self.save.export_to_json("gas_min", gas_min)
        self.save.export_to_json("gas_max", gas_min)

            gas_min = self.save.import_from_json("gas_min", self.log_function)
            gas_max = self.save.import_from_json("gas_max", self.log_function)
            gas =     self.save.import_from_json("gas", self.log_function)
            return round((gas - gas_min) / (gas_max - gas_min) * 100)
        except:
            return "Ошибка при вычислении"

"""
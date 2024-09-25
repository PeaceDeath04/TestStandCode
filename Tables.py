import numpy as np
import datetime as dt
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Graph:
    def __init__(self, parent=None, max_points=25):
        self.fig = Figure()  # Создаем объект Figure для графика
        self.canvas = FigureCanvas(self.fig)  # Холст для графика
        self.ax = self.fig.add_subplot(111)  # Добавляем ось

        self.x_data = []  # Данные по оси X
        self.y_data = []  # Данные по оси Y
        self.max_points = max_points  # Максимальное количество точек на графике

        # Настройка осей графика
        self.ax.set_xlabel('Время')
        self.ax.set_ylabel('Значения')
        self.line, = self.ax.plot([], [], label="название", marker='o', linestyle='-')  # Линия на графике с маркерами
        self.ax.legend()

    def add_data(self, x, y,name):
        """Добавляем данные в график и обновляем его"""
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_label(name)
        self.ax.legend(loc='upper right')

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
class GraphWithTimer(Graph):
    def __init__(self, interval=1, parent=None, max_points=50):
        super().__init__(parent, max_points)
        self.start_time = dt.datetime.now()  # Начальное время
        self.timer = QTimer()  # Создаем таймер для обновления X
        self.timer.setInterval(interval)  # Интервал обновления в миллисекундах
        self.timer.timeout.connect(self._update_x)  # Подключаем таймер к функции обновления
        self.timer.start()
        #self.save = JsonHandler()

    def _update_x(self):
        """Обновляем ось X временем и вызываем обновление графика"""
        elapsed_time = (dt.datetime.now() - self.start_time).total_seconds()  # Время от старта
        #new_y = self.save.import_local_data("Traction")  # Случайное значение для Y
        #self.add_data(elapsed_time, new_y)  # Добавляем данные на график

    def update_y(self, new_y):
        """Метод для обновления значения по оси Y вручную"""
        elapsed_time = (dt.datetime.now() - self.start_time).total_seconds()
        self.add_data(elapsed_time, new_y)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib import rcParams

#print(plt.style.available)
plt.style.use('seaborn-v0_8-dark')


class Graph:
    def __init__(self, parent=None, max_points=25):
        self.fig = Figure()  # Создаем объект Figure для графика
        self.canvas = FigureCanvas(self.fig)  # Холст для графика
        self.ax = self.fig.add_subplot(111)  # Добавляем ось
        self.fig.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Настройка полей
        self.fig.patch.set_alpha(0)  # Убираем фон самой фигуры (белое вокруг графика)
        self.ax.set_facecolor('none')  # Убираем фон графика (области внутри осей)

        # Настройки стиля для темной темы и жирного текста легенды
        rcParams['figure.facecolor'] = '#2c3e50'  # Цвет фона фигуры
        rcParams['axes.facecolor'] = '#34495e'  # Цвет фона осей
        rcParams['axes.edgecolor'] = '#ecf0f1'  # Цвет рамки осей
        rcParams['axes.labelcolor'] = '#ecf0f1'  # Цвет подписей к осям
        rcParams['xtick.color'] = '#ecf0f1'  # Цвет делений по оси X
        rcParams['ytick.color'] = '#ecf0f1'  # Цвет делений по оси Y
        rcParams['text.color'] = '#ecf0f1'  # Цвет текста
        rcParams['legend.facecolor'] = '#34495e'  # Цвет фона легенды
        rcParams['legend.edgecolor'] = '#ecf0f1'  # Цвет рамки легенды
        rcParams['legend.fontsize'] = 10  # Размер шрифта легенды
        rcParams['legend.framealpha'] = 0.8  # Прозрачность фона легенды
        rcParams['font.weight'] = 'bold'  # Глобальный параметр для веса шрифта

        self.x_data = []  # Данные по оси X
        self.y_data = []  # Данные по оси Y
        self.max_points = max_points  # Максимальное количество точек на графике

        # Настройка осей графика
        #self.ax.set_ylim(-30,30 )  # Устанавливаем диапазон по оси Y от 0 до 100
        self.line, = self.ax.plot([], [], label="название", marker='*', linestyle='-')  # Линия на графике с маркерами
        self.ax.legend()

        # Добавляем анимацию
        self.ani = FuncAnimation(self.fig, self.animate_my_plot, init_func=self.init_plot, frames=1, interval=125)

    def init_plot(self):
        """Начальная установка графика"""
        self.line.set_data([], [])
        return self.line,

    def animate_my_plot(self,i):
        """Анимация графика"""
        self.update_graph()  # Обновляем график данными, которые уже были добавлены
        return self.line,

    def add_data(self, x, y, name):
        """Добавляем данные в график и обновляем его"""
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_label(name)
        self.ax.legend(loc='upper right')

        # Ограничиваем количество точек до max_points
        if len(self.x_data) > self.max_points:
            self.x_data = self.x_data[-self.max_points:]
            self.y_data = self.y_data[-self.max_points:]

    def update_graph(self):
        """Обновляем график"""
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()  # Обновляем лимиты осей
        self.ax.autoscale_view()  # Масштабируем график


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from globals import colors

# Настройка параметров
plt.style.use('seaborn-v0_8-dark')
plt.rcParams.update({
    'axes.facecolor': '#1e1e1e',           # Цвет фона осей
    'axes.edgecolor': '#2d2d2d',           # Цвет границ осей
    'axes.labelcolor': '#d3d3d3',          # Цвет меток осей
    'xtick.color': '#d3d3d3',              # Цвет меток по оси X
    'ytick.color': '#d3d3d3',              # Цвет меток по оси Y
    'text.color': '#d3d3d3',               # Цвет текста
    'figure.facecolor': '#1e1e1e',         # Цвет фона графика
    'figure.edgecolor': '#1e1e1e',         # Цвет границ графика
    'grid.color': '#2d2d2d',                # Цвет сетки
    'font.family': 'Arial',                 # Шрифт
    'font.size': 12,                        # Размер шрифта
    'lines.color': '#00b894',               # Цвет линий (светло-зеленый для визуализации)
    'legend.facecolor': '#2d2d2d',          # Цвет фона легенды
    'legend.edgecolor': '#1e1e1e',          # Цвет границ легенды
    'legend.fontsize': 10,                  # Размер шрифта легенды
})

class GraphController:
    """Класс отвечает за создаие, анимацию графиков matplotlib и их передачу на UI контроллер"""
    def __init__(self):
        # self.graphs будет состоять
        self.graphs = {}

        # список цветов для графиков
        self.colors = [
            '#00b894',  # Светло-зеленый
            '#6c5ce7',  # Фиолетовый
            '#00cec9',  # Бирюзовый
            '#fdcb6e',  # Светло-желтый
            '#e84393',  # Розовый
            '#d63031',  # Красный
            '#0984e3',  # Синий
            '#6ab04c',  # Зеленый
            '#e17055',  # Оранжевый
        ]

    def create_graph(self,obj):
        """Метод получает словарь далее создает и добавляет в него обьект класса Graph и весь этот передается self.graphs
         """
        if not isinstance(obj,dict):
            print("Данный обьект не является словарем!!!")
            return
        for name_graph , _dict in obj.items():
            if not "obj" in _dict:
                _dict["obj"] = Graph(color=self.colors[0])
        self.graphs = obj.copy()


class Graph:
    def __init__(self, parent=None, max_points=50,color = None):
        self.fig = Figure()  # Создаем объект Figure для графика
        self.canvas = FigureCanvas(self.fig)  # Холст для графика
        self.ax = self.fig.add_subplot(111)  # Добавляем ось
        self.fig.tight_layout()
        self.fig.subplots_adjust(0.04, 0, 0.99, 0.99,)  # left,bottom,right,top
        self.ax.grid(color='#303030', linestyle='-.', linewidth=1)

        self.x_data = []  # Данные по оси X
        self.y_data = []  # Данные по оси Y
        self.max_points = max_points  # Максимальное количество точек на графике

        # Начальное значение масштаба
        self.scale_factor = 1.0

        # Настройка осей графика
        self.line, = self.ax.plot([], [], label="название", marker='*', linestyle='-',color=color)  # Линия на графике с маркерами
        self.ax.legend()

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

        self.update_graph()  # Обновляем график после добавления данных

    def update_graph(self):
        """Обновляем график"""
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()  # Обновляем лимиты осей
        self.ax.autoscale_view()  # Масштабируем график
        self.canvas.draw()  # Перерисовываем график

    def scale_graph(self, increment):
        """Изменяет масштаб осей графика на фиксированное значение"""
        # Получаем текущие лимиты осей
        y_min, y_max = self.ax.get_ylim()

        # Увеличиваем или уменьшаем диапазоны осей на фиксированное значение
        y_range = (y_max - y_min) * increment  # Применяем фиксированное значение

        # Устанавливаем новые лимиты с учетом масштаба
        self.ax.set_ylim(y_min - 0.5 * y_range, y_max + 0.5 * y_range)

        # Обновляем график
        self.canvas.draw()

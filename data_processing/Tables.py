from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import globals

#print(plt.style.available)
plt.style.use('seaborn-v0_8-dark')
# Настройка параметров
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



class Graph:
    def __init__(self, parent=None, max_points=50):
        self.fig = Figure()  # Создаем объект Figure для графика
        self.canvas = FigureCanvas(self.fig)  # Холст для графика
        self.ax = self.fig.add_subplot(111)  # Добавляем ось
        self.fig.tight_layout()
        self.fig.subplots_adjust(0.04, 0, 0.99, 0.99,)  # left,bottom,right,top
        self.color = globals.colors[0]
        globals.colors.pop(0)
        self.ax.grid(color='#303030', linestyle='-.', linewidth=1)


        self.x_data = []  # Данные по оси X
        self.y_data = []  # Данные по оси Y
        self.max_points = max_points  # Максимальное количество точек на графике

        # Начальное значение масштаба
        self.scale_factor = 1.0

        # Настройка осей графика
        #self.ax.set_ylim(-30,30 )  # Устанавливаем диапазон по оси Y от 0 до 100
        self.line, = self.ax.plot([], [], label="название", marker='*', linestyle='-',color=self.color)  # Линия на графике с маркерами
        self.ax.legend()

        # Добавляем анимацию
        self.ani = FuncAnimation(self.fig, self.animate_my_plot, init_func=self.init_plot, frames=1, interval=200)

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

        # Метод для изменения масштаба

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



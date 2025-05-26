import pyqtgraph as pg

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

        # количество выданных цветов
        self.count_color = 0

    def create_graph(self,name_legend,x,y):
        """
        Метод получает имя легенды , Название параметра для дальнейшего парсинга по оси x and y
        Далее заносит данные в собственный словарь:
        self.graphs[Имя графика] = {"параметр по оси x ":x,"Параметр по оси y":y,'Обьект класса Graph':Graph(цвет лиинии,имя легенды)}
         """
        len(self.graphs)

        self.graphs[name_legend] = {"x_target":x,"y_target":y,'obj':Graph(color=self.get_color(),name=name_legend,max_points=25)}
        self.count_color += 1


    def update_graphs(self,packet):
        """Метод обновления графиков , принимает обьект класса Packet"""
        if self.graphs:
            data = packet.data

            for graph_dict in self.graphs.values():
                graph = graph_dict.get("obj")

                value_x = data.get(graph_dict.get("x_target"))
                value_y = data.get(graph_dict.get("y_target"))

                graph.add_data(x_data=value_x,y_data=value_y)

    def get_widget_graphs(self):
        if not self.graphs:
            return "созданных графиков нет"

        widgets = []
        for graph in self.graphs.values():
            obj = graph.get("obj")
            widgets.append(obj.get_plot_widget())
        return widgets

    def get_color(self):
        if self.count_color < len(self.colors):
            return self.colors[self.count_color]
        else:
            self.count_color = 0
            return self.colors[self.count_color]


class Graph:
    def __init__(self, color, name,max_points):
        # Используем OpenGL для рендеринга
        self.plot_widget = pg.PlotWidget(title=name, useOpenGL=True)
        self.plot_widget.setBackground(None)  # Цвет фона
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.curve = self.plot_widget.plot(pen=pg.mkPen(color=color, width=2))

        self.name = name

        self.max_points = max_points

        self.x_data = []
        self.y_data = []

    def add_data(self, x_data,y_data):
        """Метод для добавления данных в график"""

        if len(self.x_data) < self.max_points:
            self.x_data.append(x_data)
            self.y_data.append(y_data)

        else:
            self.x_data.pop(0)
            self.y_data.pop(0)

            self.x_data.append(x_data)
            self.y_data.append(y_data)

        self.update_graph()

    def update_graph(self):
        """Обновление графика"""
        self.curve.setData(self.x_data, self.y_data)
        self.plot_widget.setTitle(f"{self.name} {self.y_data[-1]}")

    def get_plot_widget(self):
        """Возвращаем виджет для добавления в интерфейс"""
        return self.plot_widget

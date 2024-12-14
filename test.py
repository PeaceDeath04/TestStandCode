graphs = {}


def create_graph(name_legend, x, y):
    """
    Метод получает имя легенды , Название параметра для дальнейшего парсинга по оси x and y
    Далее заносит данные в собственный словарь:
    self.graphs[Имя графика] = {"параметр по оси x ":x,"Параметр по оси y":y,'Обьект класса Graph':Graph(цвет лиинии,имя легенды)}
     """
    graphs[name_legend] = {"x_target": x, "y_target": y, 'obj':"тут обьект"}

create_graph(name_legend="Тяга",x="Time",y="Traction")

for params in graphs.values():
    print(params)
    print(type(params))
    #for key, value in params.items():

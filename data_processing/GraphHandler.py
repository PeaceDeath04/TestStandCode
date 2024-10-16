from .Data import import_js, localData, create_json
from .Tables import Graph
graphs = {}


def add_graphs():
    try:
        dict_js = import_js("keys_graphs.json")
        graphs = dict_js.copy()
    except:
        print("пусто")

    for nameGraph in graphs:
        graphs[nameGraph]["ObjectClass"] = Graph()
    for nameGraph, params in graphs.items():
        graph = graphs[nameGraph].get("ObjectClass")
        graph.ax.set_xlabel(graphs[nameGraph].get("x"))
        graph.ax.set_ylabel(graphs[nameGraph].get("y"))
        graph.line.set_label(graphs[nameGraph].get("y"))
    return graphs
def add_thread_graphs():
    for nameGraph, params in graphs.items():
        update_graph(params.get("ObjectClass"), params.get("x"), params.get("y"))
def update_graph(graph, xlabel, ylabel):
    """Метод принимает обьект класса Graph (график matplotlib) и 2 стринговых параматра на основании которых ищет в локал дате значения """
    x, y = localData.get(xlabel), localData.get(ylabel)
    if xlabel == "Time":
        x = x / 1000
    graph.ax.set_xlabel(xlabel)
    graph.ax.set_ylabel(ylabel)
    graph.line.set_label(ylabel)
    graph.add_data(x=x, y=y, name=f"{ylabel} = {y}")

def TestingGraphs(name_file):
    data = {}

    for key in localData.keys():
        data[f"{key}Graph"] = {"x": "Time" , "y":key}

    create_json(name_file,data)




import os
import sys

read_ready = False
calib_weight = 62.5
step_size = 10
colors = [
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

project_dir = os.path.dirname(os.path.abspath(sys.argv[0])) # Текущая директория проекта

json_dir = os.path.join(project_dir, "Json Saves")  # Папка "jsons" внутри проекта
exel_dir = os.path.join(project_dir,"Exel Tables") # папка с экселями
full_path_ToGraphs = os.path.join(json_dir, "keys_graphs.json")






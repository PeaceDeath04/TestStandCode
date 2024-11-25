import json
import os
from types import NoneType

name_save_file = "save_file.json"

localData = {
        "T_flach_E": 0, "T_flash_O": 0, "Voltage": 0.00, "ShuntVoltage": 0,
        "Temp": 0.0, "Traction": 0.0, "Weight": 0.0, "Weight_1": 0.0, "Weight_2": 0.0, "Time": 0,
        "gas": 25, "gas_min": 0, "gas_max": 50
    }

keys_to_update_ard = ["T_flach_E", "T_flash_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1",
                               "Weight_2", "Time"]

key_to_Graphs = {
        "TractionGraph": {"x": "Time", "y": "Traction"}
    }

keysArduino = {"gas": "g", "gas_min": "m", "gas_max": "x", "ButCalibMotor": "k", "ResetTime": "t",
                            "Traction": "r", "Weight_1": "o", "Weight_2": "w"}

# Указываем путь относительно папки проекта
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Текущая директория проекта

json_dir = os.path.join(project_dir, "Json Saves")  # Папка "jsons" внутри проекта

os.makedirs(json_dir,exist_ok=True) # создаем если нет папки



def export_to_json(name_file,**keys):
    """Получает ключ значение и сохраняет в json файл"""
    try:
        try:
            with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
        except FileNotFoundError:
            data = localData.copy()
        for key, value in keys.items():
            data[key] = value

        with open(os.path.join(json_dir,name_file), mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def import_from_json(name_file,*keys):
    """Получает ключи для извлечения значений  по ключу из json файла , возвращает список значений"""
    list = []
    try:
        with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            for key in keys:
                list.append(data.get(key))
            return list
    except FileNotFoundError:
        create_json(name_file, localData)
        for key in keys:
            list.append(localData[key])
        return list
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {save_file}.")
        return None


def create_json(name_file, data):
    """
    Создает JSON файл по указанному пути, если он не существует.
    """
    # Указываем путь для файла в директории json_dir
    full_path = os.path.join(json_dir, name_file)

    # Проверяем, существует ли файл
    if not os.path.isfile(full_path):
        try:
            # Создаем файл с данными
            with open(full_path, mode="w", encoding="utf-8") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)
            print(f"Файл {full_path} успешно создан.")
        except Exception as e:
            print(f"Ошибка при создании файла {full_path}: {e}")
    else:
        pass
        #print(f"Файл {full_path} уже существует.")


def import_js(name_file):
    """Передаем в качестве параметра имя искомого файла и передаем dict/None в зависимости от результата"""
    try:
        with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            return data
    except FileNotFoundError:
        create_json(name_file, None)
        return None




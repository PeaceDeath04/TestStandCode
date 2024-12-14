import os
import json
import sys

project_dir = os.path.dirname(os.path.abspath(sys.argv[0])) # Текущая директория проекта
json_dir = os.path.join(project_dir, "Json Saves")  # Папка "jsons" внутри проекта
exel_dir = os.path.join(project_dir,"Exel Tables") # папка с экселями
path_timings = os.path.join(json_dir, "timings.json")
path_ToRead = os.path.join(json_dir, "ToRead.json")
full_path_ToGraphs = os.path.join(json_dir, "keys_graphs.json")

def export_to_json(name_file,**keys):
    """Получает ключ значение и сохраняет в json файл"""
    try:
        try:
            with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
                if data is None:
                    print("JSON-файл пуст или некорректен, инициализируем пустой словарь.")
                    data = {}
        except FileNotFoundError:
            data = {}
        for key, value in keys.items():
            data[key] = value

        with open(os.path.join(json_dir,name_file), mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def import_from_json(name_file,*keys):
    """Получает ключи для извлечения значений  по ключу из json файла , возвращает список значений"""
    listt = []
    try:
        with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            for key in keys:
                listt.append(data.get(key))
            return listt
    except FileNotFoundError:
        print("файл не найден")
        return None
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

def import_js(name_file):
    """Передаем в качестве параметра имя искомого файла и передаем dict/None в зависимости от результата"""
    try:
        with open(os.path.join(json_dir,name_file), mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            return data
    except FileNotFoundError:
        create_json(name_file, None)
        return None




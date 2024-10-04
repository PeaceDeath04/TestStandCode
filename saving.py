import json
import os


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

Tar = 0



def export_to_json(**keys):
    """Получает ключ значение и сохраняет в json файл"""
    try:
        try:
            with open(name_save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
        except FileNotFoundError:
            data = localData.copy()
        for key, value in keys.items():
            data[key] = value

        with open(name_save_file, mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
def import_from_json(*keys):
    """Получает ключи для извлечения значений  по ключу из json файла , возвращает список значений"""
    list = []
    try:
        with open(name_save_file, mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            for key in keys:
                list.append(data.get(key))
            return list
    except FileNotFoundError:
        create_json(name_save_file, localData)
        for key in keys:
            list.append(localData[key])
        return list
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {save_file}.")
        return None
def create_json(name_save_file, data):
    if not os.path.isfile(name_save_file):
        with open(name_save_file, mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)
def import_js(name_save_file):
    """Передаем в качестве параметра имя искомого файла и передаем dict/None в зависимости от результата"""
    try:
        with open(name_save_file, mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            return data
    except FileNotFoundError:
        create_json(name_save_file, None)
        return None
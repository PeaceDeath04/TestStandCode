import json
from Window import ui
Name_save_file = "save_file.json"


dict_variables = {"T_flach_E":0,"T_flash_O":0, "Voltage":0.00, "ShuntVoltage":0,"Temp":0.0,"Traction":0.0,"Weight_1":0.0,"Weight_2":0.0,"gas": 25 , "gas_min": 0 , "gas_max": 50}

def ExportToJson(key, value):
    try:
        # Открываем файл и загружаем существующие данные
        try:
            with open(Name_save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
        except FileNotFoundError:
            # Если файл не найден, используем пустой словарь
            data = dict_variables.copy()

        # Обновляем значение по ключу
        data[key] = value

        # Сохраняем обновлённые данные обратно в файл
        with open(Name_save_file, mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)

        ui.sendDb(f"Значение для ключа '{key}' успешно обновлено в {Name_save_file}.")

    except json.JSONDecodeError:
        ui.sendDb(f"Ошибка декодирования JSON в файле {Name_save_file}.")
    except IOError as e:
        ui.sendDb(f"Ошибка при работе с файлом {Name_save_file}: {e}")
    except Exception as e:
        ui.sendDb(f"Произошла непредвиденная ошибка: {e}")

def ImportFromJson(key):
    try:
        with open(Name_save_file, mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)
            return data.get(key, None)  # Возвращает значение по ключу, если ключа нет - возвращает None
    except FileNotFoundError:
            with open(Name_save_file,mode="w",encoding="Latin-1") as save_file:
                json.dump(dict_variables,save_file,ensure_ascii=False, indent=4)
            return dict_variables[key]
    except json.JSONDecodeError:
        ui.sendDb(f"Ошибка декодирования JSON в файле {Name_save_file}.")
        return None

def ArduToJson(object):
    try:
        # Открываем файл и загружаем данные
        with open(Name_save_file, mode="r", encoding="Latin-1") as save_file:
            data = json.load(save_file)

        # Создаем список ключей, которые нужно обновить (в примере это 8 значений, можно настроить под конкретные поля)
        keys_to_update = ["T_flach_E", "T_flash_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1", "Weight_2"]

        # Проверяем, что длина объекта совпадает с количеством ключей
        if len(object) == len(keys_to_update):
            # Собираем в zip и обновляем значения
            for key, value in zip(keys_to_update, object):
                data[key] = float(value)

            # Сохраняем обновленные данные обратно в файл
            with open(Name_save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)

            #ui.sendDb("Данные с ардуино успешно сохранены")
        else:
            pass
            #("Ошибка: некорректный формат данных с ардуино")

    except FileNotFoundError:
        # Если файл не найден, используем пустой словарь
        data = dict_variables.copy()
        with open(Name_save_file, mode="w", encoding="Latin-1") as save_file:
            json.dump(data, save_file, ensure_ascii=False, indent=4)
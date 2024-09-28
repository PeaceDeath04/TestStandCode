import json
import os

class JsonHandler:
    def __init__(self, save_file="save_file.json", log_function=None):
        self.save_file = save_file
        #локал дата будет хранить в себе уже прооперированые параметры
        self.localData = {
            "T_flach_E": 0, "T_flash_O": 0, "Voltage": 0.00, "ShuntVoltage": 0,
            "Temp": 0.0, "Traction": 0.0, "Weight": 0.0,"Time": 0,
            "gas": 25, "gas_min": 0, "gas_max": 50
        }
        self.keys_to_update_ard = ["T_flach_E", "T_flash_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1",
                          "Weight_2", "Time"]
        self.key_to_Graphs = {
            "TractionGraph": {"x": "Time", "y": "Traction"}
        }
        self.log_function = log_function

        self.Tar = 0
        self.create_json("keys_graphs.json",self.key_to_Graphs)

    def _log(self, message):
        if self.log_function:
            self.log_function(message)

    def export_to_json(self, **keys):
        """Получает ключ значение и сохраняет в json файл"""
        try:
            try:
                with open(self.save_file, mode="r", encoding="Latin-1") as save_file:
                    data = json.load(save_file)
            except FileNotFoundError:
                data = self.localData.copy()
            for key,value in keys.items():
                data[key] = value

            with open(self.save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)

            self._log(f"Значения успешно обновлены в {self.save_file}.")
        except json.JSONDecodeError:
            self._log(f"Ошибка декодирования JSON в файле {self.save_file}.")
        except IOError as e:
            self._log(f"Ошибка при работе с файлом {self.save_file}: {e}")
        except Exception as e:
            self._log(f"Произошла непредвиденная ошибка: {e}")

    def import_from_json(self, *keys):
        """Получает ключи для извлечения значений  по ключу из json файла , возвращает список значений"""
        list = []
        try:
            with open(self.save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
                for key in keys:
                    list.append(data.get(key))
                return list
        except FileNotFoundError:
            self.create_json(self.save_file,self.localData)
            for key in keys:
                list.append(self.localData[key])
            return list
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.save_file}.")
            return None

    def create_json(self,name_save_file,data):
        if not os.path.isfile(name_save_file):
            with open(name_save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)

    def import_js(self,name_save_file):
        """Передаем в качестве параметра имя искомого файла и возвращаем dict/None в зависимости от результата"""
        try:
            with open(name_save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
                return data
        except FileNotFoundError:
            self.create_json(name_save_file, None)
            return None
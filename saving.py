import json

class JsonHandler:
    def __init__(self, save_file="save_file.json", default_data=None, log_function=None):
        self.save_file = save_file
        self.data = {
            "T_flach_E": 1, "T_flash_O": 3, "Voltage": 2.00, "ShuntVoltage": 6,
            "Temp": 0.0, "Traction": 0.0, "Weight_1": 0.0, "Weight_2": 0.0,
            "gas": 25, "gas_min": 0, "gas_max": 50
        }
        self.log_function = log_function

    def _log(self, message):
        if self.log_function:
            self.log_function(message)

    def export_to_json(self, key, value):
        try:
            try:
                with open(self.save_file, mode="r", encoding="Latin-1") as save_file:
                    data = json.load(save_file)
            except FileNotFoundError:
                data = self.default_data.copy()

            data[key] = value

            with open(self.save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)

            self._log(f"Значение для ключа '{key}' успешно обновлено в {self.save_file}.")
        except json.JSONDecodeError:
            self._log(f"Ошибка декодирования JSON в файле {self.save_file}.")
        except IOError as e:
            self._log(f"Ошибка при работе с файлом {self.save_file}: {e}")
        except Exception as e:
            self._log(f"Произошла непредвиденная ошибка: {e}")

    def import_from_json(self, key):
        try:
            with open(self.save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)
                return data.get(key)
        except FileNotFoundError:
            with open(self.save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(self.default_data, save_file, ensure_ascii=False, indent=4)
            return self.default_data[key]
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.save_file}.")
            return None

    def import_local_data(self,key):
        return self.data.get(key)


    def export_local_data(self,key,value):
        self.data[key] = value

    def ardu_to_json(self, obj):
        try:
            with open(self.save_file, mode="r", encoding="Latin-1") as save_file:
                data = json.load(save_file)

            keys_to_update = ["T_flach_E", "T_flash_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1", "Weight_2"]

            if len(obj) == len(keys_to_update):
                for key, value in zip(keys_to_update, obj):
                    data[key] = float(value)

                with open(self.save_file, mode="w", encoding="Latin-1") as save_file:
                    json.dump(data, save_file, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            data = self.default_data.copy()
            with open(self.save_file, mode="w", encoding="Latin-1") as save_file:
                json.dump(data, save_file, ensure_ascii=False, indent=4)

    def export_data(self,**packet_data):
        for key,value in packet_data.items():
            self.export_local_data(key,value)
            self.export_to_json(key,value)


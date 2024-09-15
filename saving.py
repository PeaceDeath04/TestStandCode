import json

class JsonHandler:
    def __init__(self, save_file="save_file.json", default_data=None, log_function=None):
        self.save_file = save_file
        self.default_data = default_data or {
            "T_flach_E": 0, "T_flash_O": 0, "Voltage": 0.00, "ShuntVoltage": 0,
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

# Пример использования класса:
# json_handler = JsonHandler(log_function=print)
# json_handler.export_to_json("Voltage", 12.5)
# print(json_handler.import_from_json("Voltage"))
# json_handler.ardu_to_json([1, 2, 3.3, 4, 5, 6, 7, 8])

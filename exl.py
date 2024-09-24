import sys

import pandas as pd
import traceback

class Exl:
    def __init__(self, file_name='data.xlsx'):
        self.buffer = []
        self.bufferSize = 100
        self.file_name = file_name
        #self.stolbs = ["T_flach_E", "T_flach_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1", "Weight_2", "mainTime"]
        self.stolbs = ["T_flach_E", "T_flach_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight_1", "Weight_2"]

        # Проверяем, существует ли файл
        try:
            self.df = pd.read_excel(self.file_name)  # Загружаем существующий файл
            print(f"Файл {self.file_name} успешно загружен.")
        except FileNotFoundError:
            # Если файл не найден, создаем новый DataFrame с заголовками столбцов
            print(f"Файл не найден, создаем новый: {self.file_name}")
            self.df = pd.DataFrame(columns=self.stolbs)
            self.df.to_excel(self.file_name, index=False)

    def add_data_from_list(self, data_list):
        try:
            if (len(data_list)) == (len(self.stolbs)):
                print("gg")

        except:
            pass

    @staticmethod
    def try_convert_to_number(value):
        try:
            if '.' in value:
                return float(value)  # Преобразуем в float
            else:
                return int(value)    # Преобразуем в int
        except ValueError:
            return value  # Если не удалось преобразовать, оставляем как есть


"""
    def _pia(self,data):
         Processing Information from Arduino / обработка информации c arduino

        piaData = {}
        #сохранили внутри метода пакет данных из сериал порта
        if len(data) == 9:
            for key, value in zip(self.save.keys_to_update_ard, data):
                piaData[key] = value

        #сохранили в локальную дату вес
        weight = (piaData["Weight_1"] - piaData["Weight_2"]) / 2
        self.save.export_local_data("Weight",weight)

        # Получаем значение Traction из локал даты
        tPy = self.save.import_local_data("Traction")

        # Получаем значение Traction из арудино даты
        tArdu = piaData.get("Traction")

        # сохраняем разницу Traction в  локал дату
        tPy = tArdu - self.save.Tar
        self.save.export_local_data("Traction",tPy)

        self.save.export_local_data()
        print(piaData)

"""

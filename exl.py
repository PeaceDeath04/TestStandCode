import sys

import pandas as pd
import traceback

class Exl:
    def __init__(self, file_name='data.xlsx'):
        self.buffer = []
        self.bufferSize = 100
        self.file_name = file_name
        self.stolbs = ["Time","T_flach_E", "T_flach_O", "Voltage", "ShuntVoltage", "Temp", "Traction", "Weight"]

        # Проверяем, существует ли файл
        try:
            self.df = pd.read_excel(self.file_name)  # Загружаем существующий файл
            print(f"Файл {self.file_name} успешно загружен.")
        except FileNotFoundError:
            # Если файл не найден, создаем новый DataFrame с заголовками столбцов
            print(f"Файл не найден, создаем новый: {self.file_name}")
            self.df = pd.DataFrame(columns=self.stolbs)
            self.df.to_excel(self.file_name, index=False)



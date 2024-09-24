import pandas as pd
import csv
import os


class DataRecorder:
    def __init__(self, csv_file='data.csv', xlsx_file='data.xlsx'):
        self.csv_file = csv_file
        self.xlsx_file = xlsx_file

        # Заголовки для CSV файла
        self.headers = ['T_flach_E', 'T_flash_O', 'Voltage', 'ShuntVoltage', 'Temp', 'Time', 'mainWeight', 'Traction']

        # Если файла CSV нет, создаем его с заголовками
        if not os.path.isfile(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def save_to_csv(self, data):
        """Сохраняет данные в CSV файл"""
        if isinstance(data, dict):
            data_row = [data.get(header, '') for header in self.headers]  # Получаем значения по заголовкам
        elif isinstance(data, list):
            data_row = data
        else:
            print("Ошибка: данные должны быть списком или словарём.")
            return

        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_row)

    def convert_csv_to_xlsx(self):
        """Конвертирует CSV файл в XLSX"""
        if os.path.isfile(self.csv_file):
            df = pd.read_csv(self.csv_file)
            df.to_excel(self.xlsx_file, index=False)
        else:
            print(f"Файл {self.csv_file} не найден. Нечего конвертировать.")

    def clear_csv(self):
        """Очищает CSV файл, оставляя только заголовки"""
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
        print(f"Файл {self.csv_file} был очищен.")


import pandas as pd
import csv
import os
from datetime import datetime


class DataRecorder:
    def __init__(self, base_filename='data'):
        self.base_filename = base_filename  # Базовое имя файла
        self.csv_file = None  # Имя текущего CSV файла
        self.xlsx_file = None  # Имя текущего Excel файла
        self.headers = [
            'T_flach_E', 'T_flash_O', 'Voltage', 'ShuntVoltage',
            'Temp', 'Traction', 'Weight', 'Time', 'gas', 'gas_min', 'gas_max'
        ]

    def _generate_unique_filename(self, extension):
        """Генерирует уникальное имя файла на основе текущего времени."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"{self.base_filename}_{timestamp}.{extension}"

    def start_new_recording(self):
        """Создает новый CSV файл для записи и инициализирует его заголовками."""
        # Генерируем уникальное имя для нового CSV файла
        self.csv_file = self._generate_unique_filename('csv')

        # Создаем новый CSV файл с заголовками
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)

        print(f"Начата новая запись: {self.csv_file}")

    def save_to_csv(self, data):
        """Добавляет данные в текущий CSV файл."""
        if self.csv_file is None:
            print("Ошибка: начните новую запись, вызвав метод `start_new_recording()`.")
            return

        print(f"Сохраняю данные в {self.csv_file}")

        # Преобразуем данные в строку в зависимости от типа
        if isinstance(data, dict):
            data_row = [data.get(header, '') for header in self.headers]
        elif isinstance(data, list):
            data_row = data
        else:
            print("Ошибка: данные должны быть списком или словарём.")
            return

        # Записываем строку данных в текущий CSV файл
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_row)

    def convert_csv_to_xlsx(self):
        """Конвертирует текущий CSV файл в XLSX и удаляет исходный CSV файл."""
        if self.csv_file is None or not os.path.isfile(self.csv_file):
            print(f"Файл {self.csv_file} не найден. Нечего конвертировать.")
            return

        # Генерируем имя Excel файла на основе текущего CSV файла
        self.xlsx_file = self.csv_file.replace('.csv', '_exl.xlsx')

        # Конвертируем CSV в Excel
        df = pd.read_csv(self.csv_file)
        df.to_excel(self.xlsx_file, index=False)

        print(f"CSV файл {self.csv_file} успешно конвертирован в {self.xlsx_file}")

        # Удаляем исходный CSV файл
        try:
            os.remove(self.csv_file)
            print(f"CSV файл {self.csv_file} был удален.")
            self.csv_file = None  # Сбрасываем текущее имя CSV файла
        except OSError as e:
            print(f"Ошибка при удалении файла {self.csv_file}: {e}")

    def clear_csv(self):
        """Очищает текущий CSV файл, оставляя только заголовки."""
        if self.csv_file is None:
            print("Ошибка: текущий CSV файл не найден.")
            return

        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)

        print(f"Файл {self.csv_file} был очищен.")


import pandas as pd
import csv
import os
from datetime import datetime
from data_processing.Data import import_js,json_dir

class DataRecorder:
    def __init__(self, base_filename='data'):
        self.base_filename = base_filename  # Базовое имя файла
        self.csv_file = None  # Имя текущего CSV файла
        self.xlsx_file = None  # Имя текущего Excel файла
        self.headers = [
            'T_flach_E', 'T_flash_O', 'Voltage', 'ShuntVoltage',
            'Temp', 'Traction', 'Weight', 'Time', 'gas', 'gas_min', 'gas_max'
        ]

        # Указываем путь относительно папки проекта
        self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Текущая директория проекта
        self.exel_dir = os.path.join(self.project_dir, "Exel Tables")  # Папка "jsons" внутри проекта

        self.name_file_ToRead = "ToRead.json"
        self.full_path_ToRead = os.path.join(json_dir,self.name_file_ToRead)

        os.makedirs(self.exel_dir, exist_ok=True)  # создаем если нет папки

    def _generate_unique_filename(self, extension):
        """Генерирует уникальное имя файла на основе текущего времени."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"{self.base_filename}_{timestamp}.{extension}"

    def start_new_recording(self):
        """Создает новый CSV файл для записи и инициализирует его заголовками."""
        self.passed_to_write()

        # Генерируем уникальное имя для нового CSV файла
        self.csv_file = self._generate_unique_filename('csv')

        full_path = os.path.join(self.exel_dir, self.csv_file)

        # Создаем новый CSV файл с заголовками
        with open(full_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)

        print(f"Начата новая запись: {self.csv_file}")

    def save_to_csv(self, data):
        """Добавляет данные в текущий CSV файл."""
        if self.csv_file is None:
            print("Ошибка: начните новую запись, вызвав метод `start_new_recording()`.")
            return

        full_path = os.path.join(self.exel_dir,self.csv_file)

        print(f"Сохраняю данные в {full_path}")

        # Преобразуем данные в строку в зависимости от типа
        if isinstance(data, dict):
            data_row = [data.get(header, '') for header in self.headers]
        elif isinstance(data, list):
            data_row = data
        else:
            print("Ошибка: данные должны быть списком или словарём.")
            return

        # Записываем строку данных в текущий CSV файл
        with open(full_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_row)

    def convert_csv_to_xlsx(self):
        """Конвертирует текущий CSV файл в XLSX и удаляет исходный CSV файл."""
        full_path = os.path.join(self.exel_dir, self.csv_file)

        if self.csv_file is None or not os.path.isfile(full_path):
            print(f"Файл {self.csv_file} не найден. Нечего конвертировать.")
            return

        # Генерируем имя Excel файла на основе текущего CSV файла
        self.xlsx_file = full_path.replace('.csv', '_exl.xlsx')

        # Конвертируем CSV в Excel
        df = pd.read_csv(full_path)
        df.to_excel(self.xlsx_file, index=False)

        print(f"CSV файл {full_path} успешно конвертирован в {self.xlsx_file}")

        # Удаляем исходный CSV файл
        try:
            os.remove(full_path)
            print(f"CSV файл {full_path} был удален.")
            self.csv_file = None  # Сбрасываем текущее имя CSV файла
        except OSError as e:
            print(f"Ошибка при удалении файла {full_path}: {e}")

    def clear_csv(self):
        """Очищает текущий CSV файл, оставляя только заголовки."""
        if self.csv_file is None:
            print("Ошибка: текущий CSV файл не найден.")
            return

        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)

        print(f"Файл {self.csv_file} был очищен.")

    def passed_to_write(self):
        """Метод для отбора параметров для записи в exel , мы читаем файл из настроек , при совпадении хедара и ключа из файла и значение не true , то удаляем из списка"""
        try:
            data = import_js(self.full_path_ToRead)  # читаем файл параметров для пропуска к записи
            for name, state in data.items():
                for head in self.headers:
                    if name == head:
                        if state != True:
                            self.headers.remove(name)
        except Exception as e:
            print(e)

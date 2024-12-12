from JsonHandler import *
import pandas as pd
import csv
from datetime import datetime


class Data:
    def __init__(self):
        # данный список нужен для работы с последними 25 обработанными пакетами
        self.local_data = []

        # переменная для работы с калибровкой
        self.calib_weight = 0

        # словарь для хранения веса тарирования traction
        self.taring_traction = {}

        #словарь для хранения веса и его тарирования
        self.taring_weight = {}

        # словарь для хранения коэф. калиброовки
        self.param_kef = {}

    def create_pack(self,obj):
        """Метод добавляет пакет в общий список локальной памяти с максимальной длинной 25"""
        packet = Packet(raw_packet=obj,data=self)
        if len(self.local_data) < 25:
            self.local_data.append(packet)
        else:
            self.local_data.pop(0)
            self.local_data.append(packet)

    def input_params_for_calib(self, key_param):
        """Добавляет коэффициент калибровки для указанного параметра."""
        if not self.local_data:
            print("Ошибка: список local_data пуст.")
            return

        last_packet = self.local_data[-1]  # Последний элемент списка
        if not isinstance(last_packet, Packet):
            print("Ошибка: последний элемент local_data не является объектом Packet.")
            return


        if self.calib_weight == 0:
            print("Ошибка: калибровочный вес равен нулю.")
            return

        # Расчет коэффициента калибровки
        if key_param == "Traction":
            self.param_kef["Traction"] = last_packet._data.get("Traction") / self.calib_weight

            print(f"Коэффициент калибровки для Traction: {self.param_kef.get('Traction')}")

        if key_param == "Weight":
            self.param_kef["Weight_1"] = last_packet._data.get("Weight_1") / self.calib_weight
            self.param_kef["Weight_2"] = last_packet._data.get("Weight_2") / self.calib_weight

            print(f"Коэффициент калибровки для Weight_1: {self.param_kef.get('Weight_1')}")
            print(f"Коэффициент калибровки для Weight_2: {self.param_kef.get('Weight_2')}")

    def input_params_for_taring(self,key_param):
        """Добавляет из последнего обработанного вес для указанного параметра по ключу."""

        if not self.local_data:
            print("Ошибка: список local_data пуст.")
            return

        last_packet = self.local_data[-1]  # Последний элемент списка

        if not isinstance(last_packet, Packet):
            print("Ошибка: последний элемент local_data не является объектом Packet.")
            return

        if key_param == "Traction":
            if not self.taring_traction:
                self.taring_traction["Traction"] = last_packet._data.get("Traction")
            else:
                self.taring_traction["Traction2"] = last_packet._data.get("Traction")
            return

        if key_param == "Weight":
            if not self.taring_weight:
                self.taring_weight["Weight_1"] = last_packet._data.get("Weight_1", 0)
                self.taring_weight["Weight_2"] = last_packet._data.get("Weight_2", 0)
            else:
                self.taring_weight["Weight_12"] = last_packet._data.get("Weight_1", 0)
                self.taring_weight["Weight_22"] = last_packet._data.get("Weight_2", 0)

    def get_last_packet(self):
        return (self.local_data[-1]._data)

class Packet:
    def __init__(self,raw_packet,data):
        # наименования параметров для будущего словаря
        self.keys_to_update_ard = ["T_flach_E", "T_flash_O","Voltage", "ShuntVoltage","Temp", "Traction","Weight_1","Weight_2","Time"]

        # здесь хранятся данные по каждому параметру
        self._data = {}

        # получаем словарь коэффициэнтов из экземпляра класса Data
        self.param_kef = data.param_kef

        # получаем словарь тарирований traction из экземпляра класса Data
        self.taring_traction = data.taring_traction

        # получаем словарь тарирований weight из экземпляра класса Data
        self.taring_weight = data.taring_weight

        # номер иттерации для первичного и вторичного тарирования
        self.iter_taring = 1

        # Здесь проходит обработка пакета данных
        self.processing_packet(raw_packet=raw_packet)

    def processing_packet(self,raw_packet):
        """Здесь проходит обработка пакета данных"""

        # 1. Обьединям наименования ключей с их значениями
        for key, value in zip(self.keys_to_update_ard, raw_packet):
            self._data[key] = float(value)

        # 2. производим первичное тарирование
        self.taring_values(self.taring_traction)
        self.taring_values(self.taring_weight)

        # 3. производим калибровку
        self.calibrate_values()

        # 4. Находим общий вес
        self._data["Weight"] = (self._data["Weight_1"] - self._data["Weight_2"]) / 2

        # 5. Производим вторичное тарирование
        self.iter_taring = 2
        self.taring_values(self.taring_traction)
        self.taring_values(self.taring_weight)

        # 6 производим округление до сотых
        self.rounding_params()

    def taring_values(self, dict_tar):
        """
        Метод для тарирования значений в self.data на основе данных из dict_tar.

        - Для первичного тарирования (self.iter_taring == 1):
          Проверяет наличие ключей из dict_tar в self.data и выполняет вычитание.

        - Для вторичного тарирования (self.iter_taring != 1):
          Ищет ключи с добавлением суффикса '2' в dict_tar и вычитает их значения из self.data.

        Параметры:
        dict_tar (dict): Словарь с данными для тарирования.
        """
        if dict_tar is not None:  # Проверяем, есть ли данные для тарирования
            if self.iter_taring == 1:  # Первичное тарирование
                for key in dict_tar:
                    if key in self._data:
                        self._data[key] -= dict_tar.get(key, 0)
                # Убрали return, чтобы обработать все ключи

            else:  # Вторичное тарирование
                for key in self._data:
                    _key = key + "2"  # Добавляем суффикс для поиска вторичных значений
                    if _key in dict_tar:
                        self._data[key] -= dict_tar.get(_key, 0)

    def calibrate_values(self):
        if self.param_kef:
            for key, value_kef in self.param_kef:  # получаем все ключи и их значения в словаре
                current_value = self._data.get(key)  # получаем текущее необработанное число
                current_value /= value_kef  # производим деление на коэф
                self._data[key] = current_value  # обновляем значение по ключу в словаре для return

    def rounding_params(self):
        for key, value in self._data.items():
            self._data[key] = round(value, 2)

class DataRecorder:
    def __init__(self, base_filename='data'):
        self.base_filename = base_filename  # Базовое имя файла
        self.csv_file = None  # Имя текущего CSV файла
        self.xlsx_file = None  # Имя текущего Excel файла
        self.headers = [
            'T_flach_E', 'T_flash_O', 'Voltage', 'ShuntVoltage',
            'Temp', 'Traction', 'Weight', 'Time', 'gas', 'gas_min', 'gas_max'
        ]

        self.is_reading = False

        # Указываем путь относительно папки проекта
        self.exel_dir = exel_dir

        self.name_file_ToRead = "ToRead.json"
        self.full_path_ToRead = os.path.join(json_dir,self.name_file_ToRead)

    def _generate_unique_filename(self, extension):
        """Генерирует уникальное имя файла на основе текущего времени."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"{self.base_filename}_{timestamp}.{extension}"

    def start_new_recording(self):
        """Создает новый CSV файл для записи и инициализирует его заголовками."""
        self.is_reading = True

        headers = self.passed_to_write()

        # Генерируем уникальное имя для нового CSV файла
        self.csv_file = self._generate_unique_filename('csv')

        full_path = os.path.join(self.exel_dir, self.csv_file)

        # Создаем новый CSV файл с заголовками
        with open(full_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

        print(f"Начата новая запись: {self.csv_file}")

    def save_to_csv(self, data):
        """Добавляет данные в текущий CSV файл."""
        headers = self.passed_to_write()

        if self.csv_file is None:
            print("Ошибка: начните новую запись, вызвав метод `start_new_recording()`.")
            return

        full_path = os.path.join(self.exel_dir,self.csv_file)

        print(f"Сохраняю данные в {full_path}")

        # Преобразуем данные в строку в зависимости от типа
        if isinstance(data, dict):
            data_row = [data.get(header, '') for header in headers]
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
        """
        Метод для отбора параметров для записи в Excel.
        Мы читаем файл из настроек, при совпадении хедера и ключа из файла
        и состоянии True добавляем в список для записи.
        """
        to_write = []
        try:
            data = import_js(self.full_path_ToRead)  # читаем файл параметров для пропуска к записи
            for name, state in data.items():
                for head in self.headers:
                    if name == head and state:
                        to_write.append(name)
                        # Переходим к следующей итерации внешнего цикла
                        break  # Заканчиваем текущую проверку для этого `name`
            return to_write
        except Exception as e:
            print(e)
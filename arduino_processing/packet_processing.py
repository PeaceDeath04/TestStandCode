"""   packet_processing занимается обработкой пакета с arduino                                      """
from data_processing.Data import localData,keys_to_update_ard
from data_processing.GraphHandler import add_thread_graphs
from data_processing.exl import DataRecorder
import globals
from globals import calib_weight

params_tenz_kef = {}
dict_tar = {}
recorder = DataRecorder()

def add_exl_info():
    if globals.read_ready:
        data = localData.copy()
        recorder.save_to_csv(data=data)

def but_taring(param):
    """Кнопка тарирования \n Принимает параметр в строковом виде , который извлекает из LocalДаты и добавляет в словарь для тарирования"""
    if param == "Traction":
        dict_tar["Traction"] = localData.get("Traction")
    if param == "Weight":
        dict_tar["Weight_1"] = localData.get("Weight_1")
        dict_tar["Weight_2"] = localData.get("Weight_2")

def taring_values(packet_data):
    if dict_tar is not None:
        for key_packet, value_packet in packet_data.items():
            print(f"до тарирования{packet_data[key_packet]}")
            for key_tar, value_tar in dict_tar.items():
                if key_tar == key_packet:
                    packet_data[key_packet] -= value_tar
    return packet_data


def get_kef_tenz(key_value):
    calib_weight = globals.calib_weight
    """Получаем ключ в виде строки"""
    if key_value == "Traction":
        params_tenz_kef["Traction"] = localData.get("Traction") / calib_weight

    if key_value == "Weight":
        params_tenz_kef["Weight_1"] = localData.get("Weight_1") / calib_weight
        params_tenz_kef["Weight_2"] = localData.get("Weight_2") / calib_weight



def get_result_value(pia_data):
    """производим деление параметров на их коэффициенты если таковы имеются"""
    if params_tenz_kef:  # проверка на наличие коэффицентов в словаре
        for key, value_kef in params_tenz_kef.items():  # получаем все ключи и их значения в словаре
            current_value = pia_data.get(key)  # получаем текущее необработанное число
            current_value /= value_kef  # производим деление на коэф
            pia_data[key] = current_value  # обновляем значение по ключу в словаре для return
    return pia_data

def rounding_params(data):
    for key,value in data.items():
        data[key] = round(value,2)
    return data

# Обновлённые функции для тарирования и вычислений
def but_taring_after_calibration(pia_data, param):
    """Тарирование после калибровки"""
    if param == "Traction":
        dict_tar["Traction"] = pia_data["Traction"]
    if param == "Weight":
        dict_tar["Weight_1"] = pia_data["Weight_1"]
        dict_tar["Weight_2"] = pia_data["Weight_2"]

def get_result_value_after_taring(pia_data):
    """Учитываем тару поверх уже откалиброванных значений"""
    for key, value_tar in dict_tar.items():
        if key in pia_data:
            pia_data[key] -= value_tar  # Вычитаем только значение тары
    return pia_data


def pia(data):
    """Обработка с учётом тарирования после калибровки"""
    pia_data = {}

    # 1. Создаём сырые данные
    for key, value in zip(keys_to_update_ard, data):
        pia_data[key] = float(value)

    # 2. Применяем коэффициенты калибровки
    if params_tenz_kef:
        pia_data.update(get_result_value(pia_data))

    # 3. Применяем тару (если она установлена)
    if dict_tar:
        pia_data.update(get_result_value_after_taring(pia_data))

    # 4. Вычисляем общий вес
    pia_data["Weight"] = (pia_data["Weight_1"] - pia_data["Weight_2"]) / 2

    # 5. Округляем значения
    pia_data.update(rounding_params(pia_data))

    # Сохраняем в локальные данные
    localData.update(pia_data)

    # Обновляем графики
    add_thread_graphs()


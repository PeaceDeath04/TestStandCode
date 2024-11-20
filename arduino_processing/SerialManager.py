from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import traceback
from arduino_processing.packet_processing import pia, add_exl_info
import globals

buffer = ""
serial_speed = 9600
serial = QSerialPort()
serial.setBaudRate(serial_speed)


def open_port(port_name):
    # Закрываем текущий порт, если он открыт
    if serial.isOpen():
        if serial.portName() != port_name:
            serial.close()
            print(f"Закрытие порта {serial.portName()} перед открытием нового")

    # Устанавливаем и открываем новый порт
    serial.setPortName(port_name)
    if serial.open(QIODevice.ReadWrite):
        print(f"Порт {port_name} открыт")
    else:
        return f"Не удалось открыть порт {port_name} , т.к он уже используется"
def close_port():
    if serial.isOpen():
        serial.close()
        return "Порт закрыт"
    return "Порт уже закрыт"

def update_port_list():
    ports = QSerialPortInfo.availablePorts()
    return [port.portName() for port in ports]

def validate_data_packet(packet):
    # 1. Проверка длины пакета
    if len(packet) != 9:
        print(f"Ошибка: длина пакета должна быть 9, но получено {len(packet)} элементов.")
        return False

    # 2. Проверка каждого элемента на возможность конвертации в число
    for item in packet:
        try:
            # Попытка конвертации в float
            float(item)
        except ValueError:
            print(f"Ошибка: элемент '{item}' не является числом.")
            return False

    # 3. Пакет успешно прошел проверку
    return True
def read_data():
    global buffer
    try:

        rx = serial.readLine()
        rxs = str(rx, 'utf-8', errors='ignore')
        buffer += rxs

        if ';' in buffer:
            packets = buffer.split(';')
            for packet in packets[:-1]:
                if packet:
                    data = packet.strip().split(",")
                    if all(item != '' for item in data):
                        if validate_data_packet(data):
                            try:
                                add_exl_info()
                                pia(data)
                            except Exception as e:
                                print(e)
                                print(f"Пакет данных из сериал порта при неуспешной попытке обработке: {data}")

            buffer = packets[-1]
    except Exception as e:
        traceback.print_exc(f"что то пошло не так с вводом данных {buffer} \n {e}")
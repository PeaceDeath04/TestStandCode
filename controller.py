from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from saving import JsonHandler
import traceback
from ProjectProcessing import processing


class Controller:
    def __init__(self, log_function=None):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.buffer = ""
        self.log_function = log_function
        self.processing = processing(self.serial)
        self.save = JsonHandler()


    def open_port(self, port_name):
        # Закрываем текущий порт, если он открыт
        if self.serial.isOpen():
            if self.serial.portName() != port_name:
                self.serial.close()
                print(f"Закрытие порта {self.serial.portName()} перед открытием нового")

        # Устанавливаем и открываем новый порт
        self.serial.setPortName(port_name)
        if self.serial.open(QIODevice.ReadWrite):
            return f"Порт {port_name} открыт"
        else:
            return f"Не удалось открыть порт {port_name} , т.к он уже используется"

    def close_port(self):
        if self.serial.isOpen():
            self.serial.close()
            return "Порт закрыт"
        return "Порт уже закрыт"

    def update_port_list(self):
        ports = QSerialPortInfo.availablePorts()
        return [port.portName() for port in ports]

    def read_data(self):
        try:
            rx = self.serial.readAll()
            rxs = str(rx, 'utf-8', errors='ignore')
            self.buffer += rxs

            if ';' in self.buffer:
                packets = self.buffer.split(';')
                for packet in packets[:-1]:
                    if packet:
                        data = packet.strip().split(",")
                        if all(item != '' for item in data):
                            try:
                                self.save.ardu_to_json(data)
                            except AttributeError:
                                self.save.create_json()
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc()

    def get_gas_percentage(self):
        try:
            a = self.save.import_local_data("gas_min")
            b = self.save.import_local_data("gas_max")
            c = self.save.import_local_data("gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"


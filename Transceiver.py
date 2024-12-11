from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice


class Transceiver:
    def __init__(self,controller):
        self.controller = controller

        # Экземпляр класса для работы с портами
        self.port_handler = PortHandler(speed_baud_rate=9600)

        # буффер вспомогательная строка для чтения по com порту
        self.buffer = ""

        # словарь для работы с передачей данных на ардуино по com порту
        self.keysArduino = {"gas": "g", "gas_min": "m", "gas_max": "x", "ButCalibMotor": "k", "ResetTime": "t",
                            "Traction": "r", "Weight_1": "o", "Weight_2": "w"}

        # подключаем событие если сериал порт открыт и готов к чтению/отправке
        self.port_handler.serial.readyRead.connect(self.read_data)

    # статический метод для проверки валидности пакета с ардуино
    @staticmethod
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

    def read_data(self):
        try:

            rx = self.serial.readLine()
            rxs = str(rx, 'utf-8', errors='ignore')
            self.buffer += rxs

            if ';' in self.buffer:
                packets = self.buffer.split(';')
                for packet in packets[:-1]:
                    if packet:
                        data = packet.strip().split(",")
                        if all(item != '' for item in data):
                            if self.validate_data_packet(data):
                                self.controller.local_data.create_pack(data)

                self.buffer = packets[-1]
        except Exception as e:
            print(f"что то пошло не так с вводом данных {self.buffer} \n {e}")

    def send_data(self, **packet_data):
        if not self.serial.isOpen():
            print("Откройте порт перед отправкой")
            return

        for key_packet, value in packet_data.items():
            key_ard = self.keysArduino.get(key_packet)
            if key_ard:
                result = key_ard + str(value)
                self.serial.write(result.encode())
            else:
                print(f"Не найдено соответствие для {key_packet}")

class PortHandler:
    def __init__(self,speed_baud_rate = 9600):
        # Экземпляр класса по работе с сериал портом
        self.serial = QSerialPort()
        self.serial.setBaudRate(speed_baud_rate)

    def open_port(self,port_name):
        # Закрываем текущий порт, если он открыт
        if self.serial.isOpen():
            if self.serial.portName() != port_name:
                self.serial.close()
                print(f"Закрытие порта {self.serial.portName()} перед открытием нового")

        # Устанавливаем и открываем новый порт
        self.serial.setPortName(port_name)
        if self.serial.open(QIODevice.ReadWrite):
            print(f"Порт {port_name} открыт")
        else:
            self.serial.close()
            print("закрыли текущий порт")

    def close_port(self):
        if self.serial.isOpen():
            self.serial.close()
            return "Порт закрыт"
        return "Порт уже закрыт"

    @staticmethod
    def update_port_list():
        ports = QSerialPortInfo.availablePorts()
        return [port.portName() for port in ports]
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from saving import JsonHandler
import traceback
from ProjectProcessing import processing
from Tables import Graph
from exl import DataRecorder
from multiprocessing import Process
import asyncio


class Controller:
    def __init__(self, log_function=None):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.buffer = ""
        self.log_function = log_function
        self.processing = processing(self.serial)
        self.save = JsonHandler()
        self.graphs = {}
        self.graph = Graph
        self.recorder = DataRecorder()
        self.add_graphs()
        self.asyncio = asyncio
        self.read_ready = False
        self.p1 = Process(target=self.add_thread_graphs, daemon=True)
        self.params_tenz_kef = {}
        self.calib_weight = 200

        self.dict_tar = {}

    def open_port(self, port_name):
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
                           if len(data) == 9:
                               try:
                                   self.pia(data)
                                   self.asyncio.run(self.add_exl_info(self.read_ready))
                               except AttributeError:
                                   self.save.create_json(self.save.save_file, self.save.localData)
                               except Exception as e:
                                   print(e)
                                   print(f"Пакет данных из сериал порта при неуспешной попытке обработке: {data}")
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc(f"что то пошло не так с вводом данных {self.buffer} \n {e}")

    def but_taring(self,param):
        """Принимает параметр в строковом виде , который извлекает из LocalДаты и добавляет в словарь для тарирования"""
        if param == "Traction":
            self.dict_tar["Traction"] = self.save.localData.get("Traction")
            print(f"получили значение для тарирования{self.dict_tar['Traction']}")
        if param == "Weight":
            self.dict_tar["Weight_1"] = self.save.localData.get("Weight_1")
            self.dict_tar["Weight_2"] = self.save.localData.get("Weight_2")

    def pia(self,data):
        """ Processing Information from Arduino / обработка информации c arduino"""
        pia_data = {}
        # сохранили внутри метода пакет данных из сериал порта
        for key, value in zip(self.save.keys_to_update_ard, data):
            pia_data[key] = float(value)

        pia_data.update(self.taring_values(pia_data)) # производим тарирование

        pia_data.update(self.get_result_value(pia_data)) # производим деление параметров на коэф

        pia_data["Weight"] = (pia_data["Weight_1"] - pia_data["Weight_2"]) / 2 # получаем общий вес

        self.save.localData.update(pia_data) # сохраняем в локал дату обработанный пакет данных

        self.p1.run() # отрисовка графика в отдельном процессе

    def taring_values(self,packet_data):
        if self.dict_tar is not None:
            for key_packet, value_packet in packet_data.items():
                for key_tar, value_tar in self.dict_tar.items():
                    if key_tar == key_packet:
                        packet_data[key_packet] -= value_tar
        return packet_data

    def get_result_value(self,pia_data):
        """производим деление параметров на их коэффициенты если таковы имеются"""
        if self.params_tenz_kef: # проверка на наличие коэффицентов в словаре
            for key,value_kef in self.params_tenz_kef.items(): # получаем все ключи и их значения в словаре
                current_value = pia_data.get(key) # получаем текущее необработанное число
                current_value /= value_kef # производим деление на коэф
                pia_data[key] = current_value # обновляем значение по ключу в словаре для return
        return pia_data

    def get_kef_tenz(self,key_value):
        """Получаем ключ в виде строки"""
        if key_value == "Traction":
            self.params_tenz_kef["Traction"] = self.save.localData.get("Traction") / self.calib_weight

        if key_value == "Weight":
            self.params_tenz_kef["Weight_1"] = self.save.localData.get("Weight_1") / self.calib_weight
            self.params_tenz_kef["Weight_2"] = self.save.localData.get("Weight_2") / self.calib_weight

    async def add_exl_info(self,read):
        if read:
            data = self.save.localData.copy()
            self.recorder.save_to_csv(data=data)

    def add_thread_graphs(self):
        for nameGraph, params in self.graphs.items():
            self.update_graph(params.get("ObjectClass"), params.get("x"), params.get("y"))

    def update_graph(self,graph,xlabel,ylabel):
            """Метод принимает обьект класса Graph (график matplotlib) и 2 стринговых параматра на основании которых ищет в локал дате значения """
            x, y = self.save.localData.get(xlabel) , self.save.localData.get(ylabel)
            if xlabel == "Time":
                x = x/ 1000
            graph.ax.set_xlabel(xlabel)
            graph.ax.set_ylabel(ylabel)
            graph.line.set_label(ylabel)
            graph.add_data(x=x, y=y,name=f"{ylabel} = {y}")

    def get_gas_percentage(self):
        try:
            a , b , c = self.save.import_from_json("gas_min","gas_max","gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    def add_graphs(self):
        try:
            dict_js = self.save.import_js("keys_graphs.json")
            self.graphs = dict_js.copy()
        except :
            print("пусто")

        for nameGraph in self.graphs:
            self.graphs[nameGraph]["ObjectClass"] = Graph()
        for nameGraph, params in self.graphs.items():
            graph = self.graphs[nameGraph].get("ObjectClass")
            graph.ax.set_xlabel(self.graphs[nameGraph].get("x"))
            graph.ax.set_ylabel(self.graphs[nameGraph].get("y"))
            graph.line.set_label(self.graphs[nameGraph].get("y"))
        #print(self.graphs)



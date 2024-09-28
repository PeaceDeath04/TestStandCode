from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from Data import JsonHandler
import traceback
from ProjectProcessing import processing
from Tables import Graph
import threading
from exl import DataRecorder
#from line_profiler import profile
import asyncio


class Controller:
    def __init__(self, log_function=None):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.buffer = ""
        self.log_function = log_function
        self.processing = processing(self.serial)
        self.data = JsonHandler()
        self.graphs = {}
        self.graph = Graph
        self.recorder = DataRecorder()
        self.add_graphs()
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
        else:
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
                            if data == 9:
                                try:
                                    self.pia(data)
                                except AttributeError:
                                    self.data.create_json(self.data.save_file, self.data.localData)
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc(f"что то пошло не так с вводом данных {self.buffer} \n {e}")

    def but_calib_tract(self):
        self.data.Tar = self.data.localData.get("Traction")

    def pia(self,data):
        """ Processing Information from Arduino / обработка информации c arduino"""
        piaData = {}
        #сохранили внутри метода пакет данных из сериал порта
        if len(data) == 9:
            for key, value in zip(self.data.keys_to_update_ard, data):
                piaData[key] = float(value)

        w1 = piaData["Weight_1"]
        w2 = piaData["Weight_2"]
        tArdu = piaData.get("Traction")

        weight = (w1 - w2) /2
        traction = tArdu - self.data.Tar

        for key in ["Weight_1", "Weight_2", "Traction"]:
            del piaData[key]
        piaData.update(Weight= weight,Traction = traction)
        self.data.localData = piaData

    def add_exl_info(self):
        with self.lock:
            data = self.data.localData.copy()
            self.recorder.save_to_csv(data=data)

    def update_graph(self,graph,xlabel,ylabel):
            """Метод принимает обьект класса Graph (график matplotlib) и 2 стринговых параматра на основании которых ищет в локал дате значения """
            x , y = self.data.localData.get(xlabel) , self.data.localData.get(ylabel)
            if xlabel == "Time":
                x = x/ 1000
            graph.ax.set_xlabel(xlabel)
            graph.ax.set_ylabel(ylabel)
            graph.line.set_label(ylabel)
            graph.add_data(x=x, y=y,name=f"{ylabel} = {y}")

    def get_gas_percentage(self):
        try:
            a , b , c = self.data.import_from_json("gas_min", "gas_max", "gas")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    def add_graphs(self):
        self.graphs = self.data.import_js("keys_graphs.json").copy()

        for nameGraph in self.graphs:
            self.graphs[nameGraph]["ObjectClass"] = Graph()
        for nameGraph, params in self.graphs.items():
            graph = self.graphs[nameGraph].get("ObjectClass")
            graph.ax.set_xlabel(self.graphs[nameGraph].get("x"))
            graph.ax.set_ylabel(self.graphs[nameGraph].get("y"))
            graph.line.set_label(self.graphs[nameGraph].get("y"))
        #print(self.graphs)





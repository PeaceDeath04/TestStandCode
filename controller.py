from time import sleep

from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from fontTools.varLib.avarPlanner import WEIGHTS

from saving import JsonHandler
import traceback
from ProjectProcessing import processing
from Tables import Graph
import threading
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
        self.p1 = Process(target=self.addThreadGraphs, daemon=True)

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
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc(f"что то пошло не так с вводом данных {self.buffer} \n {e}")

    def butCalibration(self,param):
        """Принимает параметр в строковом виде , который извлекает из LocalДаты и добавляет в словарь для тарирования"""
        self.dict_tar[param] = self.save.localData.get(param)
        print(f"веса для тарирования (ими вычитаем) {self.dict_tar}")

    def pia(self,data):
        """ Processing Information from Arduino / обработка информации c arduino"""
        piaData = {}
        # сохранили внутри метода пакет данных из сериал порта
        for key, value in zip(self.save.keys_to_update_ard, data):
            piaData[key] = float(value)

        # словарь параметров в унциях
        dict_units = {"Weight_1": piaData["Weight_1"],
                      "Weight_2": piaData["Weight_2"],
                      "Traction": piaData.get("Traction")}

        for key_unc, value_unc in dict_units.items():
            dict_units[key_unc] = value_unc * 28.3495

        dict_units["Weight"] = (dict_units["Weight_1"] - dict_units["Weight_2"]) / 2
        if self.dict_tar is not None:
            for key_unit, value_unit in dict_units.items():
                for key_tar, value_tar in self.dict_tar.items():
                    if key_tar == key_unit:
                        dict_units[key_unit] -= value_tar

        piaData.update(dict_units)
        self.save.localData.update(piaData)
        self.p1.run()

    def calib_value(self,key_value):
        """Получаем ключ в виде строки"""
        if key_value == "Traction":
            value = (self.save.localData.get(key_value) / 200)
            self.processing.TxToARDU(Traction=value)

        if key_value == "Weight":
            w1 = (self.save.localData.get("Weight_1") / 200)
            w2 = (self.save.localData.get("Weight_2") / 200)
            self.processing.TxToARDU(Weight_1=w1,Weight_2 = w2)

    async def add_exl_info(self,read):
        if read:
            data = self.save.localData.copy()
            self.recorder.save_to_csv(data=data)

    def addThreadGraphs(self):
        for nameGraph, params in self.graphs.items():
            self.updateGraph(params.get("ObjectClass"), params.get("x"), params.get("y"))

    def updateGraph(self,graph,xlabel,ylabel):
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



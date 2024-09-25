from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from saving import JsonHandler
import traceback
from ProjectProcessing import processing
from Tables import Graph
import threading
from exl import DataRecorder


class Controller:
    def __init__(self, log_function=None):
        self.Graph = Graph
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        self.buffer = ""
        self.log_function = log_function
        self.processing = processing(self.serial)
        self.save = JsonHandler()
        self.graphs = {}
        self.objects_graphs = []
        self.add_graphs()
        self.recorder = DataRecorder()
        self.lock = threading.Lock()



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
                            try:
                                self.pia(data)
                                self.addThreadGraphs()
                                self.addThreadExl()
                            except AttributeError:
                                self.save.create_json(self.save.save_file, self.save.paramData)
                self.buffer = packets[-1]
        except Exception as e:
            traceback.print_exc(f"что то пошло не так с вводом данных {self.buffer} \n {e}")

    def butCalibTract(self):
        self.save.Tar = self.save.paramData.get("Traction")

    def pia(self,data):
        """ Processing Information from Arduino / обработка информации c arduino"""
        piaData = {}
        #сохранили внутри метода пакет данных из сериал порта
        if len(data) == 9:
            for key, value in zip(self.save.keys_to_update_ard, data):
                piaData[key] = float(value)

        w1 = piaData["Weight_1"]
        w2 = piaData["Weight_2"]
        weight = (w1 - w2) /2

        tPy = self.save.import_local_data("Traction")[0]
        tArdu = piaData.get("Traction")
        traction = tArdu - self.save.Tar

        for key in ["Weight_1", "Weight_2", "Traction"]:
            del piaData[key]
        piaData.update(mainWeight= weight,Traction = traction)
        self.save.export_local_data(piaData)

    def addThreadExl(self):
        exl_thread = threading.Thread(target=self.add_exl_info)
        exl_thread.start()

    def add_exl_info(self):
        with self.lock:
            data = self.save.paramData.copy()
            self.recorder.save_to_csv(data=data)

    def addThreadGraphs(self):
        # Запускаем апдейт графиков в отдельном потоке
        """Этот метод получает Название Графика и сам обьект \n
         -------  \n
         После получает словарь Графиков где есть названия графиков и их параметры \n
         -------- \n
         Метод их сравнивает и при совпадении создает отдельный поток который их обновляет
        """
        for nameGraph, params in self.graphs.items():
            graph_thread = threading.Thread(target=self.updateGraph, args=(params.get("ObjectClass"), params.get("x"), params.get("y")))
            graph_thread.start()

    def updateGraph(self,graph,xlabel,ylabel):
        """Метод принимает обьект класса Graph (график matplotlib) и 2 стринговых параматра на основании которых ищет в локал дате значения """
        x, y = self.save.paramData.get(xlabel),self.save.paramData.get(ylabel)
        if xlabel == "Time":
            x = x/ 1000
        graph.add_data(x=x, y=y,name=f"{ylabel} = {y}")



    def get_gas_percentage(self):
        try:
            a , b , c = self.save.import_data("gas_min","gas_max","gas",name_save_file="save_file.json")
            per = ((c - a) / (b - a)) * 100
            return (round(per))
        except:
            return "Ошибка при вычилсении процента"

    def add_graphs(self):
        dict_js = self.save.import_js("keys_graphs.json")
        self.graphs = dict_js.copy()

        for nameGraph in self.graphs:
            self.graphs[nameGraph]["ObjectClass"] = Graph()
        for nameGraph,params in self.graphs.items():
            graph = self.graphs[nameGraph].get("ObjectClass")
            graph.ax.set_xlabel(self.graphs[nameGraph].get("x"))
            graph.ax.set_ylabel(self.graphs[nameGraph].get("y"))
            graph.line.set_label(self.graphs[nameGraph].get("y"))



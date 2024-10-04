from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from saving import *
import traceback
# from ProjectProcessing import processing
from Tables import Graph
from exl import DataRecorder
from multiprocessing import Process
import asyncio

serial = QSerialPort()
serial.setBaudRate(9600)
buffer = ""
graphs = {}
graph = Graph
recorder = DataRecorder()
asyncio = asyncio
read_ready = False
params_tenz_kef = {}
calib_weight = 62.5
dict_tar = {}





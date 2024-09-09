import json
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import sys
from Window import Ui_MainWindow
import asyncio
from saving import ExportToJson,ImportFromJson

#region Переменные
gas_min = 0 #безразмерная
gas_max = 50 #безразмерная
gas = 0 #безразмерная
T_flach_E = 0 #время одного оборота двигателя в микросекундах
T_flash_O = 0 #время между срабатыванием датчика
Voltage = 0.00 #вольт
ShuntVoltage = 0.000 #вольт
Temp = 0.0 #градусов
Traction = 0.0 #грамм
Weight_1 = 0.0 #грамм
Weight_2 = 0.0 #грамм
#region вычисления
current = (ShuntVoltage * 0.075) / 75 # значение силы тока
#flach_E = 60000000 // T_flach_E #обороты в минуту
Time_flash_O = T_flash_O * 2 #время 1 оборота двигателя в микросекундах
#flach_O = 60000000 // Time_flash_O #обороты в минуту с оптического датчика
#endregion
#endregion

#region Инициализация

serial = QSerialPort()
serial.setBaudRate(115200)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.SlidePower.setMinimum(ImportFromJson("gas_min"))
ui.spinBoxMin.setValue(ImportFromJson("gas_min"))
ui.SlidePower.setMaximum(ImportFromJson("gas_max"))
ui.spinBoxMax.setValue(ImportFromJson("gas_max"))


#endregion

#region тарирование тензодатчиков
cargo = 200 # вес груза в граммах
def calibration_Tract():
    tar_1 = Traction
    tar_Traction = Traction - tar_1
def calibration_Weight():
    tar_2 = Weight_1 - cargo
    tar_3 = Weight_2 - cargo
    tar_Weight_1 = Weight_1 - tar_2
    tar_Weight_2 = Weight_2 - tar_3
#endregion

#region список портов
def UpdatePortList():
    port_list = []
    ports = QSerialPortInfo.availablePorts()
    for port in ports:
        port_list.append(port.portName())
    ui.ListPorts.addItems(port_list)

UpdatePortList()
#endregion

#region методы определения кнопнок

def openPort():
    serial.setPortName(ui.ListPorts.currentText())
    serial.open(QIODevice.ReadWrite)
    print(f"Порт:",ui.ListPorts.currentText(),"открыт")


def closeport():
    serial.close()
    print("Порт:", ui.ListPorts.currentText(), "закрыт")

def getValue():
    gas = ui.SlidePower.value()
    ExportToJson("gas",gas)

def GetRangeGas(min):
    if min == True:
        gas_min = ui.spinBoxMin.value()
        ui.SlidePower.setMinimum(gas_min)
        ExportToJson("gas_min",gas_min)
    else:
        gas_max = ui.spinBoxMax.value()
        ui.SlidePower.setMaximum(gas_max)
        ExportToJson("gas_max",gas_max)



ui.ButOpenPort.clicked.connect(openPort)
ui.ButClosePort.clicked.connect(closeport)
ui.SlidePower.valueChanged.connect(getValue)

ui.spinBoxMin.valueChanged.connect(lambda :GetRangeGas(True))
ui.spinBoxMax.valueChanged.connect(lambda :GetRangeGas(False))


#endregion


if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())

    # для Димы:
    # на графики по оси y нужно выводить значения следующих переменных: tar_Traction, current, flach_E, flach_O, Voltage, Temp, tar_Weight_1, tar_Weight_2
    # графики доложны быть широко растянуты по x. Фон графиков белый и цвет линии у кажлого графика должен быть свой
    # добавь 2 кнопки которые будут вызввать функции calibration_Tract() и calibration_Weight
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import sys
from Window import Ui_MainWindow
from saving import ExportToJson, ImportFromJson, ArduToJson
from ProjectProcessing import TxToARDU




#region Инициализация

serial = QSerialPort()
serial.setBaudRate(115200)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.onStartUp(ImportFromJson("gas_min"), ImportFromJson("gas_max"), ImportFromJson("gas"))




#endregion

#region методы определения кнопнок

def OnRead():
    rx = serial.readLine()
    rxs =str(rx,'utf-8').strip()
    data = rxs.split(",")
    for i in data:
        ArduToJson(i)

def GetProsent():
    try:
        a = ImportFromJson("gas_min")
        b = ImportFromJson("gas_max")
        c = ImportFromJson("gas")
        per = (c-a)/(b-a) *100
        return round(per)
    except:
        print("ошибка при вычислении")

def UpdatePortList():
    ui.ListPorts.clear()
    port_list = []
    ports = QSerialPortInfo.availablePorts()
    for port in ports:
        port_list.append(port.portName())
    ui.ListPorts.addItems(port_list)

def openPort():
    if not serial.isOpen():
        serial.setPortName(ui.ListPorts.currentText())
        serial.open(QIODevice.ReadWrite)
        print(f"Порт:", ui.ListPorts.currentText(), "открыт")
    else:
        print(f"Порт: {ui.ListPorts.currentText()} Уже открыт")


def closeport():
    if serial.isOpen():
        serial.close()
        print("Порт:", ui.ListPorts.currentText(), "закрыт")
    else:
        print(f"Порт: {ui.ListPorts.currentText()} Уже закрыт")

def getValue():
    prozent = GetProsent()
    gas = ui.SlidePower.value()
    ui.valueGas.setText(str(prozent))
    TxToARDU("o", gas)
    ExportToJson("gas",gas)

def GetRangeGas():
    gas_min = ui.spinBoxMin.value()
    ui.SlidePower.setMinimum(gas_min)
    TxToARDU("i", gas_min)
    ExportToJson("gas_min", gas_min)

    gas_max = ui.spinBoxMax.value()
    ui.SlidePower.setMaximum(gas_max)
    TxToARDU("a", gas_max)
    ExportToJson("gas_max", gas_max)

serial.readyRead.connect(OnRead)
ui.butRefresh.clicked.connect(UpdatePortList)
ui.ButOpenPort.clicked.connect(openPort)
ui.ButClosePort.clicked.connect(closeport)
ui.SlidePower.valueChanged.connect(getValue)

ui.spinBoxMin.valueChanged.connect(GetRangeGas)
ui.spinBoxMax.valueChanged.connect(GetRangeGas)
ui.ButCalibration.clicked.connect(lambda :TxToARDU('k',0))


#endregion


if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())

    """
    self.spinBoxMin.setValue(ImportFromJson("gas_min"))
    self.spinBoxMax.setValue(ImportFromJson("gas_max"))
    self.SlidePower.setMaximum(ImportFromJson("gas_max"))
    self.SlidePower.setMinimum(ImportFromJson("gas_min"))
    self.SlidePower.setValue(ImportFromJson("gas"))
    self.SlidePower.setProperty("value", 50)
    """

    # для Димы:
    # на графики по оси y нужно выводить значения следующих переменных: tar_Traction, current, flach_E, flach_O, Voltage, Temp, tar_Weight_1, tar_Weight_2
    # графики доложны быть широко растянуты по x. Фон графиков белый и цвет линии у кажлого графика должен быть свой
    # добавь 2 кнопки которые будут вызввать функции calibration_Tract() и calibration_Weight
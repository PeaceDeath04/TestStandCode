from PyQt5.QtSerialPort import QSerialPortInfo,QSerialPort
from PyQt5.QtCore import QIODevice
import sys
from Window import ui,app,MainWindow
from saving import ExportToJson, ImportFromJson, ArduToJson
from ProjectProcessing import TxToARDU

serial = QSerialPort()
serial.setBaudRate(115200)
ui.onStartUp(ImportFromJson("gas_min"),ImportFromJson("gas_max"),ImportFromJson("gas"))

def OnRead():
    rx = serial.readLine()
    rxs =str(rx,'utf-8').strip()
    data = rxs.split(",")
    data = data[:-1]
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
        ui.sendDb("ошибка при вычислении")

def UpdatePortList():
    ui.ListPorts.clear()
    port_list = []
    ports = QSerialPortInfo.availablePorts()
    for port in ports:
        port_list.append(port.portName())
    ui.ListPorts.addItems(port_list)
    ui.sendDb("Список портов обновлен")

def openPort():
    if not serial.isOpen():
        serial.setPortName(ui.ListPorts.currentText())
        serial.open(QIODevice.ReadWrite)
        ui.sendDb(f"Порт:{ui.ListPorts.currentText()} открыт")
    else:
        ui.sendDb(f"Порт: {ui.ListPorts.currentText()} Уже открыт")

def closeport():
    if serial.isOpen():
        serial.close()
        ui.sendDb(f"Порт: {ui.ListPorts.currentText()} закрыт")
    else:
        ui.sendDb(f"Порт: {ui.ListPorts.currentText()} Уже закрыт")

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

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())
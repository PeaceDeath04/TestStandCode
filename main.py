from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import sys
from Window import Ui_MainWindow

#region Переменные
gas_min = 0
gas = 0
gas_max = 50

flach_E = 0
flash_O = 0

Voltage = 0
ShuntVoltage = 0

Temp = 0

Traction = 0

Weight_1 = 0
Weight_2 = 0
#endregion

#region Инициализация
serial = QSerialPort()
serial.setBaudRate(115200)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
#endregion

#region список портов
port_list = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    port_list.append(port.portName())
ui.ListPorts.addItems(port_list)
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
    global gas # будет пофикшено
    print(gas)
    gas = ui.SlidePower.value()






ui.ButOpenPort.clicked.connect(openPort)
ui.ButClosePort.clicked.connect(closeport)

ui.SlidePower.setMinimum(gas_min)
ui.SlidePower.setMaximum(gas_max)
ui.SlidePower.valueChanged.connect(getValue)




#endregion


if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())
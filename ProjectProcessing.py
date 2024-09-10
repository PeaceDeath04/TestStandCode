from saving import ExportToJson,ImportFromJson
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


serial = QSerialPort()
serial.setBaudRate(115200)

#калибровка тяги
def calibration_Tract(object_weight):
    return (object_weight-object_weight)

# значение силы тока
def GetValueCurrent(ShuntVoltage):
    return ((ShuntVoltage * 0.075) / 75)

#посылаем на ардуинку
def TxToARDU(string,gas_int):
    string += str(gas_int)
    serial.write(string.encode())

#получаем Rpm Rotate per min / оборотов в минуту
def TakeRpmE(t_flach):
    try:
        return (60000000 // t_flach)
    except:
        return 0

def TakeRpm0(t_flach):
    t_flach *=2
    return (TakeRpmE(t_flach))


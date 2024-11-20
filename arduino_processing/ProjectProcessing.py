from data_processing.Data import keysArduino
from .SerialManager import serial


def GetValueCurrent(ShuntVoltage):
    return ((ShuntVoltage * 0.075) / 75)


# посылаем на ардуинку
def TxToARDU(**packet_data):
    for key_packet, value in packet_data.items():
        for name_key, key_ard in keysArduino.items():
            if name_key == key_packet:
                result = key_ard + str(value)
                serial.write(result.encode())



# получаем Rpm Rotate per min / оборотов в минуту
def TakeRpmE(t_flach):
    try:
        return (60000000 // t_flach)
    except:
        return 0


def TakeRpm0(t_flach):
    t_flach *= 2
    return (TakeRpmE(t_flach))
class processing():
    def __init__(self,serial):
        self.serial =serial
    def calibration_Tract(self,object_weight):
        return (object_weight - object_weight)

    def GetValueCurrent(self,ShuntVoltage):
        return ((ShuntVoltage * 0.075) / 75)

    # посылаем на ардуинку
    def TxToARDU(self,**packet_data):
        for string,value in packet_data.items():
            string += str(value)
            self.serial.write(string.encode())

    # получаем Rpm Rotate per min / оборотов в минуту
    def TakeRpmE(self,t_flach):
        try:
            return (60000000 // t_flach)
        except:
            return 0

    def TakeRpm0(self,t_flach):
        t_flach *= 2
        return (self.TakeRpmE(t_flach))


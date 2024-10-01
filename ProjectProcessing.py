class processing():
    def __init__(self,serial):
        self.keysArduino = {"gas": "g", "gas_min": "m", "gas_max": "x", "ButCalibMotor": "k", "ResetTime": "t",
                            "Traction": "r", "Weight_1": "o", "Weight_2": "w"}
        self.serial =serial

    def GetValueCurrent(self,ShuntVoltage):
        return ((ShuntVoltage * 0.075) / 75)

    # посылаем на ардуинку
    def TxToARDU(self,**packet_data):
        for key_packet,value in packet_data.items():
            for name_key,key_ard in self.keysArduino.items():
                if name_key == key_packet:
                    result = key_ard + str(value)
                    self.serial.write(result.encode())

    # получаем Rpm Rotate per min / оборотов в минуту
    def TakeRpmE(self,t_flach):
        try:
            return (60000000 // t_flach)
        except:
            return 0

    def TakeRpm0(self,t_flach):
        t_flach *= 2
        return (self.TakeRpmE(t_flach))


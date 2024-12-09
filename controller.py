from Transceiver import Transceiver
from DataControl import *



class Controller:
    def __init__(self):
        self.local_data = Data()
        self.transceiver = Transceiver(controller=self.local_data.create_pack)
        self.recorder = DataRecorder()

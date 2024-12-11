from Transceiver import Transceiver
from UI.UI_Controller import UiController
from DataControl import *


class Controller:
    def __init__(self):
        self.local_data = Data()
        self.transceiver = Transceiver(controller=self)
        self.recorder = DataRecorder()
        self.ui_controller = UiController(self)

    def save_ui_values(self):
        controller = self.ui_controller
        export_to_json("save_file.json",gas_min=controller.ui_main.spinBoxMin,gas_max=controller.ui_main.spinBoxMax,step_size=controller.step_size)

    #region работа с Трансивером
    def open_port(self,port_name):
        self.transceiver.port_handler.open_port(port_name=port_name)
        return self.transceiver.port_handler.serial.isOpen()

    def close_port(self):
        self.transceiver.port_handler.close_port()
        return self.transceiver.port_handler.serial.isOpen()

    def update_port_list(self):
        return self.transceiver.port_handler.update_port_list()
    #endregion
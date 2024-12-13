from PyQt5.QtTest import QTest

from GraphHandlers import GraphController
from Transceiver import Transceiver
from UI.UI_Controller import UiController
from DataControl import *



class Controller:
    def __init__(self):
        self.local_data = Data()
        self.transceiver = Transceiver(controller=self)
        self.recorder = DataRecorder()
        self.ui_controller = UiController(self)
        self.graph_controller = GraphController()

    def save_ui_values(self):
        controller = self.ui_controller
        export_to_json("save_file.json",gas_min=controller.ui_main.spinBoxMin,gas_max=controller.ui_main.spinBoxMax,step_size=controller.step_size,calib_weight=self.local_data.calib_weight)

    #region работа с записью параметров и автотестом
    def switch_recording(self):
        if not self.recorder.is_reading:
            self.recorder.start_new_recording()
            self.ui_controller.ui_main.ButSaveExl.setText("Остановить запись параметров")
        else:
            self.recorder.convert_csv_to_xlsx()
            self.ui_controller.ui_main.ButSaveExl.setText("Начать запись параметров")

    def start_auto_test(self):
        # обнуляем время
        self.transceiver.send_data(ResetTime=0)

        # получаем временные точки для автотеста
        points = import_js("timings.json")

        # меняем дефолт название файла
        self.recorder.base_filename = "AutoTest"

        self.recorder.start_new_recording()

        # проводим автотест
        for point in points.values():
            for gas, time in point.items():
                gas, time = int(gas), int(time)
                gas = self.ui_controller.calculate_value_from_percentage(gas)
                self.ui_controller.ui_main.SlidePower.setValue(gas)
                QTest.qWait(ms=time)

        # прекращаем запись
        self.recorder.convert_csv_to_xlsx()
        self.ui_controller.ui_main.ButAutoTest.setText("Начать автотест")

    def recorder_is_run(self):
        return self.recorder.is_reading
    #endregion

    #region работа с портами (сокрытие)
    def open_port(self,port_name):
        self.transceiver.port_handler.open_port(port_name=port_name)
        return self.transceiver.port_handler.serial.isOpen()

    def close_port(self):
        self.transceiver.port_handler.close_port()
        return self.transceiver.port_handler.serial.isOpen()

    def update_port_list(self):
        return self.transceiver.port_handler.update_port_list()
    #endregion

    #region работа с Traction/Weight

    def set_value_for_taring(self,key_param):
        """Метод принимает и передает ключ для последющей обработки тарирования"""
        self.local_data.input_params_for_taring(key_param=key_param)

    def set_value_for_calib(self,key_param):
        """Метод принимает и передает ключ для последющей калибровки"""
        self.local_data.input_params_for_calib(key_param=key_param)

    #endregion
from PyQt5.QtTest import QTest

from GraphHandlers import GraphController
from Transceiver import Transceiver
from UI_Controller import UiController
from DataControl import *



class Controller:
    def __init__(self):
        self.local_data = Data()
        self.transceiver = Transceiver(controller=self)
        self.recorder = DataRecorder()
        self.ui_controller = UiController(self)
        self.graph_controller = GraphController()

        if not os.path.exists(json_dir):
            os.makedirs(json_dir)

            create_json(name_file="keys_graphs.json",data=None)
            create_json(name_file="ToRead.json",data=None)
            create_json(name_file="timings.json",data=None)
            create_json(name_file="save_file.json",data=None)

        if not os.path.exists(exel_dir):
            os.makedirs(exel_dir)

        self.ui_controller.OnStartUp()

    def save_ui_values(self):
        controller = self.ui_controller
        print(controller.ui_main.spinBoxMin.value())
        export_to_json("save_file.json", gas_min=controller.ui_main.spinBoxMin.value(), gas_max=controller.ui_main.spinBoxMax.value(),
                       step_size=controller.step_size, calib_weight=self.local_data.calib_weight)


    def get_packet(self,packet):
        """Метод вызывается при получении с арудино *грязного пакета*"""
        self.local_data.create_pack(packet)

        if self.recorder.is_reading:
            self.recorder.save_to_csv(self.local_data.packet.data)


        #обновляем графики
        self.graph_controller.update_graphs(self.local_data.packet)

    def offset_gas_changed(self,gas_min,gas_max):
        """Вызывается при измении газа"""
        self.transceiver.send_data(gas_min=gas_min, gas_max=gas_max)

    def gas_changed(self,gas):
        """Вызывается при изменениии газа"""
        self.transceiver.send_data(gas=gas)


    def switch_recording(self):
        """Метод включает и выключает запись параметров"""
        if not self.recorder.is_reading:
            self.recorder.start_new_recording()
            self.ui_controller.ui_main.ButSaveExl.setText("Остановить запись параметров")
        else:
            self.recorder.convert_csv_to_xlsx()
            self.ui_controller.ui_main.ButSaveExl.setText("Начать запись параметров")

    def start_auto_test(self):
        """При вызове метода начинает автотест"""
        if not self.recorder.is_reading:
            self.ui_controller.ui_main.ButAutoTest.setText("Проводится автотест")
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


    def open_port(self,port_name):
        self.transceiver.port_handler.open_port(port_name=port_name)
        return self.transceiver.port_handler.serial.isOpen()

    def close_port(self):
        self.transceiver.port_handler.close_port()
        return self.transceiver.port_handler.serial.isOpen()

    def update_port_list(self):
        return self.transceiver.port_handler.update_port_list()


    def set_value_for_taring(self,key_param):
        """Метод принимает и передает ключ для последющей обработки тарирования"""
        self.local_data.input_params_for_taring(key_param=key_param)

    def set_value_for_calib(self,key_param):
        """Метод принимает и передает ключ для последющей калибровки"""
        self.local_data.input_params_for_calib(key_param=key_param)

    def update_graphs_widget(self):
        """Метод обновляет отображаемые графики в UI"""
        if self.graph_controller.graphs:

            # очищаем все графики что были
            self.ui_controller.clear_layout(self.ui_controller.ui_main.graph_Layout)

            # получаем виджеты для pyqt
            widgets = self.graph_controller.get_widget_graphs()

            # добавляем виджеты
            for widget in widgets:
                self.ui_controller.ui_main.graph_Layout.addWidget(widget)





from .UI import SettingsWindow,MainWindow

class UiController:
    def __init__(self):
        self.ui_main = MainWindow()
        self.ui_settings = SettingsWindow()
        self.setup_ui()

    def setup_ui(self):
        self.ui_main.setupUi(self.ui_main)
        self.ui_settings.setupUi(self.ui_settings)

    def add_graph(self):
        """Метод для добавления обьекта класса Graph на ui слой в главном окне"""


    def connect_events_main(self):
        pass

    def connect_events_settings(self):
        pass




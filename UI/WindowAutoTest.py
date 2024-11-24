from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton, QHBoxLayout
)

class IterationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QWidget {\n"
                                 "        background-color: #1e1e1e;  /* Очень темный фон */\n"
                                 "        color: #d3d3d3;  /* Светло-серый цвет текста */\n"
                                 "        font-family: Arial, sans-serif;\n"
                                 "        font-size: 12px;\n"
                                 "    }\n"
                                 "    QPushButton {\n"
                                 "        background-color: #2d2d2d;  /* Темный фон для кнопок */\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 5px;\n"
                                 "        font-weight: bold;\n"
                                 "    }\n"
                                 "    QPushButton:hover {\n"
                                 "        background-color: #00b894;  /* Светло-зеленый при наведении */\n"
                                 "        color: #1e1e1e;\n"
                                 "    }\n"
                                 "    QComboBox {\n"
                                 "        border: 1px solid #2d2d2d;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        background-color: #2d2d2d;\n"
                                 "    }\n"
                                 "    QTextBrowser {\n"
                                 "        background-color: #2d2d2d;  /* Темный фон для окна вывода */\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 5px;\n"
                                 "    }\n"
                                 "    QLabel {\n"
                                 "        color: #d3d3d3;  /* Мягкий серый цвет для текста */\n"
                                 "        font-weight: bold;\n"
                                 "        font-size: 14px;\n"
                                 "    }\n"
                                 "    QSpinBox {\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        color: #d3d3d3;\n"
                                 "    }\n"
                                 "    QDoubleSpinBox{\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border: 1px solid #1e1e1e;\n"
                                 "        border-radius: 5px;\n"
                                 "        padding: 2px;\n"
                                 "        color: #d3d3d3;\n"
                                 "}\n"
                                 "\n"
                                 "    QSlider {\n"
                                 "        background-color: #2d2d2d;\n"
                                 "        border-radius: 5px;\n"
                                 "}")
        self.setWindowTitle("Ввод данных")
        self.layout = QVBoxLayout(self)
        self.init_ui()

        self.gas_values = []
        self.timings = []
        self.iterations = 0
        self.current_iteration = 0

    def init_ui(self):
        # Виджет для ввода количества итераций
        self.iteration_label = QLabel("Сколько должно быть итераций?")
        self.iteration_spinbox = QSpinBox()
        self.iteration_spinbox.setMinimum(1)

        self.start_button = QPushButton("Начать")
        self.start_button.clicked.connect(self.start_iterations)

        self.layout.addWidget(self.iteration_label)
        self.layout.addWidget(self.iteration_spinbox)
        self.layout.addWidget(self.start_button)

    def start_iterations(self):
        # Устанавливаем количество итераций
        self.iterations = self.iteration_spinbox.value()

        # Убираем виджеты ввода итераций
        self.iteration_label.hide()
        self.iteration_spinbox.hide()
        self.start_button.hide()

        # Создаем виджеты для ввода значений газа и времени
        self.gas_label = QLabel()
        self.gas_spinbox = QSpinBox()
        self.gas_spinbox.setMinimum(0)
        self.gas_spinbox.setMaximum(100000)

        self.time_label = QLabel()
        self.time_spinbox = QSpinBox()
        self.time_spinbox.setMinimum(1)
        self.time_spinbox.setMaximum(1000000)

        self.next_button = QPushButton("Далее")
        self.next_button.clicked.connect(self.next_iteration)

        # Добавляем виджеты на форму
        self.layout.addWidget(self.gas_label)
        self.layout.addWidget(self.gas_spinbox)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.time_spinbox)
        self.layout.addWidget(self.next_button)

        # Запускаем первую итерацию
        self.update_iteration_ui()

    def update_iteration_ui(self):
        # Обновляем текст для текущей итерации
        self.gas_label.setText(f"Какое количество газа (в процентах) подавать на {self.current_iteration + 1} итерации?")
        self.time_label.setText(f"Какое время ожидать (в мс) на {self.current_iteration + 1} итерации?")

    def next_iteration(self):
        # Сохраняем значения текущей итерации
        self.gas_values.append(self.gas_spinbox.value())
        self.timings.append(self.time_spinbox.value())

        self.current_iteration += 1

        if self.current_iteration < self.iterations:
            # Если итерации не закончились, обновляем UI
            self.update_iteration_ui()
        else:
            # Завершаем диалог
            self.accept()
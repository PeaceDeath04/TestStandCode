from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSlider, QVBoxLayout, QLabel, QSpinBox, QWidget


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Step Slider")
        self.setGeometry(100, 100, 800, 200)

        # Виджеты интерфейса
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Минимальное и максимальное значение задаются через SpinBox
        self.spinBoxMin = QSpinBox(self.centralwidget)
        self.spinBoxMin.setRange(0, 9999)
        self.spinBoxMin.setValue(0)
        self.spinBoxMin.valueChanged.connect(self.update_slider_range)

        self.spinBoxMax = QSpinBox(self.centralwidget)
        self.spinBoxMax.setRange(1, 9999)
        self.spinBoxMax.setValue(1000)
        self.spinBoxMax.valueChanged.connect(self.update_slider_range)

        # Слайдер
        self.SlidePower = QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.SlidePower.setRange(self.spinBoxMin.value(), self.spinBoxMax.value())
        self.SlidePower.valueChanged.connect(self.correct_slider_step)  # Коррекция шага при изменении значения

        # Отображение значения
        self.valueLabel = QLabel(f"Текущее значение: {self.SlidePower.value()}", self.centralwidget)

        # Расположение элементов
        layout = QVBoxLayout(self.centralwidget)
        layout.addWidget(self.spinBoxMin)
        layout.addWidget(self.spinBoxMax)
        layout.addWidget(self.SlidePower)
        layout.addWidget(self.valueLabel)

        # Начальная настройка шага
        self.update_slider_range()

    def update_slider_range(self):
        """Обновление диапазона слайдера при изменении Min и Max."""
        min_val = self.spinBoxMin.value()
        max_val = self.spinBoxMax.value()

        if min_val >= max_val:
            max_val = min_val + 1
            self.spinBoxMax.setValue(max_val)

        self.SlidePower.setRange(min_val, max_val)

        # Рассчитываем шаг на основе диапазона
        self.step_size = (max_val - min_val) // 10
        if self.step_size == 0:  # Защита от деления на 0
            self.step_size = 1

        self.correct_slider_step()  # Сразу скорректируем начальное значение слайдера

    def correct_slider_step(self):
        """Корректировка шага слайдера при изменении его значения."""
        current_value = self.SlidePower.value()
        corrected_value = round(current_value / self.step_size) * self.step_size
        self.SlidePower.blockSignals(True)  # Отключаем сигналы, чтобы избежать рекурсии
        self.SlidePower.setValue(corrected_value)  # Устанавливаем скорректированное значение
        self.SlidePower.blockSignals(False)  # Включаем сигналы обратно
        self.valueLabel.setText(f"Текущее значение: {self.SlidePower.value()}")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

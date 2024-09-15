from PyQt5.QtWidgets import QApplication
from Window import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
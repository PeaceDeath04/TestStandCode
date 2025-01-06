from PyQt5.QtWidgets import QApplication
import controller
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    control = controller.Controller()
    app.aboutToQuit.connect(control.save_ui_values)
    sys.exit(app.exec_())




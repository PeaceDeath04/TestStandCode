from PyQt5.QtWidgets import QApplication
from UI.Window import Ui_MainWindow
import sys
import osп
from globals import json_dir,exel_dir

if not os.path.exists(json_dir):
    os.makedirs(json_dir)
    print(f"папка создана по пути: {json_dir}")

if not os.path.exists(exel_dir):
    os.makedirs(exel_dir)
    print(f"папка создана по пути: {exel_dir}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())



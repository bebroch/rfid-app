# main.py
import sys
from PyQt5 import QtWidgets, uic

def load_stylesheet(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем интерфейс из .ui файла
        uic.loadUi("main_window.ui", self)

        # Применяем стиль
        self.setStyleSheet(load_stylesheet("styles.qss"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
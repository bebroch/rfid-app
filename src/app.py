import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.increment = 1

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.onClicked)

        self.setCentralWidget(self.button)


    def onClicked(self):
        self.button.setText('Press Me! ({})'.format(self.increment))
        self.increment+=1
        self.resize(200, 200)
        print("clicked") 



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
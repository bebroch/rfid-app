from app import MainWindow
from PyQt6.QtWidgets import QApplication
import sqlite3
import sys
from database.user_service import UserService


if __name__ == "__main__":
    app = QApplication(sys.argv)

    connection = sqlite3.connect("rfid_database.db")

    userService = UserService(connection)

    window = MainWindow(userService)
    window.show()
    app.exec()

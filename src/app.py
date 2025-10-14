import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView

from main_window import Ui_MainWindow
from table_model import TableModel

test_data = [
    ["98:27:F6:B5:FD:57", "Иванов Иван Иванович", "вход", "15:00 01.01.2023"],
    ["A4:C3:F2:18:9D:44", "Петров Петр Петрович", "выход", "15:00 02.01.2023"],
    ["BC:76:5E:3A:D1:9F", "Сидорова Мария Сергеевна", "вход", "15:00 03.01.2023"],
    ["D8:92:4A:7C:E5:33", "Козлов Алексей Владимирович", "выход", "15:00 04.01.2023"],
    ["E1:5B:9F:62:A8:7D", "Новикова Елена Дмитриевна", "вход", "15:00 05.01.2023"],
    ["F7:3C:8D:29:B4:16", "Морозов Дмитрий Игоревич", "выход", "15:00 06.01.2023"],
    ["2A:9E:C4:5F:87:21", "Волкова Анна Петровна", "вход", "15:00 07.01.2023"],
    ["4D:B1:6E:93:2C:58", "Семенов Сергей Васильевич", "выход", "15:00 08.01.2023"],
    ["73:8A:1F:D5:49:BC", "Павлова Ольга Николаевна", "вход", "15:00 09.01.2023"],
    ["9C:2E:7B:46:F8:A3", "Федоров Игорь Александрович", "выход", "15:00 10.01.2023"],
    ["B5:4D:3A:81:EC:72", "Лебедева Татьяна Викторовна", "вход", "15:00 11.01.2023"],
    ["C8:7F:15:9A:63:D4", "Никитин Андрей Олегович", "выход", "15:00 12.01.2023"],
    ["E9:36:8C:2D:5A:B7", "Захарова Светлана Юрьевна", "вход", "15:00 13.01.2023"],
    ["1F:D4:72:BE:85:49", "Борисов Артем Михайлович", "выход", "15:00 14.01.2023"],
    ["52:AB:9E:34:C7:6D", "Киселева Надежда Павловна", "вход", "15:00 15.01.2023"],
    ["6C:19:4F:A8:D2:3B", "Григорьев Виктор Сергеевич", "выход", "15:00 16.01.2023"],
    ["87:E5:2D:7B:41:9C", "Титова Людмила Анатольевна", "вход", "15:00 17.01.2023"],
    ["A3:6D:58:CE:94:27", "Комарова Ирина Борисовна", "выход", "15:00 18.01.2023"],
    ["D1:4B:83:65:F2:9A", "Белов Роман Евгеньевич", "вход", "15:00 19.01.2023"],
    ["F4:28:9C:73:5D:B6", "Медведева Екатерина Андреевна", "выход", "15:00 20.01.2023"],
]


class MainWindow(QMainWindow):
    def __init__(self, UI_MainWindow: Ui_MainWindow):
        super().__init__()

        self.ui: Ui_MainWindow = UI_MainWindow()
        self.ui.setupUi(self)

        headers = ["RFID", "ФИО", "вход/выход", "Дата"]

        self.model = TableModel(test_data, headers)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        self.ui.search_button.clicked.connect(self.click)

    def click(self):
        rfid = self.ui.rfid_input.text()
        self.ui.rfid_input.setText("11111")
        print()


app = QApplication(sys.argv)

window = MainWindow(Ui_MainWindow)
window.show()

app.exec()

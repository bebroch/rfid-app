import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from datetime import datetime, timedelta

from database import Database, UserDataFilter
from ui.main_window import Ui_MainWindow
from table_model import TableModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.updateTable(self.db.get())

        self.ui.search_button.clicked.connect(self.search_button_clicked)

    def search_button_clicked(self):
        rfid = self.ui.rfid_input.text() if self.ui.rfid_input.text() != "" else None
        full_name = self.ui.name_input.text() if self.ui.rfid_input.text() != "" else None

        is_enter = self.ui.enter_status.currentText()
        if is_enter == "вход":
            is_enter = True
        elif is_enter == "вход":
            is_enter = False
        else:
            is_enter = None

        if self.ui.interval_wigdet.currentIndex() == 0:
            dateTo = datetime.now()

            match self.ui.interval_box.currentText():
                case "Час":
                    dateFrom = dateTo - timedelta(hours=3)
                case "3 часа":
                    dateFrom = dateTo - timedelta(hours=3)
                case "День":
                    dateFrom = dateTo - timedelta(days=1)
                case "3 дня":
                    dateFrom = dateTo - timedelta(days=3)
                case "Неделя":
                    dateFrom = dateTo - timedelta(days=7)
                case "Месяц":
                    dateFrom = dateTo - timedelta(days=30)
                case _:
                    dateFrom = None
                    dateTo = None

        elif self.ui.interval_wigdet.currentIndex() == 1:
            dateFrom = self.ui.datetime_input.dateTime().toPyDateTime()
            dateTo = self.ui.datetime_input_two.dateTime().toPyDateTime()
        else:
            dateFrom, dateTo = None, None

        # TODO убрать
        print({"rfid": rfid, "full_name": full_name,
              "is_enter": is_enter, "dateFrom": dateFrom, "dateTo": dateTo})

        self.updateTable(self.db.get(
            UserDataFilter(
                rfid=rfid, full_name=full_name, is_enter=is_enter, dateFrom=dateFrom, dateTo=dateTo)
        ))

    def updateTable(self, data):
        headers = ["RFID", "ФИО", "вход/выход", "Дата"]

        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][3] = datetime.fromtimestamp(
                data[i][3]
            ).strftime("%H:%M %d.%m.%Y")
            data[i][2] = "вход" if data[i][2] == 1 else "выход"

        model = TableModel(data, headers)
        self.ui.tableView.setModel(model)
        header = self.ui.tableView.horizontalHeader()
        if header:
            header.setSectionResizeMode(
                QHeaderView.ResizeMode.ResizeToContents
            )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

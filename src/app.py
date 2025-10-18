from PyQt6.QtWidgets import QMainWindow, QHeaderView
from datetime import datetime, timedelta

from database.user_service import UserService
from ui.main_window import Ui_MainWindow
from table_model import TableModel
from database.user_service import UserAccessFilter


class MainWindow(QMainWindow):
    def __init__(
        self,
        userService: UserService,
    ):
        super().__init__()

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        self.userService = userService
        self.updateTable(self.userService.get().fetchall())

        self.ui.search_button.clicked.connect(self.search_button_clicked)

    # TODO вынести в отдельное нечто
    def search_button_clicked(self):
        rfid = self.ui.rfid_input.text() if self.ui.rfid_input.text() != "" else None
        full_name = (
            self.ui.name_input.text() if self.ui.name_input.text() != "" else None
        )

        print(full_name)
        is_enter = {"Вход": True, "Выход": False, "Нет значения": None}[
            self.ui.enter_status.currentText()
        ]

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
                    dateFrom = dateTo = None

        elif self.ui.interval_wigdet.currentIndex() == 1:
            dateFrom = self.ui.datetime_input.dateTime().toPyDateTime()
            dateTo = self.ui.datetime_input_two.dateTime().toPyDateTime()
        else:
            dateFrom = dateTo = None

        # TODO убрать
        print(
            {
                "rfid": rfid,
                "full_name": full_name,
                "is_enter": is_enter,
                "dateFrom": dateFrom,
                "dateTo": dateTo,
            }
        )

        self.updateTable(
            self.userService.get(
                UserAccessFilter(
                    rfid=rfid,
                    full_name=full_name,
                    is_enter=is_enter,
                    dateFrom=dateFrom,
                    dateTo=dateTo,
                )
            ).fetchall()
        )

    def updateTable(self, data):
        headers = ["RFID", "ФИО", "вход/выход", "Дата"]

        # TODO не нравиться
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][3] = datetime.fromtimestamp(data[i][3]).strftime("%H:%M %d.%m.%Y")
            data[i][2] = "вход" if data[i][2] == 1 else "выход"

        model = TableModel(data, headers)
        self.ui.tableView.setModel(model)
        header = self.ui.tableView.horizontalHeader()
        if header:
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

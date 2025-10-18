from dataclasses import dataclass
import datetime
import sqlite3
from sqlite3 import Connection
from database.user import UserTable
from database.access_log import AccessLogTable


@dataclass
class UserAccessFilter:
    rfid: str | None = None
    full_name: str | None = None
    is_enter: bool | None = None
    dateFrom: datetime.datetime | None = None
    dateTo: datetime.datetime | None = None

    def getDate(self):
        params = {}

        if not self.dateFrom and self.dateTo:
            raise Exception("dateFrom and dateTo are related")
        elif self.dateFrom and not self.dateTo:
            raise Exception("dateFrom and dateTo are related")
        elif self.dateFrom and self.dateTo:
            params["dateFrom"] = self.dateFrom.timestamp()
            params["dateTo"] = self.dateTo.timestamp()
        else:
            params["dateFrom"] = None
            params["dateTo"] = None

        return params


class UserService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        self.cursor = connection.cursor()
        self.userTable = UserTable(connection)
        self.accessLogTable = AccessLogTable(connection)

    def createTables(self):
        self.userTable.createTable()
        self.accessLogTable.createTable()

    def get(self, filter: UserAccessFilter = UserAccessFilter()):
        rfid, full_name, is_enter = filter.rfid, filter.full_name, filter.is_enter
        date = filter.getDate()
        dateFrom, dateTo = date["dateFrom"], date["dateTo"]

        query = """
            SELECT rfid, full_name, is_enter, date FROM access_logs
            JOIN users ON access_logs.user_rfid = users.rfid
            WHERE rfid LIKE '%' || COALESCE(?, rfid) || '%'
            AND full_name LIKE '%' || COALESCE(?, full_name) || '%'
            AND is_enter = COALESCE(?, is_enter)
            AND date BETWEEN COALESCE(?, date) AND COALESCE(?, date)
            ORDER BY date DESC;
            """

        return self.cursor.execute(query, (rfid, full_name, is_enter, dateFrom, dateTo))

    def __del__(self):
        self.close()

    def close(self):
        self.connection.close()

from dataclasses import dataclass
import sqlite3
from typing import TypedDict
import datetime


class AccessLogData(TypedDict, total=True):
    rfid: str
    is_enter: bool
    date: datetime.datetime


class AccessLogTable:

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA foreign_keys = ON")

    def __del__(self):
        self.close()

    def createTable(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS access_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_rfid TEXT,
            is_enter BOOLEAN NOT NULL CHECK (is_enter IN (0, 1)),
            date UNSiGNED INT NOT NULL,
            
            FOREIGN KEY (user_rfid) REFERENCES users (rfid) ON DELETE CASCADE
        )
        """
        )

        self.connection.commit()

    def create(self, data: AccessLogData) -> None:
        self.cursor.execute(
            """
        INSERT INTO access_logs (user_rfid, is_enter, date) VALUES (?, ?, ?)
        """,
            (data["rfid"], data["is_enter"], int(data["date"].timestamp())),
        )

        self.connection.commit()

    def close(self):
        self.connection.close()

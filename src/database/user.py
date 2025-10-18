from dataclasses import dataclass
import sqlite3
from typing import TypedDict


class UserData(TypedDict, total=True):
    rfid: str
    full_name: str


class UserTable:

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.close()

    def createTable(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS users(
            rfid TEXT PRIMARY KEY CHECK (rfid LIKE '__:__:__:__:__:__'),
            full_name TEXT NOT NULL CHECK (full_name != '')
        )
        """
        )
        self.connection.commit()

    def create(self, data: UserData) -> None:
        self.cursor.execute(
            """
        INSERT INTO users (rfid, full_name) VALUES (?, ?)
        """,
            (data["rfid"], data["full_name"]),
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

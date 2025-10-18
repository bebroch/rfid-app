import os
import random
import sqlite3
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from database.user import UserData
from database.access_log import AccessLogData
from database.user_service import UserAccessFilter
from database.user_service import UserService


def add_test_data():

    users_data = [
        UserData(rfid="98:27:F6:B5:FD:57", full_name="Иванов Иван Иванович"),
        UserData(rfid="A4:C3:F2:18:9D:44", full_name="Петров Петр Петрович"),
        UserData(rfid="BC:76:5E:3A:D1:9F", full_name="Сидорова Мария Сергеевна"),
        UserData(rfid="D8:92:4A:7C:E5:33", full_name="Козлов Алексей Владимирович"),
        UserData(rfid="E4:1A:5E:3A:D1:9F", full_name="Колесникова Мария Сергеевна"),
        UserData(rfid="F2:8B:47:91:C6:2A", full_name="Смирнов Александр Дмитриевич"),
        UserData(rfid="39:DA:8E:14:B7:5C", full_name="Федорова Екатерина Андреевна"),
        UserData(rfid="7C:E3:95:28:D4:6F", full_name="Никитин Денис Олегович"),
        UserData(rfid="A1:5B:29:73:EC:48", full_name="Волкова Ольга Игоревна"),
        UserData(rfid="D6:94:3F:82:B5:17", full_name="Морозов Сергей Викторович"),
    ]

    for user_data in users_data:
        userService.userTable.create(user_data)

        for _ in range(30):
            access_data = AccessLogData(
                rfid=user_data["rfid"],
                is_enter=random.choice([True, False]),
                date=datetime.datetime.fromtimestamp(
                    random.randint(1700727005, 1760727005)
                ),
            )

            userService.accessLogTable.create(access_data)


with sqlite3.connect("rfid_database.db") as connection:
    userService = UserService(connection)
    userService.createTables()

    add_test_data()

    print(
        userService.get(
            UserAccessFilter(
                dateFrom=datetime.datetime.strptime(
                    "15:00 08.10.2025", "%H:%M %d.%m.%Y"
                ),
                dateTo=datetime.datetime.strptime("15:00 10.10.2025", "%H:%M %d.%m.%Y"),
            )
        ).fetchall()
    )

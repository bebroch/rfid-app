from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt6.QtGui import QBrush


class TableModel(QAbstractTableModel):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self._data = data or []
        self._headers = headers or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        if self._data:
            return len(self._headers)
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Метод, который вызывается для каждой ячейки таблицы когда нужно отобразить или обработать данные"""
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        # Какие отобразить данные
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[row][col])

        # Какие отобразить данные, которые в состоянии изменении
        elif role == Qt.ItemDataRole.EditRole:
            return self._data[row][col]

        # Как отобразить данные
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            row = index.row()
            col = index.column()
            self._data[row][col] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._headers[section]
        return None

    def flags(self, index):
        return (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
            | Qt.ItemFlag.ItemIsEditable
        )

    def add_row(self, row_data):
        position = len(self._data)
        self.beginInsertRows(QModelIndex(), position, position)
        self._data.append(row_data)
        self.endInsertRows()

    def remove_row(self, position):
        self.beginRemoveRows(QModelIndex(), position, position)
        del self._data[position]
        self.endRemoveRows()

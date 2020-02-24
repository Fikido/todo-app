from PyQt5 import QtCore
from PyQt5.QtCore import *


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(TableModel, self).__init__()
        self.datatable = None

    def update(self, data):
        print('Updating model')
        self.datatable = data
        print(f'Data: {self.datatable}')

    def rowCount(self, parent=QModelIndex()):
        if self.datatable:
            return len(self.datatable)
        return 0

    def columnCount(self, parent=QModelIndex):
        if self.datatable:
            return len(self.datatable[0])
        return 0

    def flags(self, index):
        flags = super(TableModel, self).flags(index)
        j = index.column()
        if j == 1:
            flags |= Qt.ItemIsEditable
        elif j == 3 or j == 4:
            flags |= Qt.ItemIsUserCheckable
        return flags

    def setData(self, index: QModelIndex, value, role=Qt.DisplayRole):
        i = index.row()
        j = index.column()
        if role == Qt.EditRole and j == 1:
            self.datatable[i][j] = value
        elif role == Qt.CheckStateRole and (j==3 or j==4):
            if value:
                self.datatable[i][j] = True
            else:
                self.datatable[i][j] = False
        return True

    def data(self, index, role=Qt.DisplayRole):
        i = index.row()
        j = index.column()
        if role == Qt.DisplayRole:
            return f'{self.datatable[i][j]}'
        elif role == Qt.CheckStateRole and (j == 3 or j == 4):
            if self.datatable[i][j]:
                return Qt.Checked
            else:
                return Qt.Unchecked
        elif role == Qt.EditRole and j == 1:
            return self.datatable[i][j]
        else:
            return QVariant()

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return ["Id", "Task", "Date", "Done", "Delete"][section]
            if orientation == QtCore.Qt.Vertical:
                return section+1

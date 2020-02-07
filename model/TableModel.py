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

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            i = index.row()
            j = index.column()
            return f'{self.datatable[i][j]}'
        else:
            return QVariant()

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return ["Id", "Task", "Date", "Done", "Delete"][section]
            if orientation == QtCore.Qt.Vertical:
                return section+1

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

from PyQt5.QtWidgets import *
from Gui import Gui
from LoginDialog import LoginDialog
import sys
from database.Db import *
import model.TableModel as tm

class ToDo(QWidget, Gui):
    def __init__(self, parent=None):
        super(ToDo, self).__init__(parent)
        self.setupGui(self)

        # Signals
        self.loginButton.clicked.connect(self.login)
        self.exitButton.clicked.connect(self.end)

    # Unpack login and password from static method and checks it
    def login(self):
        log, passwd = LoginDialog.getLoginAndPassword(self) or (None, None)
        if not log or not passwd:
            QMessageBox.warning(self, 'Error', 'Empty username or password!', QMessageBox.Ok)
            return
        user = getLogFromDb(log, passwd)
        if user is None:
            QMessageBox.warning(self, 'Error', 'Wrong username or password', QMessageBox.Ok)
            return
        tasks = readData(user)
        model.update(tasks)
        model.layoutChanged.emit()

        self.refreshView()
        QMessageBox.information(self,'Success', f'Hello, {log}!', QMessageBox.Ok)

    def refreshView(self):
        self.view.setModel(model)
        self.view.resizeColumnsToContents()
        self.view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.view.hideColumn(0)

    def end(self):
        self.close()

    def add(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    connect()
    model = tm.TableModel()
    window = ToDo()
    window.show()
    sys.exit(app.exec_())

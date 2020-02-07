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
        self.addButton.clicked.connect(self.add)

    # Unpack login and password from static method and checks it
    def login(self):
        log, passwd = LoginDialog.getLoginAndPassword(self) or (None, None)
        if not log or not passwd:
            QMessageBox.warning(self, 'Error', 'Empty username or password!', QMessageBox.Ok)
            return
        self.user = getLogFromDb(log, passwd)
        if self.user is None:
            QMessageBox.warning(self, 'Error', 'Wrong username or password', QMessageBox.Ok)
            return
        tasks = readData(self.user)
        model.update(tasks)
        model.layoutChanged.emit()

        self.refreshView()
        QMessageBox.information(self, 'Success', f'Hello, {log}!', QMessageBox.Ok)

    def refreshView(self):
        model.headerData(4)
        self.view.setModel(model)
        self.view.resizeColumnsToContents()
        self.view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.view.hideColumn(0)

    def end(self):
        self.close()

    def add(self):
        task, ok = QInputDialog.getMultiLineText(self, 'Task', 'Add new task')
        if not ok or not task.strip():
            QMessageBox.warning(self, 'Error', 'Message can not be empty', QMessageBox.Ok)
            return
        addTask(task,self.user.id)
        model.update(readData(self.user))
        model.layoutChanged.emit()
        self.refreshView()


if __name__ == '__main__':
    app = QApplication([])
    connect()
    model = tm.TableModel()
    window = ToDo()
    window.show()
    sys.exit(app.exec_())

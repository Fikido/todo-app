from gui.Gui import Gui
from gui.LoginDialog import LoginDialog
from database.Db import *
import model.TableModel as tm
from gui.RegisterDialog import *


class ToDo(QWidget, Gui):
    def __init__(self, parent=None):
        super(ToDo, self).__init__(parent)
        self.setupGui(self)
        self.user = None
        # Signals
        self.loginButton.clicked.connect(self.login)
        self.exitButton.clicked.connect(self.end)
        self.addNewTaskButton.clicked.connect(self.addTask)
        self.addNewUserButton.clicked.connect(self.addUser)
        self.saveButton.clicked.connect(self.save)

        self.addNewTaskButton.setEnabled(False)
        self.saveButton.setEnabled(False)

    # Unpack login and password from static method and checks it
    def login(self):
        log, passwd = LoginDialog.getLoginAndPassword(self) or (None, None)
        if not log or not passwd:
            QMessageBox.warning(self, 'Error', 'Empty username or password!', QMessageBox.Ok)
            return
        self.user = None
        self.user = getLogFromDb(log, passwd)
        if self.user is None:
            QMessageBox.warning(self, 'Error', 'Wrong username or password', QMessageBox.Ok)
            return
        tasks = readData(self.user)
        model.update(tasks)
        model.layoutChanged.emit()

        self.refreshView()
        QMessageBox.information(self, 'Success', f'Hello, {log}!', QMessageBox.Ok)
        self.addNewTaskButton.setEnabled(True)
        self.saveButton.setEnabled(True)

    # Refresh table
    def refreshView(self):
        model.headerData(4)
        self.view.setModel(model)
        self.view.resizeColumnsToContents()
        self.view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.view.hideColumn(0)

    def end(self):
        self.close()

    # Add new task dialog
    def addTask(self):
        task, ok = QInputDialog.getMultiLineText(self, 'Task', 'Add new task')
        if not ok or not task.strip():
            QMessageBox.warning(self, 'Error', 'Message can not be empty', QMessageBox.Ok)
            return
        if self.user is None:
            QMessageBox.warning(self, 'Error', 'You must register first', QMessageBox.Ok)
            return
        addTask(task, self.user.id)
        model.update(readData(self.user))
        model.layoutChanged.emit()
        self.refreshView()

    # Add new user dialog
    def addUser(self):
        log, passwd = RegisterDialog.getRegiterLoginAndPassword(self) or (None, None)
        if not log or not passwd:
            QMessageBox.warning(self, 'Error', 'Empty username or password!', QMessageBox.Ok)
            return
        userRegister = getLogFromDb(log, passwd)
        if userRegister is not None:
            QMessageBox.warning(self, 'Error', 'Error, username exists enter another one.', QMessageBox.Ok)
            return
        addNewUser(log, passwd)
        model.layoutChanged.emit()
        self.refreshView()
        QMessageBox.information(self, 'Success', f'Account created {log}!', QMessageBox.Ok)

    def save(self):
        saveTasks(model.datatable)
        model.layoutChanged.emit()
        tasks = readData(self.user)
        model.update(tasks)
        self.refreshView()


if __name__ == '__main__':
    app = QApplication([])
    connect()
    model = tm.TableModel()
    window = ToDo()
    window.show()
    sys.exit(app.exec_())

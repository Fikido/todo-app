from PyQt5.QtWidgets import *
from Gui import Gui
from LoginDialog import LoginDialog
import sys
from db import *


class ToDo(QWidget, Gui):
    def __init__(self, parent=None):
        super(ToDo, self).__init__(parent)
        self.setupGui(self)

        self.loginButton.clicked.connect(self.login)
        self.exitButton.clicked.connect(self.end)

    def login(self):
        log, passwd = LoginDialog.getLoginAndPassword(self) or (None, None)
        if not log or not passwd:
            QMessageBox.warning(self, 'Error', 'Empty log or pass!', QMessageBox.Ok)
            return
        QMessageBox.information(self,'Success', f'Hello, {log}!', QMessageBox.Ok)


    def end(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    CreateDb()
    window = ToDo()
    window.show()
    sys.exit(app.exec_())

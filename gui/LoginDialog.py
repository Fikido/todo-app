from PyQt5.QtWidgets import *
import sys


class LoginDialog(QDialog):
    def __init__(self, parent = None):
        super(LoginDialog, self).__init__(parent)
        self.formGroupBox = QGroupBox("Login form")
        self.createLoginGroupBox()

        # Dialog buttons
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Log in", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Back", QDialogButtonBox.RejectRole)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle('Login form')
        self.setFixedSize(300,150)

    # Username and password input fields
    def createLoginGroupBox(self):
        self.password = QLineEdit()
        self.login = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Enter your password')
        self.login.setPlaceholderText('Enter your username')
        layout = QFormLayout()
        layout.addRow(QLabel("Username:"), self.login)
        layout.addRow(QLabel("Password:"), self.password)
        self.formGroupBox.setLayout(layout)
        self.setModal(True)

    # Return Login
    def getLogin(self):
        return self.login.text()

    # Return Password
    def getPassword(self):
        return self.password.text()

    # Create instance and send tuple of login and password
    @staticmethod
    def getLoginAndPassword(parent=None):
        dialog = LoginDialog(parent)
        if dialog.exec_() == QDialog.Accepted:
            return tuple([dialog.getLogin(), dialog.getPassword()])
from PyQt5.QtWidgets import *


class Gui:
    def __init__(self):
        self.addNewUserButton = QPushButton("Register")
        self.addNewTaskButton = QPushButton("Add")
        self.saveButton = QPushButton("Save")
        self.exitButton = QPushButton("Exit")
        self.loginButton = QPushButton("Login")
        self.view = QTableView()

    def setupGui(self, Widget):
        Widget.setObjectName("Widget")
        height, width = (500, 600)

        # Layout
        layoutOutside = QVBoxLayout(self)
        layoutOutside.addWidget(self.view)
        layoutOutside.addWidget(self.addNewTaskButton)
        layoutOutside.addWidget(self.saveButton)
        layoutOutside.addWidget(self.loginButton)
        layoutOutside.addWidget(self.addNewUserButton)
        layoutOutside.addWidget(self.exitButton)

        # Center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowTitle("ToDo list")
        self.resize(height, width)

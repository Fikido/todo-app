from PyQt5.QtWidgets import *


class Gui:
    def setupGui(self, Widget):
        Widget.setObjectName("Widget")
        height, width = (500, 600)
        self.view = QTableView()

        # Buttons
        self.loginButton = QPushButton("Login")
        self.exitButton = QPushButton("Exit")
        self.addNewTaskButton = QPushButton("Add")
        self.addNewUserButton = QPushButton("Register")

        # Layout
        layoutOutside = QVBoxLayout(self)
        layoutOutside.addWidget(self.view)
        layoutOutside.addWidget(self.addNewTaskButton)
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

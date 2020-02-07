from PyQt5.QtWidgets import *


class Gui:
    def setupGui(self, Widget):
        Widget.setObjectName("Widget")
        height, width = (500, 600)
        self.view = QTableView()

        # Buttons
        self.loginButton = QPushButton("Login")
        self.exitButton = QPushButton("Exit")
        self.addButton = QPushButton("Add")

        # Layout
        layoutOutside = QVBoxLayout(self)
        layoutOutside.addWidget(self.view)
        layoutOutside.addWidget(self.loginButton)
        layoutOutside.addWidget(self.addButton)
        layoutOutside.addWidget(self.exitButton)

        # Center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowTitle("ToDo list")
        self.resize(height, width)

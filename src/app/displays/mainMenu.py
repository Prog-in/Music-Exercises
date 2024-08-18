from PyQt6.QtWidgets import (
    QWidget,
    QButtonGroup,
    QPushButton,
    QLabel,
    QVBoxLayout
)
from .baseDisplay import BaseDisplay


class MainMenu(BaseDisplay):
    def __init__(self, app):
        super().__init__("Main Menu")
        self.__controller = app

    def initUI(self) -> None:
        layout = QVBoxLayout()

        qlabel = QLabel("Exercises")

        buttonGroup = QButtonGroup(self)
        pushButton1 = QPushButton("Note reading on staff")
        buttonGroup.addButton(pushButton1, 1)

        buttonGroup.idClicked.connect(self.__controller.gotoWindow)

        layout.addWidget(qlabel)
        layout.addWidget(pushButton1)

        layout.addStretch()
        
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)

        self.show()

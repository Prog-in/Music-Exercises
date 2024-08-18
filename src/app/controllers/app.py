from PyQt6.QtWidgets import QApplication
import sys
from ..displays.mainMenu import MainMenu
from .abstractController import AbstractController
from .noteReadingController import NoteReadingController


class App(AbstractController):
    def __init__(self, QApp: QApplication) -> None:
        self.__display = MainMenu(self)
        self.__qapp = QApp
        self.__noteReadingController = NoteReadingController(self)

    def start(self) -> None:
        self.openScreen()
        self.__qapp.exec()

    def exit(self):
        sys.exit()

    def openScreen(self) -> None:
        self.__display.initUI()

    def gotoWindow(self, buttonId: int) -> None:
        self.__display.close()
        match buttonId:
            case 1:
                self.__noteReadingController.openScreen()

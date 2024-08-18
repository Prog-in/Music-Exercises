from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication
from utils.constants import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT


class BaseDisplay(QMainWindow):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE + " - " + msg)
        center = QGuiApplication.primaryScreen().availableGeometry().center()
        topleft_x = center.x() - WINDOW_WIDTH//2
        topleft_y = center.y() - WINDOW_HEIGHT//2
        self.setGeometry(topleft_x, topleft_y, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

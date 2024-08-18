from PyQt6.QtWidgets import QApplication
import sys
from app.controllers.app import App
from utils.fileUtils import getMusicNotes


def main():
    app = QApplication(sys.argv)
    App(app).start()


def setup():
    getMusicNotes()


if __name__ == "__main__":
    #setup()
    main()

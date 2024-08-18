from .abstractController import AbstractController
from ..displays.noteReadingDisplay import NoteReadingDisplay
from ..entities.noteReadingPontuation import NoteReadingPontuation

class NoteReadingController(AbstractController):
    def __init__(self, app: AbstractController) -> None:
        self.__display = NoteReadingDisplay(self)
        self.__app = app
        self.__pontuation = NoteReadingPontuation()

    def start(self) -> None:
        self.openScreen()
        self.__qapp.exec()

    def exit(self) -> None:
        self.__display.close()
        self.__app.openScreen()

    def openScreen(self) -> None:
        self.__display.initUI()

    def getGuesses(self) -> int:
        return self.__pontuation.guesses

    def getCorrectGuesses(self) -> int:
        return self.__pontuation.correctGuesses

    def correctGuess(self) -> None:
        self.__pontuation.correctGuess()
    
    def wrongGuess(self) -> None:
        self.__pontuation.wrongGuess()

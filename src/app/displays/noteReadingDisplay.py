from PyQt6.QtWidgets import (
    QWidget,
    QButtonGroup,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtGui import QPixmap, QFontMetrics
from PyQt6.QtCore import Qt
from pathlib import Path
from random import choice
from .baseDisplay import BaseDisplay
from utils.constants import NOTES_DIR, WINDOW_WIDTH, WINDOW_HEIGHT, C_MAJOR, MEDIA_SUFFIXES
from utils.fileUtils import getFilesEndingWithSuffixes


class NoteReadingDisplay(BaseDisplay):
    def __init__(self, app):
        super().__init__("Reading On Staff")
        self.__controller = app
        self.__notesDir = NOTES_DIR / "bass2"
        self.__guessesLabel = QLabel()
        self.__correctGuessesLabel = QLabel()
        self.__staffLabel = QLabel()
        self.__curNotePath = self.__getRandNoteFilePath()

    def __correctGuess(self):
        self.__curNotePath = self.__getRandNoteFilePath()
        self.__setImage()
        self.__controller.correctGuess()
    
    def __wrongGuess(self):
        self.__controller.wrongGuess()

    def __checkGuess(self, button: QPushButton):
        guess = button.text()
        correctClass = self.__curNotePath.stem[:-1]
        if guess == correctClass:
            self.__correctGuess()
        else:
            self.__wrongGuess()
        self.__updateGuessLabels()

    def __updateGuessLabels(self):
        self.__guessesLabel.setText("Guesses: " + str(self.__controller.getGuesses()))
        self.__guessesLabel.adjustSize()

        self.__correctGuessesLabel.setText("Correct Guesses: " + str(self.__controller.getCorrectGuesses()))
        self.__correctGuessesLabel.adjustSize()

    def __setImage(self):
        img = QPixmap(str(self.__curNotePath))
        imgWidth = int(3/8 * WINDOW_WIDTH)
        img.scaledToWidth(imgWidth, mode=Qt.TransformationMode.SmoothTransformation)
        self.__staffLabel.setPixmap(img)
        self.__staffLabel.resize(img.width(), img.height())

    def __getRandNoteFilePath(self) -> Path:
        notes = list(getFilesEndingWithSuffixes(self.__notesDir, MEDIA_SUFFIXES))
        return choice(notes)

    def closeEvent(self, event):
        #TODO: IMPLEMENT DATA SAVING ON WINDOW CLOSING
        print("closing...")
        event.accept()

    def initUI(self) -> None:
        layout = QVBoxLayout()

        self.__setImage()

        guessesLayout = QVBoxLayout()
        self.__updateGuessLabels()
        guessesLayout.addWidget(self.__guessesLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        guessesLayout.addWidget(self.__correctGuessesLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        NotesGroup = QButtonGroup(self)
        buttonsLayout = QVBoxLayout()

        accidentals = ["s", "", "b"]
        #widths = []
        for acc in accidentals:
            row = QHBoxLayout()
            for pitchClass in C_MAJOR:
                btnText = pitchClass + acc
                btn = QPushButton(btnText)
                #width = QFontMetrics(btn.font()).boundingRect(btnText).width()
                #widths.append(width)
                NotesGroup.addButton(btn)
                row.addWidget(btn)

            buttonsLayout.addLayout(row)
        
        # btnWidth = max(widths) * 3
        # for btn in NotesGroup.buttons():
        #     btn.setMinimumWidth(btnWidth)
        #     btn.setMaximumWidth(btnWidth)

        NotesGroup.buttonClicked.connect(self.__checkGuess)

        exitButton = QPushButton("Back to main menu")
        exitButton.clicked.connect(self.__controller.exit)

        spacing = int(1/20 * WINDOW_HEIGHT)

        layout.addLayout(guessesLayout)
        layout.addWidget(self.__staffLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(spacing)
        layout.addLayout(buttonsLayout)
        layout.addStretch()
        layout.addWidget(exitButton, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        wid = QWidget(self)
        wid.setLayout(layout)
        self.setCentralWidget(wid)

        self.show()

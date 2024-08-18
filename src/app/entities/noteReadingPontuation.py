class NoteReadingPontuation:
    def __init__(self):
        self.__guesses = 0
        self.__correctGuesses = 0
    
    def correctGuess(self):
        self.__guesses += 1
        self.__correctGuesses += 1
    
    def wrongGuess(self):
        self.__guesses += 1

    @property
    def guesses(self):
        return self.__guesses
    
    @property
    def correctGuesses(self):
        return self.__correctGuesses

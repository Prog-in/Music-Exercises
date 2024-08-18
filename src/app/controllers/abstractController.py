from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def openScreen():
        pass

    @abstractmethod
    def exit():
        pass

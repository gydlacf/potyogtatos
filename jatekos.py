# This Python file uses the following encoding: utf-8

from abc import ABC

class Jatekos(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def lep(self):
        raise NotImplementedError

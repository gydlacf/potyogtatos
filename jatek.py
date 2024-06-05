# This Python file uses the following encoding: utf-8

from jatekmester import Jatekmester
from gep import Gep

class Jatek:
    def __init__(self, width, height):
        self._mester = Jatekmester(width,
                                   height)

        self._ellenfel = Gep()

    def fut(self):
        while True:
            oszlop = int(input('Melyik oszlop?'))

            self._mester.lep(oszlop)

            if self._mester.gyoztes():
                print('Te győztél')
                return

            self._mester.valt()

            print(self._mester._jatekos)

            self._mester.lep(self._ellenfel.lep(self._mester))

            if self._mester.gyoztes():
                print(self._mester._mezo,
                      self._mester.sorok(2),
                      self._mester.oszlopok(2),
                      self._mester.atlok(2))
                print('Én győztem.')
                return

            self._mester.valt()

            print(self._mester._mezo)

if __name__ == '__main__':
    jatek = Jatek(7, 6)

    jatek.fut()



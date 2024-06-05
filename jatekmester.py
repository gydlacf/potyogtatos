# This Python file uses the following encoding: utf-8

import numpy as np

class Jatekmester:
    def __init__(self,
                 arg1,
                 arg2=None):
        if arg2 is None:
            self._mezo = arg1._mezo
            self._jatekos = arg1._jatekos
        else:
            self._mezo = np.zeros((arg2, arg1))
            self._jatekos = 1

    def ervenyes(self, oszlop):
        return np.any(self._mezo[:, oszlop] == 0)

    def lehetosegek(self):
        return np.nonzero(np.any(self._mezo == 0,
                                 axis=0))[0]

    def lep(self, oszlop):
        sor = np.nonzero(self._mezo[:, oszlop] == 0)[0].max()

        print(sor, oszlop)

        self._mezo[sor, oszlop] = self._jatekos

    def valt(self):
        if self._jatekos == 1:
            self._jatekos = 2
        else:
            self._jatekos = 1

    def proba(self, oszlop):
        if ervenyes(oszlop):
            uj = Jatekmester(self)

            uj.lep(oszlop)
            uj.valt()

            return uj

    def vannegy(self, sor, jatekos):
        asor = sor == jatekos

        hany = 0

        for i in asor:
            hany= hany + 1 if i else 0

            if hany == 4:
                return True

        return False

    def sorok(self, jatekos):
        for sor in range(self._mezo.shape[0]):
            if self.vannegy(self._mezo[sor, :],
                       jatekos):
                return True

        return False

    def oszlopok(self, jatekos):
        for oszlop in range(self._mezo.shape[1]):
            if self.vannegy(self._mezo[:, oszlop],
                       jatekos):
                return True
        return False

    def atlok(self, jatekos):
        width, height = self._mezo.shape

        for i in range(-(np.minimum(width, height) - 4),
                       np.minimum(width, height) - 3):
            if self.vannegy(np.diag(self._mezo, i),
                       jatekos):
                return True
            elif self.vannegy(np.diag(self._mezo.T, i),
                         jatekos):
                return True

        return False

    def gyoztes(self, jatekos=None):
        if jatekos is None:
            jatekos = self._jatekos

        return any([self.sorok(jatekos),
                    self.oszlopok(jatekos),
                    self.atlok(jatekos)])


if __name__ == '__main__':
    mester = Jatekmester(7, 6)

    for i in range(3):
        mester.lep(i)
        print(mester.gyoztes())
        mester.valt()
        mester.lep(i)
        print(mester.gyoztes())
        mester.valt()

    mester.lep(3)
    print(mester.gyoztes())


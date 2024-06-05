# This Python file uses the following encoding: utf-8

from jatekos import Jatekos

from random import choice

class Gep(Jatekos):
    def __init__(self, jatekos):
        self._jatekos = jatekos

    def lep(self, mester):
        lehetosegek = mester.lehetosegek()

        print(lehetosegek)

        return choice(lehetosegek)

    def nyitottkettes(self, mester,
                      jatekos):
        pass


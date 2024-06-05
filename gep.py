# This Python file uses the following encoding: utf-8

from jatekos import Jatekos

from random import choice

class Gep(Jatekos):
    def __init__(self):
        pass

    def lep(self, mester):
        lehetosegek = mester.lehetosegek()

        print(lehetosegek)

        return choice(lehetosegek)

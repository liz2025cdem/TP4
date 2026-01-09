from math import pi


class Cercle:


    pi = 3.14

    def __init__(self, rayon,):
        self.rayon = rayon
        self.circonférence = 0
        self.aire = 0

    def calcul_circonference(self):
        self.circonference = 2*pi*self.rayon



    def print_circonference(self):
        if self.circonference == 0:
            self.calcul_circonference()
        print(self.circonference)

c = Cercle(4)
c.print_circonference

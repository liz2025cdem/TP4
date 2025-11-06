from math import pi
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.longueur*self.largeur

    def print_aire(self):
        if self.aire == 0:
            self.calcul_aire()
        print(self.aire)


r = Rectangle(4, 5)
r.print_aire()

class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self):
        self.message
    def print_string(self):
        print(self.message)


s = StringFoo('allo')
s.print_string()



class Cercle:


    pi = 3.14

    def __init__(self, rayon,):
        self.rayon = rayon
        self.circonference = 0
        self.aire = 0


    def calcul_circonference(self):
        self.circonference = 2*pi*self.rayon



    def print_circonference(self):
        if self.circonference == 0:
            self.calcul_circonference()
        print(self.circonference)



    def calcul_aire(self):
        self.aire = self.rayon*pi*self.rayon



    def print_aire(self):
        if self.aire == 0:
            self.calcul_aire()
        print(self.aire)

c = Cercle(8)
c.print_circonference()
c.print_aire()








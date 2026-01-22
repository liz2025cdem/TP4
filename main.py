"""
une exercice qui contient divers petits pratiques pendant le cours Activité TEchnologie.(4.1)
Par: Zihao Li
groupe 401
"""

class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self):
        self.message
    def print_string(self):
        print(self.message.upper())


s = StringFoo('allo monde')
s.print_string()

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


import random


class Hero:


   def __init__(self, vie, attaque, defense, nom, nom2, force):
       self.vie = vie
       self.attaque = attaque
       self.defense = defense
       self.nom = nom
       self.nom2 = nom2
       self.force = force




   def calcul_dommage(self):
       dommage_donnee = random.randint(1, 6) + self.attaque
       dommage_recu = max(0, dommage_donnee - self.defense)
       self.vie -= dommage_recu
       print(f"{self.nom} attaque {self.nom2}. Dégâts infligés: {dommage_recu}. point de vie {self.nom}: {self.vie}, force = {self.force} ")


   def est_vivant(self):
       return self.vie > 0





hero_un = Hero(vie=random.randint(2,20), attaque=random.randint(1,6), defense=random.randint(1,6), nom='Hero 1',nom2= 'Hero 2', force = random.randint(1,20))
hero_deux = Hero(vie=random.randint(2,20), attaque=random.randint(1,6), defense=random.randint(1,6), nom='Hero 1',nom2= 'hero 2', force = random.randint(1,20))


print(" Début du combat ")
hero_un.calcul_dommage()
print(f"Statut Hero 1: {'Vivant' if hero_un.est_vivant() else 'Mort'}")
print(f"Statut Hero 2: {'Vivant' if hero_deux.est_vivant() else 'Mort'}")


class caracteristique:
    force = random.randint(1, 20)
    dextérité = random.randint(1, 20)
    constitution = random.randint(1, 20)
    intelligence = random.randint(1, 20)
    sagesse = random.randint(1, 20)
    charisme = random.randint(1, 20)

C = caracteristique()

print(f'force:{C.force} ')
print(f'dextérité:{C.dextérité} ')
print(f'constitution:{C.constitution} ')
print(f'intelligence:{C.intelligence} ')
print(f'sagesse:{C.sagesse} ')
print(f'charisme:{C.charisme} ')












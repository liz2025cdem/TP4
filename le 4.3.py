"""
une exercice pour pratiquer la fonction sac a dos et alignment pour le cours Activité TEchnologie.(4.3)
Par: Zihao Li
groupe 401
"""

from enum import Enum
import random
from dataclasses import dataclass


@dataclass
class item:
    nom: str
    quantite: int


class sac_a_dos:
    def __init__(self):

        self.liste_objet = []

    def ajouter_objet(self, nouvel_objet):

        trouve = False


        for objet in self.liste_objet:
            if objet.nom == nouvel_objet.nom:

                objet.quantite = objet.quantite + nouvel_objet.quantite
                trouve = True
                break


        if not trouve:
            self.liste_objet.append(nouvel_objet)

    def retirer_objet(self, objet_a_enlever, quantite_a_retirer):
        for objet in self.liste_objet:
            if objet.nom == objet_a_enlever:

                if quantite_a_retirer <= objet.quantite:
                    objet.quantite = objet.quantite - quantite_a_retirer

                    if objet.quantite == 0:
                        self.liste_objet.remove(objet)
                else:
                    print("Erreur : Pas assez de quantité dans le sac!")
                return


        print("Erreur : L'objet n'est pas dans le sac!")

    def voir_contenu(self):
        print("\n contenu du sac ")
        for objet in self.liste_objet:
            print(f"nom du item: {objet.nom}  la quantité: {objet.quantite}")


class Alignement(Enum):
    undefined = 0
    lawful_good = 1
    neutral_good = 2
    chaotic_good = 3
    lawful_neutral = 4
    true_neutral = 5
    chaotic_neutral = 6
    lawful_evil = 7
    neutral_evil = 8
    chaotic_evil = 9


def calculer_habilete():

    des = []
    for i in range(4):
        des.append(random.randint(1, 6))


    des.sort()


    somme_3_meilleurs = sum(des[1:])
    return somme_3_meilleurs


class NPC:
    def __init__(self, nom, race, espece, metier, alignment=Alignement.undefined):

        self.force = calculer_habilete()
        self.agilite = calculer_habilete()
        self.constitution = calculer_habilete()
        self.intelligence = calculer_habilete()
        self.sagesse = calculer_habilete()
        self.charisme = calculer_habilete()
        self.alignement = alignment

        self.nom = nom
        self.race = race
        self.espece = espece
        self.metier = metier
        self.classe_armure = random.randint(1, 12)
        self.pv = random.randint(1, 20)



    def afficher_caracteristiques(self):
        print(f"\n carac de {self.nom} ")
        print(f"Métier: {self.metier} | Race: {self.race}")
        print(f"Force: {self.force}")
        print(f"Agilité: {self.agilite}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Sagesse: {self.sagesse}")
        print(f"Charisme: {self.charisme}")
        print(f"Classe d'armure: {self.classe_armure}")
        print(f"Points de vie: {self.pv}")

    def subir_dommage(self, dommage):
        self.pv -= dommage
        print(f"{self.nom} subit {dommage} points de dégâts! PV restants: {self.pv}")

    def est_vivant(self):
        if self.pv > 0:
            return True
        else:
            return False


class Kobold(NPC):
    def __init__(self, nom, race, espece, metier):
        super().__init__(nom, race, espece, metier, Alignement.lawful_evil)

    def attaquer(self, cible):
        print(f"\nLe Kobold {self.nom} attaque {cible.nom}!")
        dé_de_20 = random.randint(1, 20)

        if dé_de_20 == 20:
            print("Critique!")
            cible.subir_dommage(random.randint(1, 8))
        elif dé_de_20 == 1:
            print("Échec critique")
        elif dé_de_20 >= cible.classe_armure:
            print(f"Touche! (attaque: {dé_de_20} plus grand que la classe armure: {cible.classe_armure})")
            cible.subir_dommage(random.randint(1, 6))
        else:
            print(f"Manqué! (attaque: {dé_de_20})")


class Hero(NPC):
    def __init__(self, nom, race, espece, metier):
        super().__init__(nom, race, espece, metier, Alignement.lawful_good)
        self.sac = None

    def attaquer(self, cible):
        print(f"\nLe Héros {self.nom} attaque {cible.nom}!")
        dé_de_20 = random.randint(1, 20)

        if dé_de_20 == 20:
            print("Attaque critique!")
            cible.subir_dommage(random.randint(1, 8))
        elif dé_de_20 == 1:
            print("Attaque ratée!")
        elif dé_de_20 >= cible.classe_armure:
            print(f"Réussite! (attaque: {dé_de_20} >= CA: {cible.classe_armure})")
            cible.subir_dommage(random.randint(1, 6))
        else:
            print(f"L'attaque a échoué (attaque: {dé_de_20})")

        self.sac = sac_a_dos()


monstre = Kobold("Kobold 1", "Kobold", "Monstre", "Voleur")
monstre.afficher_caracteristiques()
print(f"{monstre.alignement}")

joueur = Hero("soldat 1", "Humain", "Humanoïde", "Guerrier")
joueur.afficher_caracteristiques()
print(f"{joueur.alignement}")



joueur.attaquer(monstre)

if monstre.est_vivant():
    print("Le monstre est encore vivant")
else:
    print("le monstre est mort")


joueur.sac.ajouter_objet(item("Or", 10))

joueur.sac.ajouter_objet(item("Or", 5))

joueur.sac.ajouter_objet(item("Argent", 500))

joueur.sac.ajouter_objet(item("Potion", 1))

joueur.sac.voir_contenu()

joueur.sac.retirer_objet("Or", 15)

joueur.sac.voir_contenu()

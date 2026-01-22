"""
une exercice pour créé un npc, un hero et un kobold pendant le cours Activité TEchnologie.(4.2)
Par: Zihao Li
groupe 401
"""


import random



class NPC:
   def __init__(self, nom, race, espece, metier):
       self.force = self.calculer_habilete()
       self.agilite = self.calculer_habilete()
       self.constitution = self.calculer_habilete()
       self.intelligence = self.calculer_habilete()
       self.sagesse = self.calculer_habilete()
       self.charisme = self.calculer_habilete()


       self.nom = nom
       self.race = race
       self.espece = espece
       self.metier = metier
       self.classe_armure = random.randint(1, 12)
       self.pv = random.randint(1, 20)


   def calculer_habilete(self):

       des = []
       for i in range(4):
           des.append(random.randint(1, 6))



       des.sort()



       somme_3_meilleurs = sum(des[1:])
       return somme_3_meilleurs


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
       print(f"{self.nom} subit {dommage} points de dégâts! point de vie restants: {self.pv}")




class Kobold(NPC):
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




class Heros(NPC):
   def attaquer(self, cible):
       print(f"\nLe Héros {self.nom} attaque {cible.nom}!")
       dé_de_20 = random.randint(1, 20)


       if dé_de_20 == 20:
           print("attaque critique!")
           cible.subir_dommage(random.randint(1, 8))
       elif dé_de_20 == 1:
           print("attaque ratée!")
       elif dé_de_20 >= cible.classe_armure:
           print(f"réussite! (attaque: {dé_de_20} est plus grand que la classe armure: {cible.classe_armure})")
           cible.subir_dommage(random.randint(1, 6))
       else:
           print(f"L'attaque a échoué (attaque: {dé_de_20})")




joueur = Heros("soldat 1", "Humain", "homo-sapien", "Guerrier")
monstre = Kobold("Kobold 1", "Kobold", "Monstre", "Voleur")

joueur.afficher_caracteristiques()
monstre.afficher_caracteristiques()

joueur.attaquer(monstre)
monstre.attaquer(joueur)

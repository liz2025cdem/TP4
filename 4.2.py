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
       # 1. On roule 4 dés à 6 faces
       des = []
       for i in range(4):
           des.append(random.randint(1, 6))


       # 2. On classe les dés en ordre croissant
       des.sort()


       # 3. On ignore le premier (le plus petit) et on additionne les 3 autres
       somme_3_meilleurs = sum(des[1:])
       return somme_3_meilleurs


   def afficher_caracteristiques(self):
       print(f"\n caracteristiques de {self.nom} ")
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
       de20 = random.randint(1, 20)


       if de20 == 20:
           print("Critique!")
           cible.subir_dommage(random.randint(1, 8))
       elif de20 == 1:
           print("Échec critique...")
       elif de20 >= cible.classe_armure:
           print(f"Touche! (attaque: {de20} >= classe armure: {cible.classe_armure})")
           cible.subir_dommage(random.randint(1, 6))
       else:
           print(f"Manqué! (attaque: {de20})")




class Heros(NPC):
   def attaquer(self, cible):
       print(f"\nLe Héros {self.nom} attaque {cible.nom}!")
       de20 = random.randint(1, 20)


       if de20 == 20:
           print("Attaque critique!")
           cible.subir_dommage(random.randint(1, 8))
       elif de20 == 1:
           print("Attaque ratée!")
       elif de20 >= cible.classe_armure:
           print(f"Réussite! (attaque: {de20} >= classe armure: {cible.classe_armure})")
           cible.subir_dommage(random.randint(1, 6))
       else:
           print(f"L'attaque a échoué (attaque: {de20})")



# les infos de l'héros et le monstre
joueur = Heros("Valiant", "Humain", "homo-sapien", "Guerrier")
monstre = Kobold("Rask", "Kobold", "Monstre", "Voleur")


# Affichage des stats des caracteristiques
joueur.afficher_caracteristiques()
monstre.afficher_caracteristiques()


# Simulation d'un tour de combat
joueur.attaquer(monstre)


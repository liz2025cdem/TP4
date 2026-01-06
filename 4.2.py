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


       # 2. On trie les dés du plus petit au plus grand
       des.sort()


       # 3. On ignore le premier (le plus petit) et on additionne les 3 autres
       # des[1:] signifie : prendre de l'index 1 jusqu'à la fin
       somme_3_meilleurs = sum(des[1:])
       return somme_3_meilleurs


   def afficher_caracteristiques(self):
       print(f"\n caracteristiques de {self.nom} ---")
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
           print(f"Touche! (Jet: {de20} >= CA: {cible.classe_armure})")
           cible.subir_dommage(random.randint(1, 6))
       else:
           print(f"Manqué! (Jet: {de20})")




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
           print(f"Réussite! (Jet: {de20} >= CA: {cible.classe_armure})")
           cible.subir_dommage(random.randint(1, 6))
       else:
           print(f"L'attaque a échoué (Jet: {de20})")



# Personalisation d'un héros et d'un monstre
joueur = Heros("Valiant", "Humain", "homo-sapien", "Guerrier")
monstre = Kobold("Rask", "Kobold", "Monstre", "Voleur")


# Affichage des stats générées avec les 3 meilleurs dés
joueur.afficher_caracteristiques()
monstre.afficher_caracteristiques()


# Simulation d'un tour de combat
joueur.attaquer(monstre)


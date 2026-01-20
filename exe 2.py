import random


class NPC:
    def __init__(self, nom, race, espece, pv, metier):

        self.force = self.calcul_habilité
        self.agilité = self.calcul_habilité
        self.constitution = self.calcul_habilité
        self.intelligence = self.calcul_habilité
        self.sagesse = self.calcul_habilité
        self.charisme = self.calcul_habilité
        self.classe_armure = self.calcul_habilité
        self.nom = nom
        self.race = race
        self.espece = espece
        self.pv = pv
        self.metier = metier

    def calcul_habilité(self):

        dés = []

        for i in range(4):
            dés.append(1,6)


        dés.sort()
       somme_3_meilleurs = sum







C = NPC(force = random.randint(4, 24), agilité = random.randint(4, 24), constitution = random.randint(4, 24),
         intelligence = random.randint(4, 24), sagesse = random.randint(4, 24), charisme=  random.randint(4, 24),
         classe_armure = random.randint(1,12), nom = ('BOB'), race = ('European'),
         espece = ('Humain'), pv = random.randint(1,20), metier = ('Chasseur'))

print(f'force:{C.force} ')
print(f'agilité:{C.agilité} ')
print(f'constitution:{C.constitution} ')
print(f'intelligence:{C.intelligence} ')
print(f'sagesse:{C.sagesse} ')
print(f'charisme:{C.charisme} ')
print(f'classe_armure:{C.classe_armure} ')
print(f'le nom de NPC est: {C.nom} ')
print(f'la race de NPC est: {C.race} ')
print(f'espece de NPC est: {C.espece} ')
print(f'le pv de NPC est: {C.pv} ')
print(f'le metier de NPC est: {C.metier} ')




class kabold(NPC):
    def __init__(self, force, agilité, constitution, intelligence, sagesse, charisme, classe_armure, nom, race, espece, pv, metier ):
        super().__init__(force, agilité, constitution, intelligence, sagesse, charisme, classe_armure, nom, race, espece, pv, metier )

        self.receive_damgage = random.randint(1, 6)


K = kabold(force = random.randint(4, 24), agilité = random.randint(4, 24), constitution = random.randint(4, 24),
         intelligence = random.randint(4, 24), sagesse = random.randint(4, 24), charisme=  random.randint(4, 24),
         classe_armure = random.randint(1,12), nom = print('Kabold 1'), race = print('Kabold'),
         espece = print('Kabold'), pv = random.randint(1,20), metier = print('Monstre'))



print(f'force:{C.force} ')
print(f'agilité:{C.agilité} ')
print(f'constitution:{C.constitution} ')
print(f'intelligence:{C.intelligence} ')
print(f'sagesse:{C.sagesse} ')
print(f'charisme:{C.charisme} ')
print(f'classe_armure:{C.classe_armure} ')
print(f'votre nom est: {C.nom} ')
print(f'votre race est: {C.race} ')
print(f'votre espece est: {C.espece} ')
print(f'votre pv est: {C.pv} ')
print(f'votre metier est: {C.metier} ')













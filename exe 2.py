import random


class NPC:
    def __init__(self, force, agilité, constitution, intelligence, sagesse, charisme, classe_armure, nom, race, espece, pv, metier):

        self.force =force
        self.agilité = agilité
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self.charisme = charisme
        self.classe_armure = classe_armure
        self.nom = nom
        self.race = race
        self.espece = espece
        self.pv = pv
        self.metier = metier





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
    def __init__(self):
        super().__init__()




K = kabold(force = random.randint(4, 24), agilité = random.randint(4, 24), constitution = random.randint(4, 24),
         intelligence = random.randint(4, 24), sagesse = random.randint(4, 24), charisme=  random.randint(4, 24),
         classe_armure = random.randint(1,12), nom = input('Ecris ton nom'), race = input('Entrer votre race'),
         espece = input('Entrer votre espece'), pv = random.randint(1,20), metier = input('Entrer votre metier'))



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













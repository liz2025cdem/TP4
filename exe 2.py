import random


class Hero:
    def __init__(self, force, agilité, constitution, intelligence, sagesse, charisme):

        self.force =force
        self.agilité = agilité
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self.charisme = charisme


C = Hero(force = random.randint(4, 24), agilité = random.randint(4, 24), constitution = random.randint(4, 24),
         intelligence = random.randint(4, 24), sagesse = random.randint(4, 24), charisme=  random.randint(4, 24))

print(f'force:{C.force} ')
print(f'agilité:{C.agilité} ')
print(f'constitution:{C.constitution} ')
print(f'intelligence:{C.intelligence} ')
print(f'sagesse:{C.sagesse} ')
print(f'charisme:{C.charisme} ')









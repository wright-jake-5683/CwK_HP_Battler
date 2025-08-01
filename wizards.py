import random

class Wizard:
    def __init__(self, name, house, strength, weakness, resistance, moveSet):
        self.name = name
        self.house = house
        self.strength = strength
        self.weakness = weakness
        self.resistance = resistance
        self.moveSet = moveSet

        #randomly generated properties
        self.health = random.randint(115, 150)
        self.attack = random.randint(80, 115)
        self.defense = random.randint(80,115)
        self.speed = random.randint(80, 115)

        
    def calculateDamage(self, move, attack, opponent):
        STAB = move.STAB
        if (move.spell_type in self.weakness):
            typeEffect = 2.0
            print(f"{opponent} used {move.move}... it's super effective!")
        elif (move.spell_type in self.resistance):
            typeEffect = 0.5
            print(f"{opponent} used {move.move}... it was not very effective...")
        else:
            typeEffect = 1.0
            print(f"{opponent} used {move.move}...")

        randomMod = random.uniform(0.85, 1.0)
        crit = random.randint(1,2)
        attackMod = STAB * typeEffect * crit * randomMod
        defense = self.defense

        damage = (((0.44) * (attack/defense) * move.basePower + 2) * attackMod)
        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

#-------------------------------------------------------------------------------#

class Gryffindor(Wizard):
    def __init__(self, name):
        super().__init__(name, "Gryffindor", "Burst", "Curses", "LT Damage", ["BasicCast", "Stupefy"])

class Slytherin(Wizard):
    def __init__(self, name):
        super().__init__(name, "Slytherin", "Curses", "Counter Spell", "Burst", ["BasicCast", "Confringo"])

class Hufflepuff(Wizard):
    def __init__(self, name):
        super().__init__(name, "Hufflepuff", "Counter Spell", "LT Damage", "Curses", ["BasicCast", "Depulso"])

class Ravenclaw(Wizard):
    def __init__(self, name):
        super().__init__(name, "Ravenclaw", "LT Damage", "Burst", "Counter Spell", ["BasicCast", "Incendio"])
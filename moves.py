class Moves:
    def __init__(self, move, spell_type, basePower, strength):
        self.move = move
        self.spell_type =  spell_type
        self.basePower = basePower
        self.strength = strength
        if (self.spell_type == self.strength):
            self.STAB = 1.5
        else:
            self.STAB = 1.0


#---------------------------------------------------------------------------------------

class BasicCast(Moves):
    def __init__(self, strength):
        super().__init__("Basic Cast", "Normal", 40, strength)

class Stupefy(Moves):
    def __init__(self, strength):
        super().__init__("Stupefy", "Burst", 50, strength)

class Confringo(Moves):
    def __init__(self, strength):
        super().__init__("Confringo", "Curses", 50, strength)

class Depulso(Moves):
    def __init__(self, strength):
        super().__init__("Depulso", "Counter Spell", 50, strength)

class Incendio(Moves):
    def __init__(self, strength):
        super().__init__("Incendio", "LT Damage", 50, strength)
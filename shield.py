from weaponInterface import Weapon

class Shield(Weapon):

    def __init__(self):
        self.is_up = False
        self.base_defense = 3
        self.turns = 1
        self.turns_since_last_defense = 0

    def attack(self):
        pass
    def put_down(self):
        self.is_up = False
        pass
    def is_shield_up(self):
        return self.is_up

    def defend(self):
        return self.base_defense

    def defense(self):
        if not self.is_up:
            self.is_up = True
        pass
    def get_movements(self):
        pass
    def cooldown(self):
        self.turns_since_last_defense -= 1
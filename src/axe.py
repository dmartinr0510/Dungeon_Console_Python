from src.attacks import *
from src.weaponInterface import Weapon

class Axe(Weapon):

    def __init__(self):
        self.base_dmg = 20
        self.turns = 3
        self.turns_since_last_attack = 0

    def attack(self):

        if self.turns_since_last_attack == 0:
            self.turns_since_last_attack = self.turns
            return axe_attack(self)
        else:
            print("Weapon on CD")
            return -1

    def defense(self):
        pass
    def get_movements(self):
        pass
    def cooldown(self):
        if self.turns_since_last_attack > 0:
            self.turns_since_last_attack -= 1

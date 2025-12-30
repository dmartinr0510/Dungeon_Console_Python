from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass

    @abstractmethod
    def get_movements(self):
        pass

    def cooldown(self):
        if self.turns_since_last_attack > 0:
            self.turns_since_last_attack -= 1
    def reset_cooldown(self):
        self.turns_since_last_attack = 0
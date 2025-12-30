from src.tamaniosPociones import Tamanios


class HealthPotions:

    def __init__(self,heal_points : Tamanios):
        self.heal_points = heal_points.value

    def heal(self):
        return self.heal_points

    def getHealPoints(self):
        return self.heal_points
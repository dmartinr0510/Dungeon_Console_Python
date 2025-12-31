from typing import override

from src.item import Item
from config.settings import CURSIVE,DEFAULT
from src.tamaniosPociones import Tamanios

ITEM_DESCRIPTIONS = {
    "Coin" : f"""Gold made item used to test pirates teeth""",
    "Skull": f"""Just a skull""",
    "Heal Potion": f"""It has a note: "{CURSIVE}They call me drunk,but this shit makes me fill better{DEFAULT}"""
}

class Coin(Item):

    def __init__(self,desc):
        super().__init__("Coin",desc)


class Skull(Item):

    def __init__(self,desc):
        super().__init__("Skull",desc)

class HealthPotion(Item):

    @override
    def __init__(self, desc):
        super().__init__("Heal Potion",desc)
        self.heal_points = Tamanios.TINY.value

    def heal(self):
        return self.heal_points

    def getHealPoints(self):
        return self.heal_points

ITEMS = {
    "Coin": Coin,
    "Skull": Skull,
    "Heal Potion": HealthPotion,
}
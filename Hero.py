from settings import GREEN, DEFAULT
from healthPotions import HealthPotions
from tamaniosPociones import *

class Hero:
    def __init__(self,weapon,shield,health_points):
        self.health_points = health_points
        self.max_health = health_points
        self.weapon = weapon
        self.shield = shield
        self.protection = 0
        self.potions = []
        self.max_potions = 3
        self.name = "Hero"

    def do_dmg(self):
        dmg = self.weapon.attack()
        self.reduce_cooldowns()
        self.shield.put_down()
        return dmg

    def recive_dmg(self,dmg):
        dmg_recived = dmg - self.protection
        if dmg_recived > 0:
            self.health_points -= dmg_recived
        if self.shield.is_shield_up():
            self.shield.put_down()
            self.protection -= self.shield.defend()
        self.reduce_cooldowns()

    def defend(self):
        self.shield.is_up = True
        self.protection += self.shield.defend()

    def reduce_cooldowns(self):
        self.weapon.cooldown()
        self.shield.cooldown()

    def reset_cooldowns(self):
        self.weapon.reset_cooldown()

    def generate_potions(self):
        for i in range(self.max_potions):
            self.potions.append(HealthPotions(Tamanios.TINY))

    def recive_heal(self, potion):
        heal = potion.heal()
        new_hp = self.health_points + heal

        if new_hp > self.max_health:
            new_hp = self.max_health
            heal = self.max_health-self.health_points

        self.health_points = new_hp

        print(f"{self.name} Has recovered:{GREEN}{heal}{DEFAULT} hp New Health: {GREEN}{self.health_points}{DEFAULT}")

        self.potions.remove(potion)
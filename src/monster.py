from config.fight_resources import MONSTERS_SETTINGS


class Monster():

    def __init__(self,name):

        if name in MONSTERS_SETTINGS:
            data = MONSTERS_SETTINGS[name]
            self.name = name.capitalize()
            self.health_points = data["hp"]
            self.armor = data["armor"]
            self.dmg = data["dmg"]
            self.attack_movement = data["attack"]
            self.cooldown = data["cooldown"]
            self.cooldown_msg = data["cooldown_msg"]

        self.turns_since_last_attack = 0
        self.pos = (0,0)
        self.alive = True
    def recive_dmg(self,dmg):
        if not dmg == - 1:
            dmg_recived = dmg - self.armor
            if dmg_recived > 0:
                self.health_points -= dmg_recived
            else:
                print("Parried ( Not enough DMG)")

    def kill_monster(self):
        self.alive = False

    def get_hp(self):
        return self.health_points

    def attack(self):
        if self.turns_since_last_attack == 0:
            self.turns_since_last_attack = self.cooldown
            return self.attack_movement(self)
        else:
            self.cooldown_msg()
            return 0

    def cooldown_attack(self):
        if self.turns_since_last_attack > 0:
            self.turns_since_last_attack -= 1
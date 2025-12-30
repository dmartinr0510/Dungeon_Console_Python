from config.settings import RED, DEFAULT,GREEN
def zombie_attack(monster):
    print(f"{monster.name} attacked doing: {RED}{monster.dmg}{DEFAULT} dmg")
    return monster.dmg

def vampire_attack(monster):
    print(f"{monster.name} attacked doing: {RED}{monster.dmg}{DEFAULT} dmg  and Healing himself {GREEN}{monster.dmg // 2}{DEFAULT} hp" )
    monster.health_points += monster.dmg // 2
    return monster.dmg

def skeleton_attack(monster):
    print(f"{monster.name} attacked doing: {RED}{monster.dmg}{DEFAULT} dmg")
    return monster.dmg

def axe_attack(weapon):
    print(f"Hero used Axe doing: {RED}{weapon.base_dmg}{DEFAULT} dmg")
    return weapon.base_dmg

def default_cd_msg():
    pass

def skeleton_cd_msg():
    print(f"{RED}Skeleton{DEFAULT} is reloading...")

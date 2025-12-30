import settings
def zombie_attack(monster):
    print(f"{monster.name} attacked doing: {settings.RED}{monster.dmg}{settings.DEFAULT} dmg")
    return monster.dmg

def vampire_attack(monster):
    print(f"{monster.name} attacked doing: {settings.RED}{monster.dmg}{settings.DEFAULT} dmg  and Healing himself {settings.GREEN}{monster.dmg // 2}{settings.DEFAULT} hp" )
    monster.health_points += monster.dmg // 2
    return monster.dmg

def skeleton_attack(monster):
    print(f"{monster.name} attacked doing: {settings.RED}{monster.dmg}{settings.DEFAULT} dmg")
    return monster.dmg

def axe_attack(weapon):
    print(f"Hero used Axe doing: {settings.RED}{weapon.base_dmg}{settings.DEFAULT}")
    return weapon.base_dmg

def default_cd_msg():
    pass

def skeleton_cd_msg():
    print(f"{settings.RED}Skeleton{settings.DEFAULT} is reloading...")

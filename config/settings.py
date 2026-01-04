import random
#TEXT SETTINGS
RED = "\033[31m"
DEFAULT = "\033[0m"
CURSIVE = "\033[3m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
#ROOM SETTINGS
TILES = {
    "q": "\u2554",  # ╔ (Top Left)
    "p": "\u2557",  # ╗ (Top Right)
    "z": "\u255a",  # ╚ (Bottom Left)
    "m": "\u255d",  # ╝ (Bottom Right)
    "x": "\u2550",  # ═ (Horizontal)
    "y": "\u2551",  # ║ (Vertical)
    ".": " ",       # Suelo vacío
    "P": "@",       # Jugador
    "M": "\u00a3",  # Enemigo
    "D": "\u2620",  # Enemigo Muerto
    "c": "#"        # Cofre
}


ROOM_WIDTH = 23
ROOM_HEIGHT = 7

#DUNGEON SETTINGS
DUNGEON_WIDTH = 10
DUNGEON_HEIGHT = 10
DUNGEON_MAX_ROOMS = 10
DUNGEON_MAX_MONSTERS = 7
dungeon_current_monsters = 0
DUNGEON_MAX_LOOT = 3
generated_rooms = 0
dungeon_current_chests = 0
rooms_with_chest = random.sample(range(1, DUNGEON_MAX_ROOMS + 1), DUNGEON_MAX_LOOT)

MENU_SYMBOLS = {
    "go_up": "[W]",
    "go_down": "[S]",
    "go_left": "[A]",
    "go_right": "[D]",
    "loot_icon": "\u25CB",   # ○
    "fight_icon": "\u2694",  # ⚔
    "inventory_icon": "\u00a7" #§
}

DUNGEON_MAP_TILES = {
    "#" : "\u2591 ",
    "S" : "\u25a0 ",
    "R" : "\u25a0 "
}



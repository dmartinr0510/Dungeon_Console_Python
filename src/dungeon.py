import sys,os,time
from pyfiglet import Figlet

import src.utils.compat
from src.utils.compat import *

from config.settings import ROOM_WIDTH, ROOM_HEIGHT, MENU_SYMBOLS, RED, DEFAULT, GREEN, YELLOW
from config.fight_resources import *

from src.roomGenerator import Generator
from src.map import Map
from src.room import Room
from src.dungeonGenerator import DungeonGen
from src.Hero import Hero
from src.axe import Axe
from src.shield import Shield


class Dungeon:

    def __init__(self):
        self.dungeon = DungeonGen()
        self.layout = self.dungeon.gen_layout()
        self.rooms = []
        self.in_fight = False
        self.hero = Hero(Axe(), Shield(), 100)
        self.map = Map(self.dungeon, self)
        #inventario
        self.selected_idx = 0
        self.in_innv = False
        self.looking_at_item = False
        self.in_chest = False





    def gen_dungeon_rooms(self):
        w = len(self.layout[0])  # Width
        h = len(self.layout)  # Height

        for row in range(h):

            for col in range(w):
                south = east = north = west = False
                starter = False

                if self.layout[row][col] == "S":
                    starter = True

                if self.layout[row][col] in ["R", "S", "."]:


                    # Check SOUTH:
                    if row + 1 < h and self.layout[row + 1][col] in ["R", "S","."]:
                        south = True

                    # Check NORTH:
                    if row - 1 >= 0 and self.layout[row - 1][col] in ["R", "S","."]:
                        north = True

                    # Check EAST:
                    if col + 1 < w and self.layout[row][col + 1] in ["R", "S","."]:
                        east = True

                    # Check WEST:
                    if col - 1 >= 0 and self.layout[row][col - 1] in ["R", "S", "."]:
                        west = True

                    room_ascii = Generator(ROOM_WIDTH, ROOM_HEIGHT, self.layout[row][col])
                    roomgrid = room_ascii.generate_room(north,south,east,west)
                    self.rooms.append(Room(north, south, east, west, ROOM_WIDTH, ROOM_HEIGHT,roomgrid, (row, col),starter))


    def get_room_coords(self,row,col):

        for room in self.rooms:
            if room.get_coords() == (row,col):
                return room
        return None

    def start_dungeon(self):
        for room in self.rooms:
            if room.is_starter():
                self.hero.generate_potions()
                self.start_gameloop(room)
                break

    @staticmethod
    def draw_room(room):
        room.print_room()

    def draw_actions_rooms(self, room):
        up = MENU_SYMBOLS["go_up"] if room.north_entrance else "   "
        down = MENU_SYMBOLS["go_down"] if room.south_entrance else "   "
        left = MENU_SYMBOLS["go_left"] if room.west_entrance else "   "
        right = MENU_SYMBOLS["go_right"] if room.east_entrance else "   "
        fight = MENU_SYMBOLS["fight_icon"]
        loot = MENU_SYMBOLS["loot_icon"]
        inventory = MENU_SYMBOLS["inventory_icon"]
        print("============================================")
        print(f"               {up}         ‖   q) exit")
        print(f"           {left} {down} {right}     ‖   {"e) " + str(loot) + "loot" if room.get_has_loot() else ""}")
        print(f"                           ‖   {"f) " + str(fight) + "fight" if room.fighteable() else ""}")
        print(f"                           ‖   i) {inventory}Inventory")
        print("============================================")

    def start_gameloop(self, current_room):
        clear_screen()
        self.draw_room(current_room)
        self.draw_actions_rooms(current_room)
        self.map.draw_map(current_room)
        while True:
            char = get_char().lower()
            if current_room.are_monsters:
                current_monster = current_room.monsters[0]
            # 1. Mapeo de dirección y validación de puerta
            direccion = None

            if char == "w" and current_room.north_entrance and not self.in_fight and not self.in_innv:
                direccion = (-1, 0)
                self.in_chest = False
            elif char == "s" and current_room.south_entrance and not self.in_fight and not self.in_innv:
                direccion = (1, 0)
                self.in_chest = False
            elif char == "a" and current_room.west_entrance and not self.in_fight and not self.in_innv:
                direccion = (0, -1)
                self.in_chest = False
            elif char == "d" and current_room.east_entrance and not self.in_fight and not self.in_innv:
                direccion = (0, 1)
                self.in_chest = False
            elif char == "\x1b[b" and self.in_innv:
                if self.selected_idx < len(self.hero.inventory.items)-1:
                    self.selected_idx += 1
                    clear_screen()
                    self.hero.show_inventory(self.selected_idx)
                    continue
            elif char == "\x1b[a" and self.in_innv:
                if self.selected_idx > 0:
                    self.selected_idx -= 1
                    clear_screen()
                    self.hero.show_inventory(self.selected_idx)
                    continue
            elif char =="o" and self.in_innv and not self.looking_at_item:
                self.looking_at_item = True
                self.hero.render_current_item(self.selected_idx)
                continue
            elif char =="o" and self.in_innv and self.looking_at_item:
                self.selected_idx = 0
                self.hero.show_inventory(self.selected_idx)
                self.looking_at_item = False
                continue
            elif char == "e" and current_room.looteable():
                current_room.open_chest()
                self.in_chest = True
                continue
            elif char == "l" and self.looking_at_item:
                self.hero.inventory.remove_items(self.selected_idx)
                self.selected_idx = 0
                self.hero.show_inventory(self.selected_idx)
                self.looking_at_item = False
            elif char == "l" and self.in_chest:
                if self.in_chest:
                    for item in current_room.get_chest().get_items()[:]:
                        if len(self.hero.inventory.get_items()) < self.hero.inventory.get_capacity():
                            if self.hero.inventory.add_item(item):
                                current_room.get_chest().remove_item(item)

                        else:
                            print(f"------{RED} INVENTORY FULL {DEFAULT}------")


                    current_room.open_chest()
                continue

            elif char == "i" and self.in_innv:
                self.in_innv = False

                if not self.in_fight:
                    direccion = (0,0)
                if self.in_fight and current_room.fighteable():
                    self.combat_bg()
                    self.draw_actions_fight(current_monster)

            elif char == "i" and not self.in_innv:
                self.in_chest = False
                self.in_innv = True
                self.selected_idx = 0
                self.hero.show_inventory(self.selected_idx)
                continue
            elif char == "f" and not self.in_fight and current_room.fighteable():
                self.in_chest = False
                self.fight_situation(current_monster)
                self.in_fight = True
                continue
            elif char == "1" and self.in_fight and not self.in_innv:

                 current_monster.recive_dmg(self.hero.do_dmg())
                 if current_monster.health_points > 0:
                    self.hero.recive_dmg(current_monster.attack())
                    current_monster.cooldown_attack()

                 if not self.game_over(current_monster):
                     print("--")
                     print("Next Turn")
                     print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                     print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                     print(f"Potions: ({GREEN}{len(self.hero.inventory.potions)}{DEFAULT}/{self.hero.inventory.max_potions}) ")
                     print("--")
                 else:
                     self.in_fight = False
                     direccion = (0,0)
                     self.hero.reduce_cooldowns()
            elif char == "2" and self.in_fight and not self.in_innv:
                self.hero.defend()
                self.hero.recive_dmg(current_monster.attack())
                current_monster.cooldown_attack()
                if not self.game_over(current_monster):
                    print("--")
                    print("Next Turn")
                    print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                    print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                    print(f"Potions: ({GREEN}{len(self.hero.inventory.potions)}{DEFAULT}/{self.hero.inventory.max_potions}) ")
                    print("--")
                else:
                    self.in_fight = False
                    direccion = (0,0)
                    self.hero.reduce_cooldowns()
            elif char == "3" and (self.in_fight or self.in_innv) and not self.looking_at_item:
                if not self.in_innv:
                    if not len(self.hero.inventory.potions) == 0:
                        self.hero.recive_heal(self.hero.inventory.potions[0])
                    else:
                        print("There is no potion to heal")
                    current_monster.cooldown_attack()
                    if not self.game_over(current_monster):
                        print("--")
                        print("Next Turn")
                        print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                        print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                        print(f"Potions: ({GREEN}{len(self.hero.inventory.potions)}{DEFAULT}/{self.hero.inventory.max_potions}) ")
                        print("--")
                    else:
                        self.in_fight = False
                        direccion = (0,0)
                        self.hero.reduce_cooldowns()
                else:
                    if not len(self.hero.inventory.potions) == 0:
                        self.hero.recive_heal(self.hero.inventory.potions[0])
                        print(f"{GREEN} HEALED {DEFAULT}")
                        time.sleep(1)
                    else:
                        print("There is no potion to heal")
                    current_monster.cooldown_attack()

                    self.hero.show_inventory(self.selected_idx)
                    continue
            elif char == "4" and self.in_fight:
                self.escape_situation()
                current_monster.cooldown_attack()
                direccion = (0, 0)
                self.in_fight = False

            elif char == "q":
                self.exit()


            #Si la dirección es válida, buscamos la sala
            if direccion:
                target_coords = (
                    current_room.coords[0] + direccion[0],
                    current_room.coords[1] + direccion[1]
                )

                # Busca el objeto Room en la lista
                found_room = None
                for r in self.rooms:
                    if r.coords == target_coords:
                        found_room = r
                        break

                # Si encuentra la sala, limpia y actualiza
                if found_room:
                    clear_screen()
                    found_room.print_room()
                    self.draw_actions_rooms(found_room)
                    self.map.draw_map(found_room)
                    current_room = found_room  # Actualiza el puntero para el siguiente input

                else:
                    print("\n[!] Error: No se encontró la habitación en el sistema.")

    def move_player(self, current_room, direction):
        row, col = current_room.coords
        if direction == "north":
            row -= 1
        elif direction == "south":
            row += 1
        elif direction == "east":
            col += 1
        elif direction == "west":
            col -= 1

        # Busca si existe la habitación en esas coordenadas
        for room in self.rooms:
            if room.coords == (row, col):
                return room  # Devuelve la habitación encontrada
        return None  # Si no hay nada, devuelve None

    def exit(self):
        clear_screen()
        print("Gracias por jugar.")
        print("Saliendo del juego...")
        sys.exit()  # Cierra el proceso de Python inmediatamente

    @staticmethod
    def combat_animation():
        for frame in FIGHT_ANIMATION.values():
            clear_screen()
            print(frame)
            time.sleep(0.06)

    @staticmethod
    def combat_animation_backwards():
        for frame in FIGHT_ANIMATION.values().__reversed__():
            clear_screen()
            print(frame)
            time.sleep(0.06)
    @staticmethod
    def combat_bg():
        clear_screen()
        print(FIGHT_BACKGROUND)

    def draw_actions_fight(self,current_monster):

        print("==================================================================================")
        print(f"        1) Attack                  3) Heal                  ‖        q) exit")
        print(f"                                                            ‖                     ")
        print(f"        2) Defend                  4) Escape                ‖        i) {MENU_SYMBOLS["inventory_icon"]}Inventory      ")
        print("==================================================================================")
        print("COMBAT LOG")
        print("-------------")
        print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
        print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
        print(f"Potions: ({GREEN}{len(self.hero.inventory.potions)}{DEFAULT}/{self.hero.inventory.max_potions}) ")
        print("-------------")

    def fight_situation(self,current_monster):
        self.combat_animation()
        self.combat_bg()
        self.draw_actions_fight(current_monster)

    def escape_situation(self):
        self.combat_animation_backwards()
        clear_screen()
        f = Figlet(font="standard")
        print(f.renderText(f"      ESCAPED"))
        time.sleep(1.5)

    def game_over(self,monster):
        pass_turn_by_dead_monster = False
        pass_turn_by_dead_hero = False

        if monster.get_hp() <= 0:
            pass_turn_by_dead_monster = True
            monster.kill_monster()
        if self.hero.health_points <= 0:
            pass_turn_by_dead_hero = True
        if pass_turn_by_dead_hero:
            final_fight_msg = f"GAME OVER\nHERO DEAD"
        if pass_turn_by_dead_monster:
            final_fight_msg = "MONSTER DEFEATED"

        if pass_turn_by_dead_hero or pass_turn_by_dead_monster:
            clear_screen()
            f = Figlet(font="slant")
            print(f.renderText(f"{final_fight_msg}"))
            time.sleep(2.5)
            if pass_turn_by_dead_hero:
                self.exit()
            return True
        else:
            return False


import sys,termios,tty,os,time
from  roomGenerator import Generator
from settings import ROOM_WIDTH, ROOM_HEIGHT, MENU_SYMBOLS, RED, DEFAULT, GREEN, YELLOW
import settings
from map import Map
from room import Room
from dungeonGenerator import DungeonGen
from fight_resources import *
from Hero import Hero
from axe import Axe
from pyfiglet import Figlet
#Test imports
from shield import Shield
from monster import Monster


class Dungeon:

    def __init__(self):
        self.dungeon = DungeonGen()
        self.layout = self.dungeon.gen_layout()
        self.rooms = []
        self.in_fight = False
        self.hero = Hero(Axe(),Shield(),100)
        self.map = Map(self.dungeon,self)




    def gen_dungeon_rooms(self):
        w = len(self.layout[0])  # Width
        h = len(self.layout)  # Height

        for row in range(h):

            for col in range(w):
                south = east = north = west = False
                starter = False

                if self.layout[row][col] == "S":
                    starter = True

                if self.layout[row][col] in ["R", "S"]:


                    # Check SOUTH:
                    if row + 1 < h and self.layout[row + 1][col] in ["R", "S"]:
                        south = True

                    # Check NORTH:
                    if row - 1 >= 0 and self.layout[row - 1][col] in ["R", "S"]:
                        north = True

                    # Check EAST:
                    if col + 1 < w and self.layout[row][col + 1] in ["R", "S"]:
                        east = True

                    # Check WEST:
                    if col - 1 >= 0 and self.layout[row][col - 1] in ["R", "S"]:
                        west = True

                    room_ascii = Generator(ROOM_WIDTH, ROOM_HEIGHT)
                    roomgrid = room_ascii.generate_room()
                    self.rooms.append(Room(north, south, east, west, ROOM_WIDTH, ROOM_HEIGHT, roomgrid, (row, col),starter))


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
        print(f"               {up}            q) exit")
        print(f"           {left} {down} {right}        e) {loot}loot")
        if room.fighteable():
            print(f"                              f) {fight}fight")
        else:
            print(" ")
        print(f"                              i) {inventory}Inventory")
        print("============================================")
    @staticmethod
    def getch_linux():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

    def start_gameloop(self, current_room):
        os.system("clear")
        self.draw_room(current_room)
        self.draw_actions_rooms(current_room)
        self.map.draw_map(current_room)

        while True:
            char = self.getch_linux().lower()

            # 1. Mapeo de dirección y validación de puerta
            direccion = None

            if char == "w" and current_room.north_entrance and not self.in_fight:
                direccion = (-1, 0)
            elif char == "s" and current_room.south_entrance and not self.in_fight:
                direccion = (1, 0)
            elif char == "a" and current_room.west_entrance and not self.in_fight:
                direccion = (0, -1)
            elif char == "d" and current_room.east_entrance and not self.in_fight:
                direccion = (0, 1)
            elif char == "f" and not self.in_fight and current_room.fighteable():
                current_monster = current_room.monsters[0]
                self.fight_situation(current_room,current_monster)
                self.in_fight = True

            elif char == "1" and self.in_fight:

                 current_monster.recive_dmg(self.hero.do_dmg())
                 self.hero.recive_dmg(current_monster.attack())
                 current_monster.cooldown_attack()

                 if not self.game_over(current_monster):
                     print("--")
                     print("Next Turn")
                     print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                     print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                     print(f"Potions: ({GREEN}{len(self.hero.potions)}{DEFAULT}/{self.hero.max_potions}) ")
                     print("--")
                 else:
                     print("Hello")
                     self.in_fight = False
                     direccion = (0,0)
                     self.hero.reduce_cooldowns()


            elif char == "2" and self.in_fight:
                self.hero.defend()
                self.hero.recive_dmg(current_monster.attack())
                current_monster.cooldown_attack()
                if not self.game_over(current_monster):
                    print("--")
                    print("Next Turn")
                    print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                    print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                    print(f"Potions: ({GREEN}{len(self.hero.potions)}{DEFAULT}/{self.hero.max_potions}) ")
                    print("--")
                else:
                    self.in_fight = False
                    direccion = (0,0)
                    self.hero.reduce_cooldowns()

            elif char == "3" and self.in_fight:
                if not len(self.hero.potions) == 0:
                    self.hero.recive_heal(self.hero.potions[0])
                else:
                    print("There is no potion to heal")
                current_monster.cooldown_attack()
                if not self.game_over(current_monster):
                    print("--")
                    print("Next Turn")
                    print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
                    print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
                    print(f"Potions: ({GREEN}{len(self.hero.potions)}{DEFAULT}/{self.hero.max_potions}) ")
                    print("--")
                else:
                    self.in_fight = False
                    direccion = (0,0)
                    self.hero.reduce_cooldowns()
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
                    os.system('clear')
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
        os.system('clear')
        print("Gracias por jugar a la Mazmorra.")
        print("Saliendo del juego...")
        sys.exit()  # Cierra el proceso de Python inmediatamente

    @staticmethod
    def combat_animation():
        for frame in FIGHT_ANIMATION.values():
            os.system('clear')
            print(frame)
            time.sleep(0.06)

    @staticmethod
    def combat_animation_backwards():
        for frame in FIGHT_ANIMATION.values().__reversed__():
            os.system('clear')
            print(frame)
            time.sleep(0.06)
    @staticmethod
    def combat_bg():
        os.system('clear')
        print(FIGHT_BACKGROUND)

    def draw_actions_fight(self,current_monster):

        print("==================================================================================")
        print(f"        1) Attack                  3) Heal                                q) exit")
        print(f"                                                                                 ")
        print(f"        2) Defend                  4) Escape                                     ")
        print("==================================================================================")
        print("COMBAT LOG")
        print("-------------")
        print(f"{RED}{current_monster.name}{DEFAULT} hp: {current_monster.health_points}")
        print(f"{YELLOW}{self.hero.name}{DEFAULT} hp: {GREEN}{self.hero.health_points}{DEFAULT}")
        print(f"Potions: ({GREEN}{len(self.hero.potions)}{DEFAULT}/{self.hero.max_potions}) ")
        print("-------------")

    def fight_situation(self,room,current_monster):
        self.combat_animation()
        self.combat_bg()
        self.draw_actions_fight(current_monster)

    def escape_situation(self):
        self.combat_animation_backwards()
        os.system("clear")
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
            os.system("clear")
            f = Figlet(font="slant")
            print(f.renderText(f"{final_fight_msg}"))
            time.sleep(2.5)
            if pass_turn_by_dead_hero:
                self.exit()
            return True
        else:
            return False


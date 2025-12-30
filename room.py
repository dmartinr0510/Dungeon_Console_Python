from fight_resources import MONSTERS_NAMES
from monster import Monster
from settings import TILES
import random

class Room:
    def __init__(self,north,south,east,west,width,height,grid,coords,starter):
        self.grid = grid
        self.north_entrance = north
        self.south_entrance = south
        self.east_entrance = east
        self.west_entrance = west
        self.width = width
        self.height = height
        self.are_monsters = False
        self.coords = coords
        self.starter = starter
        self.monsters = []
        self.visited = False

    """
    q = top_left_corner
    p = top_right_corner
    m = bottom_right_corner
    z = bottom_left_corner
    y = vertical
    x = horizontal
    """

    def print_room(self):
        mid_h = self.width // 2
        mid_v = self.height // 2

        for row in range(self.height):
            linea_visual = "        "
            for col in range(self.width):
                cell = self.grid[row][col]
                if col == mid_v and row == mid_h:
                    char = TILES.get(cell, " ")
                elif row == 0 and self.north_entrance and (mid_h - 1 <= col <= mid_h + 1):
                    char = " "
                elif row == self.height - 1 and self.south_entrance and (mid_h - 1 <= col <= mid_h + 1):
                    char = " "
                elif col == 0 and row == mid_v and self.west_entrance:
                    char = " "
                elif col == self.width - 1 and row == mid_v and self.east_entrance:
                    char = " "
                else:
                    char = TILES.get(cell, " ")
                    if cell == "M":
                        if not self.are_monsters:
                            self.add_monster(Monster(random.choice(MONSTERS_NAMES)))
                            self.are_monsters = True
                        elif not self.monsters[0].alive:
                            char = TILES.get("D", " ")


                linea_visual += char
            print(linea_visual, flush=True)

    def add_monster(self,monster):
        self.monsters.append(monster)

    def is_starter(self):
        return self.starter
    def print_grid(self):
        for i in range(len(self.grid)):
            print("")
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end="")

    def fighteable(self):
        if self.are_monsters and self.monsters[0].alive:
            return True
        else:
            return False

    def set_visited(self):
        self.visited = True
    def get_visited(self):
        return self.visited
    def get_coords(self):
        return self.coords
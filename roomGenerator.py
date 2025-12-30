import random

import settings


class Generator:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[" " for _ in range(width)] for _ in range(height)]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def generate_room(self):
        for row in range(self.height):
            for col in range (self.width):
                if row == 0 and col == 0:
                    self.grid[row][col] = "q"
                elif row == 0 and col == self.width - 1:
                    self.grid[row][col] = "p"
                elif row == self.height - 1 and col == 0:
                    self.grid[row][col] = "z"
                elif row == self.height - 1 and col == self.width - 1:
                    self.grid[row][col] = "m"
                elif row == 0 or row == self.height - 1:
                    self.grid[row][col] = "x"
                elif col == 0 or col == self.width - 1:
                    self.grid[row][col] = "y"
                elif row == self.height // 2 and col == self.width // 2:
                    self.grid[row][col] = "P"
                else:
                    self.grid[row][col] = "."
                # Intentar buscar una posición válida hasta que no sea el centro ni pared
        while True:
            r = random.randint(1, self.height - 2)
            c = random.randint(1, self.width - 2)

            # Si no es el centro, es válida
            if (r, c) != (self.height // 2, self.width // 2):
                if settings.dungeon_current_monsters < settings.DUNGEON_MAX_MONSTERS:
                    self.grid[r][c] = "M"
                    settings.dungeon_current_monsters += 1
                break
        return self.grid
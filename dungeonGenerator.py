from settings import DUNGEON_WIDTH, DUNGEON_HEIGHT, DUNGEON_MAX_ROOMS
import random


class DungeonGen:
    def __init__(self):
        self.layout = [["#" for _ in range(DUNGEON_WIDTH)] for _ in range(DUNGEON_HEIGHT)]
        self.max_rooms = DUNGEON_MAX_ROOMS
        self.start_pos = None

    def gen_layout(self):
        #random starting point
        curr_row = random.randint(0, DUNGEON_HEIGHT - 1)
        curr_col = random.randint(0, DUNGEON_WIDTH - 1)

        self.start_pos = (curr_row, curr_col)
        self.layout[curr_row][curr_col] = "S"
        rooms_created = 1

        # safety break in case max_rooms is impossible to reach
        attempts = 0
        max_attempts = 1000

        while rooms_created < self.max_rooms and attempts < max_attempts:
            attempts += 1

            if self.layout[curr_row][curr_col] == "#":
                if (curr_row, curr_col) == self.start_pos:
                    self.layout[curr_row][curr_col] = "S"
                else:
                    self.layout[curr_row][curr_col] = "R"
                rooms_created += 1

            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

            # Check limits
            if 0 <= curr_row + direction[0] < DUNGEON_HEIGHT and 0 <= curr_col + direction[1] < DUNGEON_WIDTH:
                curr_row += direction[0]
                curr_col += direction[1]

        return self.layout

    def print_layout(self):
        for r in range(DUNGEON_HEIGHT):
            row_display = []
            for c in range(DUNGEON_WIDTH):
                if (r, c) == self.start_pos:
                    row_display.append("S")
                else:
                    row_display.append(self.layout[r][c])
            print(" ".join(row_display))
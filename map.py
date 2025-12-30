from settings import DUNGEON_MAP_TILES, RED, DEFAULT,TILES


class Map():

    def __init__(self,dungeon):
        self.dungeon = dungeon


    def draw_map(self,current_room):
        dungeon_layout = self.dungeon.layout
        print("                                    " + TILES.get("q", " ") + 7*TILES.get("x", " ") + TILES.get("p", " "))
        print("                                    " + TILES.get("y", " ") + "MAP".center(7) + TILES.get("y", " "))
        print("                                    " + TILES.get("z", " ") + 7 * TILES.get("x", " ") + TILES.get("m", " "))
        for row in range(len(dungeon_layout)):
            linea_visual = "                                      "
            for col in range(len(dungeon_layout[row])):
                current_coords = (row,col)
                cell = dungeon_layout[row][col]
                if cell == "#":
                    char = DUNGEON_MAP_TILES.get(cell, " ")
                elif cell == "S" or cell == "R":
                    char = DUNGEON_MAP_TILES.get(cell, " ")

                if current_coords == current_room.coords:

                    char = RED +  char + DEFAULT

                linea_visual += char

            print(linea_visual, flush=True,)

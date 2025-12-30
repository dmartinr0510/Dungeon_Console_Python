from config.settings import DUNGEON_MAP_TILES, RED, DEFAULT,BLUE,TILES


class Map():

    def __init__(self,dungeonmap,dungeon):
        self.dungeonmap = dungeonmap
        self.dungeon = dungeon


    def draw_map(self,current_room):
        dungeon_layout = self.dungeonmap.layout
        current_room.set_visited()
        print("        " + TILES.get("q", " ") + 21*TILES.get("x", " ") + TILES.get("p", " "))
        print("        " + TILES.get("y", " ") + "MAP".center(21) + TILES.get("y", " "))



        for row in range(len(dungeon_layout)):
            linea_visual = f"        {TILES.get("y", " ")} "
            for col in range(len(dungeon_layout[row])):
                current_coords = (row,col)
                cell = dungeon_layout[row][col]

                if (cell == "S" or cell == "R" ) and self.dungeon.get_room_coords(row,col).get_visited():
                    char = DUNGEON_MAP_TILES.get("R", " ")
                elif cell == "." and self.dungeon.get_room_coords(row,col).get_visited():
                    if current_coords == current_room.coords:
                        char = RED + DUNGEON_MAP_TILES.get("R", " ") + DEFAULT
                    else:
                        char = BLUE + DUNGEON_MAP_TILES.get("R", " ") + DEFAULT
                else:
                    char = DUNGEON_MAP_TILES.get("#", " ")

                if current_coords == current_room.coords:
                    char = RED +  char + DEFAULT

                linea_visual += char

            print(f"{linea_visual}{TILES.get("y" , " ")}", flush=True,)
        print("        " + TILES.get("z", " ") + 21 * TILES.get("x", " ") + TILES.get("m"," "))


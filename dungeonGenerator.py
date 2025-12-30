from settings import DUNGEON_WIDTH, DUNGEON_HEIGHT, DUNGEON_MAX_ROOMS
import random
import math


class DungeonGen:
    def __init__(self):
        self.layout = [["#" for _ in range(DUNGEON_WIDTH)] for _ in range(DUNGEON_HEIGHT)]
        self.max_rooms = DUNGEON_MAX_ROOMS
        self.start_pos = None
        self.rooms = []

    def gen_layout(self):
        # puntos en un círculo/elipse central
        while len(self.rooms) < self.max_rooms:
            # Generar posición aleatoria en un radio central para que queden agrupadas
            radius = min(DUNGEON_WIDTH, DUNGEON_HEIGHT) // 3
            t = 2 * math.pi * random.random()
            u = random.random() + random.random()
            r = radius * (2 - u if u > 1 else u)

            row = int(DUNGEON_HEIGHT // 2 + r * math.sin(t))
            col = int(DUNGEON_WIDTH // 2 + r * math.cos(t))

            # Asegurar que está dentro y no colisiona (al ser iguales,
            # solo cheque que no sea la misma celda o adyacente)
            if 0 <= row < DUNGEON_HEIGHT and 0 <= col < DUNGEON_WIDTH:
                if (row, col) not in self.rooms:
                    self.rooms.append((row, col))
                    self.layout[row][col] = "R"

        # Conectar puntos
        # El artículo usa triangulos, pero uso L para conectar
        # con su vecina más cercana para asegurar que no hay islas.
        connected_rooms = [self.rooms[0]]
        unconnected_rooms = self.rooms[1:]

        while unconnected_rooms:
            # Buscar la habitación más cercana a la estructura ya conectada
            best_dist = float('inf')
            best_pair = None

            for r1 in connected_rooms:
                for r2 in unconnected_rooms:
                    dist = abs(r1[0]-r2[0]) + abs(r1[1]-r2[1]) # Distancia Manhattan
                    if dist < best_dist:
                        best_dist = dist
                        best_pair = (r1, r2)

            # Crear pasillo entre ellas (L-Shape como dice el artículo)
            self.create_h_line(best_pair[0], best_pair[1])
            connected_rooms.append(best_pair[1])
            unconnected_rooms.remove(best_pair[1])

        # Marcar el inicio
        start = self.rooms[0]
        self.layout[start[0]][start[1]] = "S"
        return self.layout

    def create_h_line(self, p1, p2):
        # Crea pasillos en forma de L
        row_start, col_start = p1
        row_end, col_end = p2

        # Primero horizontal, luego vertical (o viceversa)
        step_c = 1 if col_end > col_start else -1
        for c in range(col_start, col_end + step_c, step_c):
            if self.layout[row_start][c] == "#": self.layout[row_start][c] = "R"

        step_r = 1 if row_end > row_start else -1
        for r in range(row_start, row_end + step_r, step_r):
            if self.layout[r][col_end] == "#": self.layout[r][col_end] = "R"

    def print_layout(self):
        print("\n--- Dungeon Map ---")
        for row in self.layout:

            line = " ".join(row)
            print(line)
        print("-------------------\n")
import random

import settings


class Generator:

    def __init__(self, width, height, type):
        self.width = width
        self.height = height
        self.grid = [[" " for _ in range(width)] for _ in range(height)]
        if type in["R","S"]:
            self.type = "room"
        else:
            self.type = "corridor"

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def generate_room(self,north,south,east,west):

        if self.type == "room":
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
        else:
            # 1. Crear la matriz vacía con espacios
            self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

            # Calculamos centro y posiciones de las paredes
            cy = self.height // 2
            cx = self.width // 2

            # Tus pasillos Norte/Sur tienen 3 de ancho (el camino), así que las paredes están en +/- 2 del centro
            # Tus pasillos Este/Oeste tienen 1 de alto (el camino), así que las paredes están en +/- 1 del centro
            lx = cx - 2  # Pared Izquierda (Left X)
            rx = cx + 2  # Pared Derecha (Right X)
            ty = cy - 1  # Pared Superior (Top Y)
            by = cy + 1  # Pared Inferior (Bottom Y)

            # ---------------------------------------------------------
            # PASO 1: DIBUJAR EL SUELO (.)
            # ---------------------------------------------------------

            # Centro: Siempre es suelo para conectarlo
            self.grid[cy][cx] = "."

            # Pasillo OESTE y ESTE (Fila central)
            if west:
                for x in range(0, cx): self.grid[cy][x] = "."
            if east:
                for x in range(cx + 1, self.width): self.grid[cy][x] = "."

            # Pasillo NORTE y SUR (Columnas centrales, ancho 3)
            # Range es cx-1, cx, cx+1
            if north:
                for y in range(0, cy + 1):
                    for x in range(cx - 1, cx + 2): self.grid[y][x] = "."
            if south:
                for y in range(cy, self.height):
                    for x in range(cx - 1, cx + 2): self.grid[y][x] = "."

            # Unir cruces: Si hay pasillos laterales, abrimos el centro exacto para que conecten bien
            if west or east:
                self.grid[cy][cx - 1] = "."
                self.grid[cy][cx + 1] = "."

            # ---------------------------------------------------------
            # PASO 2: DIBUJAR LAS PAREDES RECTAS (Sin tocar las esquinas todavía)
            # ---------------------------------------------------------

            # Paredes Verticales (Norte y Sur)
            # Van desde el borde hasta JUSTO ANTES de la intersección (ty o by)
            if north:
                for y in range(0, ty):
                    self.grid[y][lx] = "y"
                    self.grid[y][rx] = "y"

            if south:
                for y in range(by + 1, self.height):
                    self.grid[y][lx] = "y"
                    self.grid[y][rx] = "y"

            # Paredes Horizontales (Este y Oeste)
            # Van desde el borde hasta JUSTO ANTES de la intersección (lx o rx)
            if west:
                for x in range(0, lx):
                    self.grid[ty][x] = "x"
                    self.grid[by][x] = "x"

            if east:
                for x in range(rx + 1, self.width):
                    self.grid[ty][x] = "x"
                    self.grid[by][x] = "x"

            # ---------------------------------------------------------
            # PASO 3: RESOLVER LAS 4 ESQUINAS DE INTERSECCIÓN (La Lógica Maestra)
            # ---------------------------------------------------------
            # Aquí es donde arreglamos el problema visual. Decidimos la pieza exacta
            # según si el muro debe doblar o seguir recto.

            # --- ESQUINA SUPERIOR IZQUIERDA (Top-Left) ---
            # Coordenada: (ty, lx)
            if north and west:
                # Abierto arriba y a la izquierda -> Esquina interior (muro opuesto al pasillo)
                # Necesita conectar ARRIBA e IZQUIERDA: "m" (╝)
                self.grid[ty][lx] = "m"
            elif north:
                self.grid[ty][lx] = "y"  # Solo norte -> Muro vertical recto
            elif west:
                self.grid[ty][lx] = "x"  # Solo oeste -> Muro horizontal recto
            else:
                self.grid[ty][lx] = "q"  # Cerrado -> Esquina de caja (╔)

            # --- ESQUINA SUPERIOR DERECHA (Top-Right) ---
            # Coordenada: (ty, rx)
            if north and east:
                # Abierto arriba y derecha -> Conecta ARRIBA y DERECHA: "z" (╚)
                self.grid[ty][rx] = "z"
            elif north:
                self.grid[ty][rx] = "y"
            elif east:
                self.grid[ty][rx] = "x"
            else:
                self.grid[ty][rx] = "p"  # Cerrado -> Esquina de caja (╗)

            # --- ESQUINA INFERIOR IZQUIERDA (Bottom-Left) ---
            # Coordenada: (by, lx)
            if south and west:
                # Abierto abajo y izquierda -> Conecta ABAJO e IZQUIERDA: "p" (╗)
                self.grid[by][lx] = "p"
            elif south:
                self.grid[by][lx] = "y"
            elif west:
                self.grid[by][lx] = "x"
            else:
                self.grid[by][lx] = "z"  # Cerrado -> Esquina de caja (╚)

            # --- ESQUINA INFERIOR DERECHA (Bottom-Right) ---
            # Coordenada: (by, rx)
            if south and east:
                # Abierto abajo y derecha -> Conecta ABAJO y DERECHA: "q" (╔)
                self.grid[by][rx] = "q"
            elif south:
                self.grid[by][rx] = "y"
            elif east:
                self.grid[by][rx] = "x"
            else:
                self.grid[by][rx] = "m"  # Cerrado -> Esquina de caja (╝)

            # ---------------------------------------------------------
            # PASO 4: CERRAR "TAPAS" (Dead Ends)
            # ---------------------------------------------------------
            # Si un camino no existe, rellenamos el hueco entre las esquinas que acabamos de crear.

            if not north:  # Cerrar pared de arriba
                for x in range(lx + 1, rx): self.grid[ty][x] = "x"

            if not south:  # Cerrar pared de abajo
                for x in range(lx + 1, rx): self.grid[by][x] = "x"

            if not west:  # Cerrar pared izquierda (verticalmente estrecha, solo 1 char)
                # El pasillo horizontal es de altura 1, así que solo rellenamos el hueco cy
                for y in range(ty + 1, by): self.grid[y][lx] = "y"

            if not east:  # Cerrar pared derecha
                for y in range(ty + 1, by): self.grid[y][rx] = "y"

            self.grid[cy][cx] = "P"

        return self.grid
# Dungeon Console Python

> Una aventura clásica de exploración de mazmorras (Dungeon Crawler) ejecutada directamente en tu terminal.

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/status-beta-orange7o?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Descripción

**Dungeon Console Python** es un juego de rol basado en texto (RPG) desarrollado íntegramente en Python. El proyecto busca recrear la esencia de los juegos de aventuras clásicos, donde el jugador debe navegar a través de mazmorras, enfrentarse a enemigos y gestionar sus recursos, todo ello a través de una interfaz de consola limpia y eficiente.

Este proyecto demuestra el uso de programación orientada a objetos (POO), lógica de juegos y gestión de estados en Python sin la necesidad de librerías gráficas externas.

## Características Principales

* **Exploración de Mazmorras:** Navegación por diferentes niveles o habitaciones generadas de forma [procedural](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm).
* **Sistema de Combate:** Encuentros por turnos contra diversos tipos de enemigos.
* **Interfaz de Texto:** Diseño retro basado en ASCII/Texto para una experiencia nostálgica.

## Requisitos Previos


Para ejecutar este proyecto, necesitas estar en LINUX, tener instalado **Python 3.6** o superior en tu sistema.

Puedes verificar tu versión de Python con:

# Controles

El juego se maneja mediante el teclado.

|  Tecla / Comando   | Acción                                                    |
|:------------------:|:----------------------------------------------------------|
|     `1` - `4`      | **Seleccionar opciones** en menús (Atacar, Huir, Objeto). |
| `w`, `a`, `s`, `d` | **Movimiento** por el mapa (Norte, Oeste, Sur, Este).     |
|        `i`         | Abrir el **Inventario**.                                  |
|        `f`         | Entrar en **Combate** (si está disponible).               |
|        `q`         | **Salir** del juego.                                      |

## Estructura del Proyecto

El código está organizado de manera modular para separar la lógica del juego, las entidades y la interfaz.

```text
Dungeon_Console_Python/
├── 📁 config/                   # Archivos de configuración y Assets
│   ├── 🐍 fight_resources.py    # Animaciones y todo lo necesario para los combates
│   └── 🐍 settings.py           # Assets para diferentes aspectos del juego y variables globales
│ 
├── 📁 src/                      # Código fuente principal
│   ├── 🐍 attacks.py            # Lógica de ataques de enemigos y armas
│   ├── 🐍 axe.py                # Clase del arma del jugador
│   ├── 🐍 chest.py              # Clase de para los cofres (/TODO)
│   ├── 🐍 dungeon.py            # Archivo principal que gestiona el juego
│   ├── 🐍 dungeonGenerator.py   # Archivo que genera la distibución del mapa del juego
│   ├── 🐍 healthPotions.py      # Clase de las pociones de vida
│   ├── 🐍 Hero.py               # Clase para el personaje del jugador 
│   ├── 🐍 map.py                # Clas encargada de enseñar el mapa y gestionar esos recursos
│   ├── 🐍 monster.py            # Clase para los monstruos(no es un interfaz)
│   ├── 🐍 room.py               # Clase que gestiona lo relacionado con las habitaciones salvo su grid
│   ├── 🐍 roomGenerator.py      # Clase genera la grid para la room.py ya sean pasillos o habitaciones
│   ├── 🐍 shield.py             # Clase del escudo del jugador
│   ├── 🐍 tamaniosPociones.py   # Clase ENUM para las diferentes dimensiones de las pociones (/TODO solo hay TINY ing)
│   └── 🐍 weaponInterface.py    # Interfaz para el funcionamiento de las armas (escudo y hacha)
│ 
├── 🐍 main.py                   # Punto de entrada (Ejecutar este archivo)
│ 
└── 📄 README.md                 # Documentación
```

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Eres libre de usar, copiar y modificar el código para uso personal o educativo. Sin embargo, este repositorio no admite contribuciones externas. Para más detalles, consulta el archivo [LICENSE](LICENSE).
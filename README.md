# Dungeon Console Python

[Castellano](./README.es.md) | **English**
> A classic dungeon crawler adventure executed directly in your terminal.

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/status-beta-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## Description

**Dungeon Console Python** is a text-based role-playing game (RPG) developed entirely in Python. The project aims to recreate the essence of classic adventure games where the player must navigate through dungeons, face enemies, and manage resources—all through a clean and efficient console interface.

This project demonstrates the use of Object-Oriented Programming (OOP), game logic, and state management in Python without the need for external graphical libraries.

## Key Features

* **Dungeon Exploration:** Navigation through different levels or rooms generated [procedurally](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm).
* **Combat System:** Turn-based encounters against various types of enemies.
* **Inventory System:** Access to an inventory of items found throughout the journey.
* **Text Interface:** Retro ASCII/Text-based design for a nostalgic experience.

## Prerequisites

To run this project on **LINUX**, you must have **Python 3.6** or higher installed on your system. Download the file from the last [release](https://github.com/dmartinr0510/Dungeon_Console_Python/releases) and grant execution permissions using:

```bash
chmod +x DungeonsGame
```
To run this project on **WINDOWS**, simply download the`.exe` file from the latest  [release](https://github.com/dmartinr0510/Dungeon_Console_Python/releases).
# Controls

The game is controlled via the keyboard.

|   Key / Command    | Action                                                           |
|:------------------:|:-----------------------------------------------------------------|
| `w`, `a`, `s`, `d` | **Movement** through the map (North, West, South, East).         |
|        `i`         | Open the **Inventory**.                                          |
|      `↑`,`↓`       | **Navigate** through inventory items.                            |
|        `f`         | Enter **Combat** (if available).                                 |
|     `1` - `4`      | **Select options** in combat menus (Attack, Defend, Heal, Flee). |
|        `l`         | **Loot** inside a chest                                          |
|        `q`         | **Exit** the game.                                               |

# Legend

The game features ASCII art; different elements are represented by specific characters.

| Character | Meaning          |
|:---------:|:-----------------|
|    `@`    | Hero             |
|    `£`    | Monster (Alive)  |
|    `☠`    | Monster (Dead)   |
|    `⚔`    | Combat Symbol    |
|    `§`    | Inventory Symbol |
|    `#`    | Chest Symbol     |

## Project Structure

The code is organized modularly to separate game logic, entities, and the interface.

```text
Dungeon_Console_Python/
├── 📁 config/                   # Configuration files and Assets
│   ├── 🐍 fight_resources.py    # Animations and everything needed for combat
│   └── 🐍 settings.py           # Assets for different game aspects and global variables
│ 
├── 📁 src/                      # Main source code
│   ├── 📁 utils/                # OS helpers
│   │    └── 🐍 compat.py        # System things
│   │
│   ├── 🐍 attacks.py            # Attack logic for enemies and weapons
│   ├── 🐍 axe.py                # Player's weapon class
│   ├── 🐍 chest.py              # Chest class 
│   ├── 🐍 dungeon.py            # Main file that manages the game
│   ├── 🐍 dungeonGenerator.py   # File that generates the game map layout
│   ├── 🐍 Hero.py               # Player character class
│   ├── 🐍 inventory.py          # Player inventory class
│   ├── 🐍 inventoryRender.py    # Class to render the inventory visual section
│   ├── 🐍 item.py               # Interface for items 
│   ├── 🐍 itemsRender.py        # Class to render item visuals and options 
│   ├── 🐍 map.py                # Class responsible for displaying the map and managing resources
│   ├── 🐍 monster.py            # Monster class (not an interface)
│   ├── 🐍 room.py               # Class managing room-related logic (excluding grid)
│   ├── 🐍 roomGenerator.py      # Class that generates the grid for room.py (hallways or rooms)
│   ├── 🐍 shield.py             # Player's shield class
│   ├── 🐍 tamaniosPociones.py   # ENUM class for different potion dimensions (/TODO only TINY exists)
│   ├── 🐍 variousItems.py       # Diferent classes of Items
│   └── 🐍 weaponInterface.py    # Interface for weapon functionality (shield and axe)
│ 
├── 🐍 main.py                   # Entry point (Run this file)
├── 📄 ideas.txt                 # Ideas to add to the game
│ 
└── 📄 README.md                 # Documentation
```

## License

This project is distributed under the **MIT** license.

You are free to use, copy, and modify the code for personal or educational use. However, this repository does not accept external contributions.

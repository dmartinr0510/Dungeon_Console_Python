# 🏰 Dungeon Console Python

> Una aventura clásica de exploración de mazmorras (Dungeon Crawler) ejecutada directamente en tu terminal.

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/status-completed-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

## 📖 Descripción

**Dungeon Console Python** es un juego de rol basado en texto (RPG) desarrollado íntegramente en Python. El proyecto busca recrear la esencia de los juegos de aventuras clásicos, donde el jugador debe navegar a través de mazmorras, enfrentarse a enemigos y gestionar sus recursos, todo ello a través de una interfaz de consola limpia y eficiente.

Este proyecto demuestra el uso de programación orientada a objetos (POO), lógica de juegos y gestión de estados en Python sin la necesidad de librerías gráficas externas.

## ✨ Características Principales

* **Exploración de Mazmorras:** Navegación por diferentes niveles o habitaciones generadas por el sistema.
* **Sistema de Combate:** Encuentros por turnos contra diversos tipos de enemigos.
* **Gestión de Inventario:** Recolección de objetos, pociones y equipamiento.
* **Progresión del Personaje:** Sistema de estadísticas (Vida, Ataque, Defensa).
* **Interfaz de Texto:** Diseño retro basado en ASCII/Texto para una experiencia nostálgica.

## 🛠️ Requisitos Previos

Para ejecutar este proyecto, necesitas tener instalado **Python 3.6** o superior en tu sistema.

Puedes verificar tu versión de Python con:

```bash
python --version
```

# 🎮 Controles

El juego se maneja mediante el teclado numérico y comandos simples. Asegúrate de pulsar `Enter` después de cada elección.

| Tecla / Comando | Acción |
| :---: | :--- |
| `1` - `4` | **Seleccionar opciones** en menús (Atacar, Huir, Objeto). |
| `w`, `a`, `s`, `d` | **Movimiento** por el mapa (Norte, Oeste, Sur, Este). |
| `i` | Abrir el **Inventario**. |
| `m` | Ver el **Mapa** (si está disponible). |
| `q` | **Salir** del juego. |

## 📂 Estructura del Proyecto

El código está organizado de manera modular para separar la lógica del juego, las entidades y la interfaz.

```text
Dungeon_Console_Python/
├── 📁 assets/          # Archivos de guardado o arte ASCII
├── 📁 src/             # Código fuente principal
│   ├── 🐍 items.py     # Lógica de objetos y armas
│   ├── 🐍 player.py    # Clase del Jugador y estadísticas
│   ├── 🐍 enemy.py     # Lógica de enemigos y generación
│   └── 🐍 world.py     # Generación de mazmorras y mapa
├── 🐍 main.py          # Punto de entrada (Ejecutar este archivo)
│ 
└── 📄 README.md        # Documentación
```

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Eres libre de usar, copiar y modificar el código para uso personal o educativo. Sin embargo, este repositorio no admite contribuciones externas. Para más detalles, consulta el archivo [LICENSE](LICENSE).
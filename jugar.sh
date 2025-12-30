#!/bin/bash

# Obtener la ruta del directorio donde está este script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Entrar en la carpeta del proyecto
cd "$DIR"

# Ejecutar el juego con python3
# Usamos 'python3' explícitamente
python3 main.py

import sys
import os
import platform

IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    import msvcrt
else:
    import termios
    import tty
try:
    from colorama import init
    init()
except ImportError:

    pass

def clear_lines(n=1):
    for _ in range(n):
        # Mueve cursor arriba (\033[1A) y limpia línea (\033[2K)
        sys.stdout.write('\033[1A\033[2K')
    sys.stdout.flush()

def clear_screen():
    #Limpia la pantalla según el SO
    os.system("cls" if IS_WINDOWS else "clear")

def get_char():
    #Lee una tecla y normaliza las flechas de Windows a formato Linux
    if IS_WINDOWS:
        ch = msvcrt.getch()
        if ch in [b'\x00', b'\xe0']:
            ch = msvcrt.getch()
            # Mapeamos códigos de Windows a los que ya usa tu código de Linux
            mapping = {b'H': '\x1b[A', b'P': '\x1b[B', b'M': '\x1b[C', b'K': '\x1b[D'}
            return mapping.get(ch, "")
        return ch.decode('utf-8', errors='ignore')
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch += sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
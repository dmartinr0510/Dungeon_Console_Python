from src.dungeon import Dungeon
import sys
sys.stdout.reconfigure(encoding='utf-8')

def start():
    sys.stdout.reconfigure(encoding='utf-8')

    dungeon = Dungeon()
    dungeon.gen_dungeon_rooms()
    dungeon.start_dungeon()


if __name__== "__main__":
    start()


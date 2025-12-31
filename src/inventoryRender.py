import os,sys
from config.settings import BLUE,DEFAULT
from src.utils.compat import clear_screen


class InventoryRender:

    def draw_inventory(self,hero,selected_idx):
        width = 67
        output = []

        output.append("█" * (width + 4))
        output.append(f"█░{"INVENTORY":^{width}}░█")
        output.append(f"█░{"":^{width}}░█")
        potions_text = f"Φ x{len(hero.inventory.potions)}"
        weapon_name = f"  > Weapon: {BLUE}{hero.get_weapon().get_name()}{DEFAULT}"
        health_bar = f"HP: {"■" * (hero.get_health_points() // 10)}{'░' * (10 - (hero.get_health_points()// 10))} ({hero.get_health_points()}/100)"
        output.append(f"█░{weapon_name:<{width+9}}░█")
        output.append(f"█░{"":^{width}}░█")
        output.append(f"█░{health_bar}{potions_text:>{width - len(health_bar) - 2}}  ░█")
        output.append(f"█░{"":^{width}}░█")


        inventory = hero.get_inventory()
        items = inventory.get_items()
        items_names = []
        for item in items:
            items_names.append(item.get_name())

        for i in range(inventory.get_capacity()):
            if i < len(items):
                item_name = items_names[i]
                if i == selected_idx:
                    item_text = f" ► {i + 1}. {item_name}"
                else:
                    item_text = f"   {i + 1}. {item_name}"
            else:
                item_text = f"{i + 1}. ----------"

            output.append(f"█░{item_text:<{width}}░█")

            output.append(f"█░{'':^{width}}░█")
            output.append("█" * (width + 4))

        clear_screen()
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()

        self.draw_controls()
        #print(selected_idx)

    @staticmethod
    def draw_controls():
        width = 71
        print("=" * width)
        print(f"              3) Heal                                     q) exit")
        print("")
        print(f"              ↵) See item                                 i) Close Inventory")
        print("=" * width)
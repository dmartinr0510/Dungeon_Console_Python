import sys

from src.utils.compat import clear_screen


class ItemRender:

    def __init__(self):
        self.item = None


    def show_item_desc(self):
        desc = self.item.get_description()
        return desc


    def show_item_name(self):
        name = self.item.get_name().upper()
        return name

    def show_item_icon(self):
        icon = self.item.get_icon()
        return icon
    @staticmethod
    def show_item_actions():
        width = 71
        print("=" * width)
        print(f"              o) Back to inventory                        q) exit")
        print("")
        print(f"              l) Drop Item                                i) Close inventory")
        print("=" * width)

    def render_item(self, item):
        self.item = item
        width = 67
        output = []

        output.append("█" * (width + 4))
        output.append(f"█░{self.show_item_name():^{width}}░█")
        output.append(f"{self.show_item_icon():^{width}}")
        for i in range(0, 4):
            output.append(f"█░{"":^{width}}░█")
        output.append(f"█░{" DESCRIPTION:":<{width}}░█")
        output.append(f"█░{"":^{width}}░█")
        output.append(f"█░{self.show_item_desc():<{width}}░█")
        output.append(f"█░{'':^{width}}░█")
        output.append("█" * (width + 4))

        clear_screen()
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()
        self.show_item_actions()


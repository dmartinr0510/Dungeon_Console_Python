from src.utils.compat import clear_screen

class ItemRender:

    def __init__(self):
        self.item = None


    def show_item_desc(self):
        desc = self.item.get_description()
        print(desc)


    def show_item_name(self):
        name = self.item.get_name()
        print(f"Item: {name}")

    @staticmethod
    def show_item_actions():
        width = 71
        print("=" * width)
        print(f"              o) Back to inventory                        q) exit")
        print("")
        print(f"              l) Drop Item                                i) Close inventory")
        print("=" * width)

    def render_item(self, item):
        clear_screen()
        self.item = item
        self.show_item_name()
        self.show_item_desc()
        self.show_item_actions()


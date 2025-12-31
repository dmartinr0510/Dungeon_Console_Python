from src.variousItems import  ITEMS,ITEM_DESCRIPTIONS
import random

class Chest:

    def __init__(self):
        self.items = []
        self.created = False

    def create_chest_items(self):
        item_pool = list(ITEM_DESCRIPTIONS.keys())
        selected_names = random.sample(item_pool,2)

        for item_name in selected_names:
            item_desc = ITEM_DESCRIPTIONS.get(item_name)
            build_class = ITEMS.get(item_name)

            if build_class:
                added_item = build_class(item_desc)
                self.items.append(added_item)
        self.created = True

    def show_items(self):

        print("                                    --------- CHEST -----------")


        for item in self.items:
            item.show_item()


        print("                                      l) loot")




    def chest_created(self):
        if self.created:
            return True
        else:
            return False
    def get_items(self):
        return self.items

    def remove_item(self,item):
        self.items.remove(item)
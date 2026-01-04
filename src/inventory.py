


class Inventory:

    def __init__(self):
        self.capacity = 5
        self.potions = []
        self.max_potions = 3
        self.items = []

    def add_item(self, item):
        if self.is_potion(item) and len(self.potions) < self.max_potions:
            self.potions.append(item)
            return True
        elif self.is_potion(item) and len(self.potions) >= self.max_potions:
            print("                                      Max potions reached cant add more")
            return False
        else:
            if len(self.items) < self.capacity:
                self.items.append(item)
                return True
        return False

    def remove_items(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None
    def  get_items(self):
        return self.items
    def get_item(self, index):
        return self.items[index]
    def get_capacity(self):
        return self.capacity
    @staticmethod
    def is_potion(item):
        if item.get_name() == "Heal Potion" :
            return True
        else:
            return False
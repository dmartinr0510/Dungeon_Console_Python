from src.inventoryRender import InventoryRender


class Inventory:

    def __init__(self):
        self.capacity = 5
        self.items = ["Moneda","Espatula", "Calavera"]

    def add_item(self, item):
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
    def get_capacity(self):
        return self.capacity

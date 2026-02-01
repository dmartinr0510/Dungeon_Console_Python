from abc import ABC, abstractmethod

from config.item_resources import ITEMS_ICONS


class Item(ABC):

    @abstractmethod
    def __init__(self, name,description):
        self.name = name
        self.description = description
        if ITEMS_ICONS[self.name] is not None:
            self.icon = ITEMS_ICONS[self.name]
        else:
            self.icon = " "

    def show_item(self):
        print(f"                                      - {self.name}")
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description

    def get_icon(self):
        return self.icon

from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def __init__(self, name,description):
        self.name = name
        self.description = description

    def show_item(self):
        print(f"                                      - {self.name}")
    def get_name(self):
        return self.name
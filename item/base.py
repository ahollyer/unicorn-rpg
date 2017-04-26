import time

class Item:
    def __init__(self, name, cost, desc):
        self.name = name
        self.cost = cost
        self.desc = desc
    def equip (self, hero):
        raise NotImplementedError
    @staticmethod
    def pause():
        time.sleep(0.3)

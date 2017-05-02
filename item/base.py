import time

class Item:
    def __init__(self, name, cost, desc, img):
        self.name = name
        self.cost = cost
        self.desc = desc
        self.img = img
    def equip (self, hero):
        raise NotImplementedError
    @staticmethod
    def pause():
        time.sleep(0.3)

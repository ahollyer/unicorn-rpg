from character.base import Character

class Hero(Character):
    def __init__ (self, name='Becky', health=10, power=5, evade=0, coins=10):
        super().__init__(name, health, power, evade, coins)

    @classmethod
    def create(cls):
        name = input("What's your name, hero?: ")
        return cls(name)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.equip(self)
        else:
            print("You can't afford that, loser!")

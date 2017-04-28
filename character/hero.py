import time

from character.base import Character

class Hero(Character):
    def __init__ (self, name='Becky', health=10, power=5, evade=0, coins=10):
        super().__init__(name, health, power, evade, coins)

    @classmethod
    def create(cls):
        print("""\nPIXIE:
        Welcome to FairyLand! I'm the gumdrop pixie, and I
        brought you here using sprinkle magic. We've been waiting many
        centuries for a magical unicorn princess like you.
        """)
        time.sleep(1.5)
        name = input("What's your name, princess? ").upper()
        return cls(name)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.equip(self)
        else:
            print("You can't afford that, loser!")

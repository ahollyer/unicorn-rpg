from character.base import Character

class Enemy (Character):
    def __init__ (self, name ='Shagrat', health=6, power=2, evade=0, coins=3):
        super().__init__(name, health, power, evade, coins)

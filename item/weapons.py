from item.base import Item

class Sword(Item):
    def equip (self, hero):
        print("{}'s power is {}.".format(
            hero.name, hero.power))
        self.pause()
        print("{} grips the hilt of the {}.".format(hero.name, self.name))
        self.pause()
        print("~~~ * . . ~~.~~ . . * ~~~")
        self.pause()
        hero.power += 2
        print("{}'s power increases to {}!".format(hero.name, hero.power))

from item.base import Item

class Blade(Item):
    def equip (self, hero):
        print("{}'s power is {}.".format(
            hero.name, hero.power))
        self.pause()
        print("{} takes the {}.".format(hero.name, self.name))
        self.pause()

        for i in range(3):
            print("~*- TAPE -*~")
            self.pause()

        hero.power += 2
        print("{}'s power increases to {}!".format(hero.name, hero.power))

from item.base import Item

class Shirt(Item):
    def equip(self, hero):
        print("{}'s health is {} out of {}.".format(
            hero.name, hero.health, hero.max_health))
        self.pause()
        print("{} puts on {}.".format(hero.name, self.name))
        self.pause()

        for i in range(3):
            print("~ * ... * ~")
            self.pause()

        hero.max_health += 2
        hero.health += 2
        print("{}'s health increases to {} out of {}!".format(
            hero.name, hero.health, hero.max_health))

class Boots(Item):
    def equip (self, hero):
        print("{}'s evade is {}.".format(
            hero.name, hero.evade))
        self.pause()
        print("{} puts on {}.".format(hero.name, self.name))
        self.pause()

        for i in range(3):
            print("~ * ... * ~")
            self.pause()

        hero.evade += 2
        print("{}'s evade increases to {}!".format(hero.name, hero.evade))

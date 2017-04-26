from item.base import Item

class Tonic(Item):
    def equip(self, hero):
        print("{}'s health is {} out of {}.".format(
            hero.name, hero.health, hero.max_health))
        self.pause()
        print("{} drinks the {}.".format(
            hero.name, self.name))
        self.pause()
        print("~ * . . . . * ~")
        self.pause()
        hero.health = hero.max_health
        print("{}'s health is now {} out of {}!".format(
            hero.name, hero.health, hero.max_health))

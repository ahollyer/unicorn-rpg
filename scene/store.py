import time

from item.armor import *
from item.tonics import *
from item.weapons import *

class Store:
    shirt = Shirt(
        "A Ragged Tunic", 5,
        "This tunic has seen better days. It will provide some protection.")
    supertonic = Tonic(
        "SuperTonic", 10,
        "This tonic tastes like dirty socks, but it will restore a lot of health!")
    boots = Boots(
        "Sneaky Boots", 10,
        "These boots will make you light on your feet!")
    sword = Sword(
        "Rusty Sword", 8,
        "This dull-as-a-butter-knife blade has seen better days. It might deal more damage than your bare fists, though.")
    items = [shirt, supertonic, boots, sword]
    def shop(self, hero):
        print("=====================")
        print("Welcome to the store!")
        print("=====================")
        while True:
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?\n")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. Buy {} ({} coins) - {}\n".format(i + 1, item.name, item.cost, item.desc))
            print("10. leave")
            choice = int(input("> "))
            if choice == 10:
                break
            else:
                item = Store.items[choice - 1]
                hero.buy(item)
                Store.items.remove(item)
                time.sleep(2)
                print("\n\nThanks for your business.\n")

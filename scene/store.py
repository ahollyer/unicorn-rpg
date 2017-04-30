import random
import time

import image

from item.armor import *
from item.tonics import *
from item.weapons import *

class Store:
    shirt = Shirt(
        "A Ragged Tunic", 5,
        "This tunic has seen better days. It will provide some protection.")
    supercandy = Tonic(
        "SuperCandy", 5,
        "This candy tastes like dirty socks, but it will restore a lot of health!")
    boots = Boots(
        "Sneaky Boots", 10,
        "These boots will make you light on your feet!")
    sword = Sword(
        "Rusty Sword", 8,
        "This dull-as-a-butter-knife blade has seen better days. It might deal more damage than your bare fists, though.")

    items = [shirt, supercandy, boots, sword]

    def go_shopping(self, hero):
        print(image.divider.divs[1])
        print("{} travels onward.".format(hero.name))
        print(image.divider.divs[1])

        # Animate by drawing, erasing, and re-drawing
        print(image.char.unicorn_right[3])
        for i in range(1):
            for img in image.char.unicorn_right:
                time.sleep(0.4)
                print(("\r" + ("\033[A\033[K" * 8)) + img, end="")

        rand = random.randint(0, len(image.char.merchants) - 1)
        print("\nA traveling merchant appears!")
        time.sleep(0.3)
        print(image.char.merchants[rand])
        ans = input("> ")

        print(image.divider.divs[5])
        print("\tWELCOME TO MY SHOPPY SHOP!")
        print(image.divider.divs[5])

        while True:
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?\n")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. Buy {} ({} coins) - {}\n".format(i + 1, item.name, item.cost, item.desc))
            print("10. leave")

            waiting = True
            while waiting:
                try:
                    choice = int(input("> "))
                    waiting = False
                except ValueError:
                    print("""
                    This ain't burger king, {}. You can't have it your way.
                    PICK ONE OF THE OPTIONS I GAVE YOU!
                    """.format(hero.name))

            if choice == 10:
                break
            elif choice > len(Store.items):
                print("""
                This ain't burger king, {}. You can't have it your way.
                PICK ONE OF THE OPTIONS I GAVE YOU!
                """.format(hero.name))
            else:
                item = Store.items[choice - 1]
                hero.buy(item)
                Store.items.remove(item)
                time.sleep(2)
                print("\n\nThanks for your business.\n")

        print(image.divider.divs[1])
        print("{} travels onward.".format(hero.name))
        print(image.divider.divs[1])

        # Animate by drawing, erasing, and re-drawing
        print(image.char.unicorn_right[3])
        for i in range(1):
            for img in image.char.unicorn_right:
                time.sleep(0.4)
                print(("\r" + ("\033[A\033[K" * 8)) + img, end="")

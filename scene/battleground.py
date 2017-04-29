import time

from image import *
from character import *

def do_battle(hero, enemy):
    print("\n\n\n")
    print(divider.divs[0])
    print("{} faces {}".format(hero.name, enemy.name))
    print(divider.divs[0])
    while hero.alive() and enemy.alive():
        hero.print_status()
        enemy.print_status()
        time.sleep(1.5)
        print("\n" + divider.divs[0])
        print("1. Fight {}".format(enemy.name))
        print("2. Do nothing")
        print("3. Flee")
        print("4. Check stats")
        ans = input("> ")
        if ans == '1':
            hero.fight(enemy)
        elif ans == '2':
            pass
        elif ans == '3':
            print("Goodbye.")
            exit(0)
        elif ans == '4':
            hero.print_status(hud=True)
        else:
            print("""
            This ain't Burger King. You can't 'have it your way', {}.
            PICK ONE OF THE OPTIONS I GAVE YOU!!""".format(hero.name))
            continue
        enemy.fight(hero)
    if hero.alive():
        print("{} defeated the {}".format(hero.name, enemy.name))
        return True
    else:
        print("YOU LOSE!")
        return False

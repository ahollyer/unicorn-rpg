import time

from image import *
from character import *

def do_battle(hero, enemy):
    print(divider.divs[0])
    print("Hero faces the {}".format(enemy.name))
    print(divider.divs[0])
    while hero.alive() and enemy.alive():
        hero.print_status()
        enemy.print_status()
        time.sleep(1.5)
        print(divider.divs[0])
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("4. check status")
        print("> ", end=' ')
        keyinput = int(input())
        if keyinput == 1:
            hero.attack(enemy)
        elif keyinput == 2:
            pass
        elif keyinput == 3:
            print("Goodbye.")
            exit(0)
        elif keyinput == 4:
            hero.print_status(hud=True)
        else:
            print("Invalid input {}".format(input))
            continue
        enemy.attack(hero)
    if hero.alive():
        print("You defeated the {}".format(enemy.name))
        return True
    else:
        print("YOU LOSE!")
        return False

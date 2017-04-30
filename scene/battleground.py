import time

from image import *
from character import *

def do_battle(hero, enemy):
    print("\n")
    print("\b" + text.fight)
    print(divider.divs[1])
    print("\t{} vs. {}".format(hero.name, enemy.name))
    print(divider.divs[1])
    time.sleep(0.8)

    while hero.alive() and enemy.alive():
        print("")
        print("*~- STATUS -~*")
        hero.print_status()
        enemy.print_status()
        print("")
        time.sleep(1.5)

        waiting = True
        while waiting:
            print("\n" + divider.divs[0])
            print("~*- OPTIONS -*~")
            print("1. Fight {}".format(enemy.name))
            print("2. Do nothing")
            print("3. Flee")
            print("4. See {}'s traits".format(hero.name))
            ans = input("> ")
            if ans == '1':
                print("\n" + divider.divs[2])
                hero.fight(enemy)
                if enemy.alive():
                    enemy.fight(hero)
                print(divider.divs[2])
                waiting = False
            elif ans == '2':
                print("")
                print(divider.divs[2])
                print("{}: Use me as a punching bag!!".format(hero.name))
                time.sleep(0.5)
                print("{} stands dumbly, waiting to be hit.\n".format(hero.name))
                time.sleep(1)
                enemy.fight(hero)
                print(divider.divs[2])
                time.sleep(0.5)
                waiting = False
            elif ans == '3':
                print("\n{} screams like a little girl.".format(hero.name))
                time.sleep(0.5)
                print("{} gallops away, but the enemy gets a whack at her before she escapes.".format(hero.name))
                enemy.fight(hero)
                waiting = False
            elif ans == '4':
                hero.print_status(hud=True)
            else:
                print("""
                This ain't Burger King. You can't 'have it your way', {}.
                PICK ONE OF THE OPTIONS I GAVE YOU!!""".format(hero.name))
        if ans == '3':
            break
    if hero.alive():
        if ans == '3':
            print("""
            *===========================================================*
             {} lives to fight another day. She gallops onward.
            *===========================================================*
            """.format(hero.name, enemy.name))
        else:
            hero.win_count += 1
            print("""
            *===========================================================*
             {} emerges victorious. She trots away, leaving the corpse
             of {} to rot in the sun.
            *===========================================================*
            """.format(hero.name, enemy.name))
        return True
    else:
        return False

import time

from image import *
from character import *

def do_battle(hero, enemy):
    print("\n")
    print(divider.divs[1])
    print("\t{} faces {}".format(hero.name, enemy.name))
    print(divider.divs[1])
    time.sleep(0.5)

    while hero.alive() and enemy.alive():
        print("")
        print("*~-STATUS-~*")
        hero.print_status()
        enemy.print_status()
        print("")
        time.sleep(1.5)

        waiting = True
        while waiting:
            print("\n" + divider.divs[0])
            print("~*-OPTIONS-*~")
            print("1. Fight {}".format(enemy.name))
            print("2. Do nothing")
            print("3. Flee")
            print("4. See {}'s attributes".format(hero.name))
            ans = input("> ")
            if ans == '1':
                enemy.fight(hero)
                hero.fight(enemy)
                waiting = False
            elif ans == '2':
                print("\n{}: Use me as a punching bag!!".format(hero.name))
                time.sleep(0.5)
                print("{} stands dumbly, waiting to be hit.\n".format(hero.name))
                time.sleep(1)
                enemy.fight(hero)
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
        if ans == '3'
            print("""
            \b{} lives to fight another day, and gallops onward.
            """.format(hero.name, enemy.name))
        else:
            print("""
            \b{} emerges victorious. She trots away, leaving the corpse of
            \b{} to rot in the sun.
            """.format(hero.name, enemy.name))
        return True
    else:
        print("YOU LOSE!")
        return False

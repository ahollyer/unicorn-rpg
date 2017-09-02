import random
import time
from image import *
from character import *

def print_fight_intro(hero, enemy):
    rand = random.randint(0, len(text.fight_msgs) - 1)
    print("\n")
    print(text.fight_msgs[rand])
    print(divider.divs[1])
    print("  {} vs. {}".format(hero.name, enemy.name))
    print(divider.divs[1])
    time.sleep(0.8)

def print_battle_options(hero, enemy):
    print("\n" + divider.divs[0])
    # print("~*~ OPTIONS ~*~")
    print("1. Fight {}".format(enemy.name))
    print("2. Do nothing")
    print("3. Flee")
    print("4. See {}'s traits".format(hero.name))

def print_status(hero, enemy):
    print("")
    print("*****************************\n\tSTATUS\n*****************************")
    hero.print_status()
    enemy.print_status()
    print("")
    time.sleep(1.5)

def print_victory_msg(hero, enemy, ans):
    if ans == '3':
        print("""
        *===========================================================*
         {} lives to fight another day. She gallops onward.
        *===========================================================*
        """.format(hero.name, enemy.name))
        input("> ")
    else:
        hero.win_count += 1
        print("""
        *===========================================================*
         {} emerges victorious. She trots away, leaving the corpse
         of {} to rot in the sun.
        *===========================================================*
        """.format(hero.name, enemy.name))
        input("> ")

def fight(hero, enemy):
    print("\n" + divider.divs[2])
    hero.fight(enemy)
    if enemy.alive():
        enemy.fight(hero)
    print(divider.divs[2])

def do_nothing(hero, enemy):
    print("")
    print(divider.divs[2])
    print("{}: Use me as a punching bag!!".format(hero.name))
    time.sleep(0.5)
    print("{} stands dumbly, waiting to be hit.\n".format(hero.name))
    time.sleep(1)
    enemy.fight(hero)
    print(divider.divs[2])
    time.sleep(0.5)

def flee(hero, enemy):
    print("\n{} screams like a little girl.".format(hero.name))
    time.sleep(0.5)
    print("{} gallops away, but the enemy gets a whack at her before she escapes.".format(hero.name))
    enemy.fight(hero)

def do_battle(hero, enemy):
    print_fight_intro(hero, enemy)

    while hero.alive() and enemy.alive():
        waiting = True
        print_status(hero, enemy)

        while waiting:
            print_battle_options(hero, enemy)
            ans = input("> ")
            if ans == '1':
                fight(hero, enemy)
                waiting = False
            elif ans == '2':
                do_nothing(hero, enemy)
                waiting = False
            elif ans == '3':
                flee(hero, enemy)
                waiting = False
            elif ans == '4':
                hero.print_status(hud=True)
            else:
                print("""
                This ain't Burger King. You can't 'have it your way', {}.
                PICK ONE OF THE OPTIONS I GAVE YOU!!""".format(hero.name))
        # If user selects 'flee', leave the battle
        if ans == '3':
            break

    if hero.alive():
        print_victory_msg(hero, enemy, ans)
        return True
    else:
        return False

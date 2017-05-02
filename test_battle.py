#!/usr/bin/env python3

import random
import time

import image

from scene import *
from character.hero import *
from character.enemies import *

def print_title():
    for word in image.text.title:
        print(word)
        time.sleep(1)
    time.sleep(2)
    print('\n\n\n', image.text.subtitle)
    time.sleep(1)
    for i in range(40):
        print('')
        time.sleep(0.2)

if __name__ == "__main__":

    # Initialize Game
    #print_title()

    hero = Hero("BECKY")
    enemies = [
        Enemy("An Angry Triceratops", 6, 2, "maul", 0, 5),
        Enemy("A Hungry Velociraptor", 6, 4, "swipe", 2, 5),
        Enemy("A Vicious T-Rex", 10, 5, "bite", 0, 8),
        Enemy("Boss: Fairy Satan", 15, 5, "stab", 2, 10)
    ]
    shopping_engine = store.Store()

    # Level 1
    battle_counter = 0
    for enemy in enemies:
        print(image.char.enemies[battle_counter])
        battle_counter += 1
        input("> ")
        hero_won = battleground.do_battle(hero, enemy)
        if not hero_won:
            print("Rainbow blood pools around {}'s lifeless body".format(hero.name))
            print("FAIRIES FOREVER!! YOU LOSE!")
            exit(0)
        shopping_engine.go_shopping(hero)

    print("THAT'S ALL FOR NOW!")
    print("BYE!")

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
    print_title()

    hero = Hero.create()
    enemies = [Enemy("A Vicious T-Rex"), Enemy("JimBob", 5, 5)]
    shopping_engine = store.Store()

    # Intro Scene
    choice = bridge.play_scene(hero)
    if choice == 1:
        forest.play_scene(hero)
    elif choice == 2:
        mountains.play_scene(hero)

    # Level 1
    for enemy in enemies:
        hero_won = battleground.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.shop(hero)

    print("YOU WIN!")

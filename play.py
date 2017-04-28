#!/usr/bin/env python3

import random
import time
import scene.battleground
import scene.bridge
import scene.store

import image

from character.hero import *
from character.enemies import *

def print_title():
    for word in image.text.title:
        print(word)
        time.sleep(1)
    time.sleep(1)
    print(image.text.subtitle)
    time.sleep(1)

if __name__ == "__main__":

    # Initialize Game
    print_title()

    hero = Hero.create()
    enemies = [Enemy(), Enemy("JimBob", 5, 5)]
    shopping_engine = scene.store.Store()

    # Intro Scene
    scene.bridge.play_scene(hero)

    # Level 1
    for enemy in enemies:
        hero_won = battleground.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.shop(hero)

    print("YOU WIN!")

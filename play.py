#!/usr/bin/env python3

import random
import time

from image import *
from scene import *

from character.hero import *
from character.enemies import *

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

if __name__ == "__main__":
    for word in text.title:
        print(word)
        time.sleep(1)
    time.sleep(1)
    print(text.subtitle)
    time.sleep(1)

    hero = Hero()
    enemies = [Enemy(), Enemy("JimBob", 5, 5)]
    battle_engine = battleground.Battle()
    shopping_engine = store.Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.shop(hero)

    print("YOU WIN!")

import random
import time

import image

class Character:
    def __init__(self, name, health, power, attack, evade, coins):
        self.name = name
        self.max_health = health
        self.health = health
        self.power = power
        self.attack = attack
        self.evade = evade
        self.coins = coins

    def fight(self, target):
        crit_dice = random.random()
        if crit_dice > 0.6:
            crit = self.power * 2
            print("** CRITICAL HIT:")
            target.health -= crit
            print("{} {}s {} for {} damage.".format(
            self.name, self.attack, target.name, crit))
        else:
            target.health -= self.power
            print("{} {}s {} for {} damage.".format(
            self.name, self.attack, target.name, self.power))
        if target.health <= 0:
            print("{} is dead.".format(target.name))
            time.sleep(1)
            print("""
   .--.
  ( ${} ) {} loots the corpse and retrieves {} coins.
   '--'
            """.format(target.coins, self.name, target.coins))
            self.coins += target.coins

    def alive(self):
        return self.health > 0

    def print_status(self, hud=False):
        if hud:
            print(image.char.unicorn)
            print("""
            >>>>>-----------*-----------<<<<<
                    *~-~* Traits *~-~*
            >>>>>-----------*-----------<<<<<
              * HEALTH: {} out of {}
              * POWER: {}
              * EVADE: {}
              * WALLET: {} coins
              * KILLS: {} foes slain
            >>>>>-----------*-----------<<<<<
            """.format(
                self.health, self.max_health, self.power,
                self.evade, self.coins, self.win_count))
        else:
            print("{} has {} health and {} power.".format(
                self.name, self.health, self.power))

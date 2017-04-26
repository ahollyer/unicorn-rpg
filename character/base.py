import time
import random

class Character:
    def __init__(self, name, health, power, coins):
        self.name = name
        self.max_health = health
        self.health = health
        self.power = power
        self.coins = coins

    def attack(self, target):
        crit_dice = random.random()
        if crit_dice > 0.6:
            print("Critical hit!")
            target.health -= self.power * 2
        else:
            target.health -= self.power
        print("{} does {} damage to {}.".format(
            self.name, self.power, target.name))
        if target.health <= 0:
            print("{} is dead.".format(target.name))
            time.sleep(1)
            print("\n{} loots the corpse and retrieves {} coins".format(
                self.name, target.coins))
            self.coins += target.coins

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

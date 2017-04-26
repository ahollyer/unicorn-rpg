import time

class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
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

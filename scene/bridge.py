import time

import image
import scene.battleground

def pause():
    time.sleep(2)

def play_scene(hero):
    print("""\n\nPIXIE:
    \t{}, we need your help.""".format(hero.name))
    pause()
    print("\n\tYou see, it's kind of a long story.")
    pause()
    print("\n\tBasically, there's this bad guy who needs defeating.")
    pause()
    print("\n\t. . .")
    time.sleep(2.5)
    print("\n\tWell, I'm sure you'll figure it out. Bye!")
    pause()
    pause()

    print(image.char.pixie)
    for c in image.thing.poof:
        time.sleep(0.5)
        print(("\r" + ("\033[A\033[K" * 6)) + c, end="")

    print("\033[A\033[K" * 5)

    print("\nThe gumdrop pixie vanishes in a puff of glitter.")
    pause()
    print("\n{} looks around.".format(hero.name))
    pause()
    print("\n\n\nOff to the east lies an ominous-looking lollipop forest,")
    pause()
    print(image.thing.lollipop_forest)
    pause()
    pause()
    print("\n\nand to the west, a range of steep, treacherous candy mountains")
    print("with summits covered in ice cream.")
    pause()
    pause()
    print(image.thing.ice_cream_mountains)
    pause()
    pause()

    waiting = True
    while waiting:
        print("\n1. Go east\n2. Go west\n")
        ans = input('> ')
        if ans == '1':
            waiting = False
            return 1
        elif ans == '2':
            waiting = False
            return 2
        else:
            print("""
            This ain't Burger King. You can't 'have it your way', {}.
            PICK ONE OF THE OPTIONS I GAVE YOU!!""".format(hero.name))

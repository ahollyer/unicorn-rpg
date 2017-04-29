import time

import image

def pause():
    time.sleep(1.5)

def play_scene(hero):
    print("""\n\nPIXIE:
    \t{}, we need your help.""".format(hero.name))
    pause()
    print("\n\tYou see, it's kind of a long story.")
    input('> ')
    print("\n\tBasically, there's this bad guy who needs defeating.")
    input('> ')
    print("\n")
    for i in range(6):
        time.sleep(0.3)
        print("\r\t" + ". " * i, end="")
        time.sleep(0.3)
    print("\n\n\tWell, I'm sure you'll figure it out. Bye!")
    pause()

    print(image.char.pixie)
    time.sleep(1)
    for c in image.thing.poof:
        time.sleep(0.4)
        print(("\r" + ("\033[A\033[K" * 6)) + c, end="")

    print("\033[A\033[K" * 5)

    print("\nThe gumdrop pixie vanishes in a puff of glitter.")
    input('> ')
    print("\n{} looks around.".format(hero.name))
    input('> ')
    print("\n\n\nOff to the east lies an ominous-looking lollipop forest,")
    input('> ')
    print(image.thing.lollipop_forest)
    input('> ')
    print("\n\nand to the west, a range of steep, treacherous candy mountains")
    print("with summits covered in ice cream.")
    input('> ')
    print(image.thing.ice_cream_mountains)
    input('> ')

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

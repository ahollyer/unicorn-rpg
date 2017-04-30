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
    time.sleep(0.7)
    for c in image.thing.poof:
        time.sleep(0.3)
        print(("\r" + ("\033[A\033[K" * 6)) + c, end="")

    print("\033[A\033[K" * 5)

    print("The gumdrop pixie vanishes in a puff of glitter.")
    input('> ')
    print("{} looks around.".format(hero.name))
    input('> ')
    print("To the right lies an ominous-looking lollipop forest,")
    print(image.thing.lollipop_forest)
    input('> ')
    print("and to the left, a range of steep, treacherous candy mountains")
    print("with summits covered in ice cream.")
    print(image.thing.ice_cream_mountains)
    input('> ')

    waiting = True
    while waiting:
        print("\n1. Go right\n2. Go left\n")
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

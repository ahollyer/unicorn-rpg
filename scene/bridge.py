import scene.battleground
import time

def pause():
    time.sleep(2)

def play_scene(hero):
    print("""PIXIE:
    {}, we need your help.""".format(hero.name))
    pause()
    print("\n\tYou see, it's kind of a long story.")
    pause()
    print("\n\tBasically, there's this bad guy who needs defeating.")
    pause()
    print("\n\t.")
    pause()
    print("\n\t. .")
    pause()
    print("\n\t. . .")
    pause()
    pause()
    print("\n\tWell, I'm sure you'll figure it out. Bye!")
    pause()
    pause()
    pause()

    print("\nThe gumdrop pixie vanishes in a puff of glitter.")
    pause()
    print("\n{} looks around.".format(hero.name))
    pause()
    pause()
    print("\nOff to the east lies an ominous-looking lollipop forest,")
    print("and to the west, a range of steep, treacherous candy mountains")
    print("with summits covered in ice cream.")
    pause()

    waiting = True
    while waiting:
        ans = input("\n1. Go east\n2. Go west\n")

        if ans == '1':
            waiting = False
        elif ans == '2':
            waiting = False
        else:
            print('That is not a valid choice. Try again.')

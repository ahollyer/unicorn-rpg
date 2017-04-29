import time

import image

def pause():
    time.sleep(2)

def play_scene(hero):
    print(image.divider.divs[1])
    print("\t{} heads east.".format(hero.name))
    print(image.divider.divs[1])

    print(image.char.unicorn_right[3])
    for i in range(3):
        for img in image.char.unicorn_right:
            time.sleep(0.4)
            print(("\r" + ("\033[A\033[K" * 8)) + img, end="")

    print("\n\nAn enemy appears!")
    print(image.char.t_rex)
    pause()
    print("\nOh no! A dinosaur! Who knew FairyLand could be so dangerous?")
    input("> ")
    print("Luckily, {}'s blood-spattered horn proves she is no stranger to violence.".format(hero.name))
    input("> ")
    print("{} rears up and lets out a fearsome battle-neigh.".format(hero.name))
    pause()

    print("\n\n\n\n", image.char.unicorn_left[0])
    for i in range(2):
        for img in image.char.unicorn_left:
            time.sleep(0.3)
            print(("\r" + ("\033[A\033[K" * 9)) + img, end="")

    input("> ")

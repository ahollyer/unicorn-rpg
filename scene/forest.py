import time

import image

def pause():
    time.sleep(2)

def play_scene(hero):
    print("{} heads east.\n".format(hero.name))

    for i in range(6):
        #print(image.char.unicorn_right[0])
        for img in image.char.unicorn_right:
            time.sleep(0.4)
            print(("\r" + ("\033[A\033[K" * 8)) + img, end="")

    print("\n\nAn enemy appears!")
    print(image.char.t_rex)
    pause()
    print("\nOh no! A dinosaur! Who knew FairyLand could be so dangerous?")
    pause()
    print("""Luckily, {}'s blood-spattered horn proves she is no stranger
    to battle.""".format(hero.name))
    pause()
    print(image.char.unicorn_left[1])

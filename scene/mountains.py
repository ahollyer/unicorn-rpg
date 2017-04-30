import time

import image

def pause():
    time.sleep(1.5)

def play_scene(hero):
    print(image.divider.divs[1])
    print("{} heads toward the Candy Mountains.".format(hero.name))
    print(image.divider.divs[1])

    # Animate by drawing, erasing, and re-drawing
    print(image.char.unicorn_right[3])
    for i in range(3):
        for img in image.char.unicorn_right:
            time.sleep(0.4)
            print(("\r" + ("\033[A\033[K" * 8)) + img, end="")

    print("\n\nOh no, a dinosaur! Who knew FairyLand could be so dangerous?")
    input("> ")
    print("Luckily, {}'s blood-spattered horn proves she is no stranger to violence.".format(hero.name))
    input("> ")
    print("{} rears up and lets out a fearsome battle-neigh.".format(hero.name))
    pause()

    # Animate by drawing, erasing, and re-drawing
    print("\n\n\n\n\n\n", image.char.unicorn_left[0])
    for i in range(2):
        for img in image.char.unicorn_left:
            time.sleep(0.3)
            print(("\r" + ("\033[A\033[K" * 9)) + img, end="")

    input("\b\b\b\b> ")

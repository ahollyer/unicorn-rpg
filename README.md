# Unicorns vs. Fairies: The Reckoning

## A text-based RPG. Run it in your terminal to experience all its unicorn glory.

--------------------------------------------------------------------------------

## About

It's a game! Level one is complete(ish).

For me, this project is an ongoing lesson in the fundamentals of programming. It's also an absurd text-based RPG full of ridiculous ASCII art.

--------------------------------------------------------------------------------

## How to Play

1. Clone/download the repository.
2. Open your terminal and ```$ cd``` into the 'unicorn-rpg' directory
3. ```$ python3 play.py``` to start the game.

--

## Challenges

This is my first attempt at Object-Oriented Programming and also my first attempt at building a large program in Python. It's been a great learning experience, but of course it is still far from complete.

- **Learning to organize code in separate files**

  - Throughout writing the game, I struggled to understand when to split code into its own function, much less its own class or module.
  - After refactoring several times, the code is becoming much more organized and readable, with separate directories for ASCII art assets, character modules, item modules, and scene modules.
  - I'm still learning OOP basics. It's getting clearer though!

- **DRY, DRY, DRY**

  - As I learned how to split code into modules, I realized I was either importing my modules into each other all the time, or rewriting simple functions. At this point, it became clear that I was doing something wrong. I've learned a couple of strategies to help:

    - If you need a variable from another module for your function to work, pass it as an argument.
    - If you find yourself needing the same function over and over across modules, put it into its own module so you can call it easily and only have to edit it in one place.

--------------------------------------------------------------------------------

## Future Plans

- [x] Add evade ability
- [ ] Create a bank of items
- [ ] Switch out items randomly in the store
- [ ] Add Level 2
- [ ] Add inventory/ability to use items in battle
- [ ] Randomize merchant appearance
- [ ] Create a bank of enemies
- [ ] Choose or generate random enemies based on current level

--------------------------------------------------------------------------------

If you have advice or want to learn together, feel free to reach out! I'm always interested in talking to new people.

Take Care,

Aspen aspen.hollyer@gmail.com

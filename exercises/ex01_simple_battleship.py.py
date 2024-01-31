"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730392828"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
results: str = ""

boat_loc: int = int(input("Pick a secret boat location between 1 and 4: "))
if boat_loc > 4:
    print("Error!" + str(boat_loc) + "too high!")
    exit()
if boat_loc < 1:
    print("Error!" + str(boat_loc) + "too low!")
    exit()
guess_2: int = int(input("Guess a number between 1 and 4: "))
if guess_2 > 4:
    print("Error!" + str(guess_2) + "too high! ")
    exit()
if guess_2 < 1:
    print("Error!" + str(guess_2) + "too low! ")
    exit()
if guess_2 == boat_loc:
    results = RED_BOX
    if guess_2 == 1:
        print(results + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    if guess_2 == 2:
        print(BLUE_BOX + results + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship. ")
    if guess_2 == 3:
        print(BLUE_BOX + BLUE_BOX + results + BLUE_BOX)
        print("Correct! You hit the ship. ")
    if guess_2 == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + results)
        print("Correct! You hit the ship. ")
else: 
    results = WHITE_BOX
    if guess_2 == 1:
        print(results + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship. ")
    if guess_2 == 2:
        print(BLUE_BOX + results + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship. ")
    if guess_2 == 3:
        print(BLUE_BOX + BLUE_BOX + results + BLUE_BOX)
        print("Incorrect! You missed the ship. ")
    if guess_2 == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + results)
        print("Incorrect! You missed the ship. ")
"""3rd Creation of Battleship."""

__author__ = "730392828"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size_grid: int, guess_type: str) -> int:
    """Defining input_guess."""
    assert guess_type == "row" or guess_type == "column"

    correct: bool = False
    par_guess: int = int(input(f"Guess a {guess_type}: "))
    while not correct:
        if par_guess >= 1 and par_guess <= size_grid:
            correct = True
        else: 
            print(input(f"The grid is only {size_grid} by {size_grid}. Try again: "))
    return par_guess


def print_grid(size_grid: int, row_guess: int, col_guess: int, par_guess2: bool) -> None:
    """Defining print_grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    # creating red and white box for miss or hit
    if par_guess2:
        result = RED_BOX
    else:
        result = WHITE_BOX

# creating counter for rows/creating a grid
    row_counter = 1
    while row_counter <= size_grid:
        # creating emoji counter
        emoji_row = ""
        column_counter = 1
        while column_counter <= size_grid:
            if row_guess == row_counter and col_guess == column_counter:
                emoji_row += result
            else: 
                emoji_row += BLUE_BOX
            column_counter += 1
        print(emoji_row)
        row_counter += 1


def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Defining the participant's correct guess."""
    if row_guess == secret_row and col_guess == secret_col:
        return True
    else:
        return False


def main(size_grid: int, secret_row: int, secret_col: int) -> None:
    """Defining main function to run game altogether."""
    attempts = 1
    gvictory = False
    while attempts <= 5 and gvictory is False:
        print(f"=== Turn {attempts}/5 ===")
        row_guess = input_guess(size_grid, "row")
        col_guess = input_guess(size_grid, "column")
        gvictory = correct_guess(secret_row, secret_col, row_guess, col_guess)
        print_grid(size_grid, row_guess, col_guess, gvictory)
        if gvictory is True:
            print("Hit!")
            print(f"You won in {attempts}/5 turns!")
        else: 
            print("Miss!")
            if attempts == 5:
                print("X/5 - Better luck next time!")
            else:
                attempts += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
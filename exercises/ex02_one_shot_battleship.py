"""EX01 - One Shot Battleship - Let's Do it!"""

__author__ = "730392828"

grid_size: int = 4
secret_row: int = 3
secret_col: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

row_guess: int = int(input("Guess a row: "))
while row_guess < 1 or row_guess > grid_size:
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

col_guess: int = int(input("Guess a column: "))
while col_guess < 1 or col_guess > grid_size:
    col_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# creating red and white box for miss or hit
if row_guess == secret_row and col_guess == secret_col:
    result = RED_BOX
else: 
    result = WHITE_BOX

# creating counter for rows/creating a grid
row_counter = 1
while row_counter <= grid_size:
    # creating counter for emojis, before printing
    emoji_row = ""
    column_counter = 1
    while column_counter <= grid_size:
        if row_guess == row_counter and col_guess == column_counter:
            emoji_row += result
        else: 
            emoji_row += BLUE_BOX
        column_counter += 1
    print(emoji_row)
    row_counter += 1

# creating a hint for the participant
if row_guess == secret_row and col_guess == secret_col:
    print("Hit!")
elif row_guess == secret_row:
    print("Close! Correct row, wrong column.")
elif col_guess == secret_col:
    print("Close! Correct column, wrong row.")
else: 
    print("Miss!")





    


    

"""Demonstrates while loops by finding low value in string"""

cards: str = 5235

card_idx: int = 0
#look at each number in the string
while card_idx < 4:
    print(cards[card_idx])
    card_idx = card_idx + 1
    
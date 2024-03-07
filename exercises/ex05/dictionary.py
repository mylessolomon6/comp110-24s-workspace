"""5th Assignment of COMP110."""

__author__ = "730392828"


def invert(scope: dict[str, str]) -> dict[str, str]:
    """This is the creation of the invert function."""
    list_inverted: dict[str, str] = {}
    for key in scope:
        if scope[key] in list_inverted:
            raise KeyError("You can't have the same inputs.")
        else:
            list_inverted[scope[key]] = key
    return list_inverted


def favorite_color(percol: dict[str, str]) -> str:
    """This is to determine the color that most frequently appears."""
    color_counter: dict[str, int] = {}
    score: int = 0
    highest: str = ""
    for key in percol:
        if percol[key] in color_counter:
            color_counter[percol[key]] += 1
        else:
            color_counter[percol[key]] = 1
    for key in color_counter:
        if color_counter[key] > score:
            score = color_counter[key]
            highest = key
    return highest


def count(num4: list[str]) -> dict[str, int]:
    """Define count."""
    val_store: dict[str, int] = {}
    for key in num4:
        if key in val_store:
            val_store[key] += 1
        else:
            val_store[key] = 1
    return val_store


def alphabetizer(nels: list[str]) -> dict[str, list[str]]:
    """Grouping all the words that begin with a specific letter together."""
    words: dict[str, list[str]] = {}
    for key in nels:
        letteruno = key[0].lower()
        if letteruno in words:
            words[letteruno].append(key)
        else:
            words[letteruno] = [key]
    return words


def update_attendance(attendance_log: dict[str, list[str]], days: str, goodstu: str) -> None:
    """Keeping track of the students who attended class on specific days."""
    for key in attendance_log:
        days = key
        if days in attendance_log:
            attendance_log[days].append(goodstu)
        else:
            attendance_log[days] = [goodstu]
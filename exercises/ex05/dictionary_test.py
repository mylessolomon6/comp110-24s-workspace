"""Checking to see if my EX05 works under different circumstances."""

__author__ = "730392828"
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_uc() -> dict[str, str]:
    """Checking to see if invert function works correctly."""
    scope = {"green": "hams", "water": "bottle"}
    list_inverted = {"hams": "green", "bottle": "water"}
    assert invert(scope) == list_inverted


def test_invert_uc2() -> dict[str, str]:
    """Checking to see if invert function works correctly - part 2."""
    scope = {"bacon": "sausage", "watermelon": "ice cream"}
    assert invert(scope) == {"sausage": "bacon", "ice cream": "watermelon"}


def test_invert_ec() -> dict[str, str]:
    """Checking to see if invert function works correctly - edge case."""
    scope = {}
    assert invert(scope) == {}


def test_favorite_color_uc() -> str:
    """Checking to see if favorite color works (use case)."""
    percol = {"Marcus": "blue", "Akoya": "blue", "Alexa": "green"}
    assert favorite_color(percol) == "blue"


def test_favorite_color_uc2() -> str:
    """Checking to see if favorite color works (with stores)."""
    percol = {"Walmart": "blue", "Target": "red", "Fairprice": "red"}
    assert favorite_color(percol) == "red"


def test_favorite_color_ec() -> str:
    """Checking to see if favorite color works (with an empty list)."""
    percol = {"Akoya": "red", "Brian": "green", "Cameron": "red", "Javair": "green"}
    assert favorite_color(percol) == "red"


def test_count_uc() -> dict[str, int]:
    """Checking to see if count works (use case)."""
    num4 = ["hello", "graduate", "banana", "hello", "apple"]
    assert count(num4) == {"hello": 2, "graduate": 1, "banana": 1, "apple": 1}


def test_count_uc2() -> dict[str, int]:
    """Checking to see if count works (using letters)."""
    num4 = ["85", "82", "95", "95", "95", "85"]
    assert count(num4) == {"85": 2, "82": 1, "95": 3}


def test_count_ec() -> dict[str, int]:
    """Checking to see if count works (using edge case)."""
    num4 = []
    assert count(num4) == {}


def test_alphabetizer_uc() -> dict[str, list[str]]:
    """Checking to see if grouping all words with specific letter work."""
    nels = ["water", "costume", "glasses", "western", "cat"]
    assert alphabetizer(nels) == {"w": ["water", "western"], "c": ["costume", "cat"], "g": ["glasses"]}


def test_alphabetizer_uc2() -> dict[str, list[str]]:
    """Checking to see if grouping all words with specific letter work (part 2)."""
    nels = ["Python", "Camry", "competition", "Potion", "phone"]
    assert alphabetizer(nels) == {"p": ["Python", "Potion", "phone"], "c": ["Camry", "competition"]}


def test_alphabetizer_ec() -> dict[str, list[str]]:
    """Checking to see if grouping all words with specific letters (edge case)."""
    nels = []
    assert alphabetizer(nels) == {}


def test_update_attendance_uc() -> None:
    """Checking to make sure log is working properly."""
    attendance_log = {"Monday": ["Akoya", "Cameron"], "Thursday": ["Stacia", "Dontae"]}
    days = "Thursday"
    goodstu = "Sam"
    update_attendance(attendance_log, days, goodstu) 
    assert attendance_log == {"Monday": ["Akoya", "Cameron"], "Thursday": ["Stacia", "Dontae", "Sam"]}


def test_update_attendance_uc2() -> None:
    """Checking to make sure log is working properly (pt.2)."""
    attendance_log = {"Tuesday": ["Ronaldo", "Messi"], "Wednesday": ["James", "Bryant"]}
    days = "Tuesday"
    goodstu = "Beckham"
    update_attendance(attendance_log, days, goodstu)
    assert attendance_log == {"Tuesday": ["Ronaldo", "Messi", "Beckham"], "Wednesday": ["James", "Bryant"]}


def test_update_attendance_ec() -> None:
    """Checking to make sure log is working properly (ec)."""
    attendance_log = {"Monday": ["Akoya", "Cameron"], "Thursday": ["Stacia", "Dontae"]}
    days = "Friday"
    goodstu = "Sam"
    update_attendance(attendance_log, days, goodstu)
    assert attendance_log == {"Monday": ["Akoya", "Cameron"], "Thursday": ["Stacia", "Dontae"], "Friday": ["Sam"]}
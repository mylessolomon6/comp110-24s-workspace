"""Test my garden functions."""

__author__ = "730392828"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_uc() -> None:
    """Add by kind list with another flower should return complete list of flowers."""
    by_kind = {"flower": ["rose", "tulip", "daisy"]}
    new_plant_kind = "flower"
    new_plant = "sunflower"
    assert add_by_kind(by_kind, new_plant_kind, new_plant) == {"flower": ["rose", "tulip", "daisy", "sunflower"]}


def test_add_by_kind_ec() -> None:
    """Add by kind list with new category should add to dictionary."""
    by_kind = {"flower": ["rose", "daisy"]}
    new_plant_kind = "fruit"
    new_plant = "watermelon"
    assert add_by_kind(by_kind, new_plant_kind, new_plant) == {"flower": ["rose", "daisy"], "fruit": ["watermelon"]}


def test_add_by_date_uc() -> None:
    """Organizing the plant type with the month its seeds should be sown that is already in a list."""
    garden_by_date = {"April": ["carrots", "strawberries"], "June": ["watermelon"]}
    month = "April"
    plant = "sunflowers"
    assert add_by_date(garden_by_date, month, plant) == {"April": ["carrots", "strawberries", "sunflowers"], "June": ["watermelon"]}


def test_add_by_date_ec() -> None:
    """Organizing the plant type with the month its seeds should be sown."""
    garden_by_date = {"April": ["carrots", "strawberries"], "June": ["watermelon"]}
    month = "July"
    plant = "sunflowers"
    assert add_by_date(garden_by_date, month, plant) == {"April": ["carrots", "strawberries"], "June": ["watermelon"], "July": ["sunflowers"]}


def test_lookup_by_kind_and_date_uc() -> str:
    """Testing to see if return string with list of plants of a specific kind to plant in a specific month."""
    plants_by_kind = {"flower": ["marigold", "sunflowers"], "vegetable": ["green beans"]}
    plants_by_date = {"April": ["marigold", "sunflowers"], "May": ["green beans"]}
    kind = "flower"
    month = "April"
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month) == "flowers to plant in April: ['marigold', 'sunflowers']"


def test_lookup_by_kind_and_date_ec() -> str:
    """Testing to see if return string with list of plants of a specific kind to plant in a specific month (ec now)."""
    plants_by_kind = {"flower": ["marigold", "sunflowers"], "vegetable": ["green beans"]}
    plants_by_date = {"April": ["marigold", "sunflowers"], "May": ["green beans"]}
    kind = "flower"
    month = "May"
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month) == "No flowers to plant in May."
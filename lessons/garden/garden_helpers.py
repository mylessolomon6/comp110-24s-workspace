"""Some functions for my garden plan!"""

__author__ = "730392828"


# Function name: add by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None
def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind...this should now work for any plant kind."""
    if new_plant_kind in by_kind: # if the kind is already in the dictionary ("flower" was in by_kind, so I did this)
        by_kind[new_plant_kind].append(new_plant)
    else: #if the kind is not in the dictionary (e.g. "fruit" is not in by_kind)
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)
    return by_kind


# want to get: {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}

def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under state to sow seeds."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)

# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str
        
def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return string with list of plants of a specific kind to plant in a specific month."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    # Get a list of all plants of the specific kind input
    if kind in plants_by_kind:
        kind_list: list[str] = plants_by_kind[kind]
        # Get a list of all plants planted in a specific month
        month_list: list[str] = plants_by_date[month]
        # Go through both lists and find elements that appear in both.
        # kind_list = ["marigold", "daisy"]
        # month_list - ["daisy", "rose"]
        combined_list: list[str] = []
        for plant in kind_list:
            for other_plant in month_list:
                if plant == other_plant: # plant is in both kind_list and month_list
                    combined_list.append(other_plant)
    # "<kind>s to plant in <month>: <combined_list>"
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else: # 'No <kind>s to plant in ,month.'
        return f"No {kind}s to plant in {month}."
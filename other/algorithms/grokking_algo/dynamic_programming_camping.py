from dataclasses import dataclass

from rich import pretty
"""
Exercise 9.2 

Suppose you’re going camping. 

You have a knapsack that will hold 6 lb, and you can take the following items. 

Each has a value, and the higher the value, the more important the item is: 

Water, 3 lb, 10 
Book, 1 lb, 3 
Food, 2 lb, 9 
Jacket, 2 lb, 5 
Camera, 1 lb, 6

What’s the optimal set of items to take on your camping trip?
"""

@dataclass
class Item:
    name: str
    weight: int
    value: int


ITEMS = (
    Item(name="Water", weight=3, value=10),
    Item(name="Book", weight=1, value=3),
    Item(name="Food", weight=2, value=9),
    Item(name="Jacket", weight=2, value=5),
    Item(name="Camera", weight=1, value=6),
)

ITEMS2 = (
    Item(name="Guitar", weight=1, value=1_500),
    Item(name="Stereo", weight=4, value=3_000),
    Item(name="Laptop", weight=3, value=2_000),
)


@dataclass
class Cell:
    capacity: int
    value: int = 0
    weight: int = 0
    items: list[Item] | None = None


def solve_using_dyn_prog(
    items: tuple[Item, ...],
    capacity: int,
) -> list[Cell]:

    containers = []
    for i in range(capacity):
        cell = Cell(capacity=i + 1)
        cell.items = []
        containers.append(cell)

    for i in range(len(items)):
        for j in range(capacity):
            item = items[i]
            cell = containers[j]
            if item.weight <= cell.capacity and item.value > cell.value:
                cell.items = [item]
                cell.weight = item.weight
                cell.value = item.value
            elif cell.weight + item.weight <= cell.capacity:
                cell.items.append(item)
                cell.weight += item.weight
                cell.value += item.value
            pretty.pprint(containers)
    return containers

# pretty.pprint(solve_using_dyn_prog(ITEMS, 6))
pretty.pprint(solve_using_dyn_prog(ITEMS2, 4))

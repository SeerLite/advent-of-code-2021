from typing import Sequence
from collections import defaultdict

EXAMPLE_MODE = False
DEBUG = False

def read_input() -> list[int]:
    filename = "input.txt" if not EXAMPLE_MODE else "input.example.txt"
    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def calculate_cheapest_pos(crabs: Sequence[int]) -> tuple[int, int]:
    crabs = sorted(crabs)
    expenses: defaultdict[int, int] = defaultdict(int)
    for position in range(crabs[0], crabs[-1] + 1): # crabs are sorted
        for crab in crabs:
            expenses[position] += abs(position - crab)
            if DEBUG:
                print(position, expenses[position])

    cheapest_pos = min(expenses, key=lambda position: expenses[position])
    fuel = expenses[cheapest_pos]

    return cheapest_pos, fuel


crabs = read_input()
cheapest_pos, fuel = calculate_cheapest_pos(crabs)

print(f"Cheapest position for all crabs to align at is"
      f"{cheapest_pos} and the total fuel used to get there is {fuel}")

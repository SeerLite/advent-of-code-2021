from typing import Sequence
from collections import defaultdict

EXAMPLE_MODE = False
DEBUG = False

Expenses = dict[int, int]

def read_input() -> list[int]:
    filename = "input.txt" if not EXAMPLE_MODE else "input.example.txt"
    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def calculate_cheapest_expense(crabs: Sequence[int], key=lambda pos, crab: abs(pos - crab)) -> int:
    crabs = sorted(crabs)
    expenses: dict[int, int] = defaultdict(int)
    for position in range(crabs[0], crabs[-1] + 1): # crabs are sorted
        for crab in crabs:
            expenses[position] += key(position, crab)
            if DEBUG:
                print(position, expenses[position])

    return min(expenses.values())

crabs = read_input()
cheapest_expense = calculate_cheapest_expense(crabs)

true_cheapest_expense = calculate_cheapest_expense(
    crabs,
    key=lambda pos, crab: sum(range(abs(pos - crab) + 1))
)

print(f"At the most efficient position, the spent fuel is {cheapest_expense}")
print(f"Oh sorry, it's actually {true_cheapest_expense}")

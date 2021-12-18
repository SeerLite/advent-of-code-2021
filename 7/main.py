# post-solution means I've already seen other people's solutions

from typing import Sequence, Optional
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
    min_expense: Optional[int] = None
    for position in range(crabs[0], crabs[-1] + 1): # crabs are sorted
        current_expense = 0
        for crab in crabs:
            current_expense += key(position, crab)
            if DEBUG:
                print(position, current_expense)

        if min_expense is None or current_expense < min_expense:
            min_expense = current_expense

    # For mypy
    if min_expense is None:
        return 0

    return min_expense

# NOTE: post-solution
def summation(n):
    return n * (n + 1) // 2

crabs = read_input()
cheapest_expense = calculate_cheapest_expense(crabs)

true_cheapest_expense = calculate_cheapest_expense(
    crabs,
    # NOTE: post-solution
    key=lambda pos, crab: summation(pos - crab)
    # key=lambda pos, crab: abs(pos - crab) * (abs(pos - crab) + 1) // 2
)

print(f"At the most efficient position, the spent fuel is {cheapest_expense}")
print(f"Oh sorry, it's actually {true_cheapest_expense}")

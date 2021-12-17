from collections.abc import Sequence
from typing import Any, Union
from time import sleep
import math

EXAMPLE = True
DEBUG = True
ONLY_INDEXES: Union[list[int], "fakelist"] = []

if not ONLY_INDEXES:
    # Always contains everything
    # Yes I know this is dumb but whatever
    class fakelist(list):
        def __contains__(self, value):
            return True
    ONLY_INDEXES = fakelist()

def read_list_from_file() -> list[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def prettyprint_list(li: Sequence[Any]) -> None:
    print("\t".join(str(x) for x in li))


def print_new_lanternfishes(lanternfishes: Sequence[int], days: int) -> None:
    lanternfishes = list(lanternfishes)
    new_lanternfishes: list[int] = []
    for day in range(days):
        for i in range(len(new_lanternfishes)):
            new_lanternfishes[i] -= 1

        for i in range(len(lanternfishes)):
            lanternfishes[i] -= 1
            if lanternfishes[i] < 0:
                lanternfishes[i] = 6
                if i in ONLY_INDEXES:
                    new_lanternfishes.append(8)

    prettyprint_list(new_lanternfishes)


def print_new_lanternfishes_m(lanternfishes: Sequence[int], days: int) -> None:
    lanternfishes = list(lanternfishes)
    new_lanternfishes: list[int] = []
    for i in range(len(lanternfishes)):
        new_fishes_num = math.ceil((lanternfishes[i] - days) / -7)
        if i in ONLY_INDEXES:
            new_lanternfishes += range(
                # Shift by the distance from 0 (+ 1 but I'm not sure why)
                8 + lanternfishes[i] + 1,
                # Cycle goes for 7 days
                8 + lanternfishes[i] + 1 + 7 * new_fishes_num,
                7
            )

    for i in range(len(new_lanternfishes)):
        new_lanternfishes[i] -= days

    prettyprint_list(sorted(x for x in new_lanternfishes))


days = 18
lanternfishes = read_list_from_file()
prettyprint_list(lanternfishes)
print_new_lanternfishes(lanternfishes, days)
print_new_lanternfishes_m(lanternfishes, days)

from collections.abc import Sequence, MutableSequence
from typing import Any, Union
from time import sleep
import math

EXAMPLE = True
DEBUG = True

def read_list_from_file() -> list[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def print_new_lanternfishes(lanternfishes: Sequence[int], days: int) -> None:
    lanternfishes = list(lanternfishes)
    for day in range(days):
        for i in range(len(lanternfishes)):
            lanternfishes[i] -= 1
            if lanternfishes[i] < 0:
                lanternfishes[i] = 6
                lanternfishes.append(8)

    # print(sorted(x for x in lanternfishes))
    print(len(sorted(x for x in lanternfishes)))


def recurse_lanternfishes(lanternfishes: Sequence[int], days: int) -> list[int]:
    if not lanternfishes:
        return list(lanternfishes)
    lanternfishes = list(lanternfishes)
    new_lanternfishes: list[int] = []
    for i in range(len(lanternfishes)):
        new_fishes_num = math.ceil((lanternfishes[i] - days) / -7)
        new_lanternfishes += range(
            # Shift by the distance from 0 (+ 1 but I'm not sure why)
            8 + lanternfishes[i] + 1,
            # Cycle goes for 7 days
            8 + lanternfishes[i] + 1 + 7 * new_fishes_num,
            7
        )

    lanternfishes += recurse_lanternfishes(new_lanternfishes, days)

    return lanternfishes

def print_new_lanternfishes_m(lanternfishes: Sequence[int], days: int) -> None:
    # print(sorted(x for x in recurse_lanternfishes(lanternfishes, days)))
    print(len(sorted(x for x in recurse_lanternfishes(lanternfishes, days))))


days = 90
lanternfishes = read_list_from_file()
print(lanternfishes)
print_new_lanternfishes(lanternfishes, days)
print_new_lanternfishes_m(lanternfishes, days)

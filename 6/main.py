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


def recurse_lanternfishes(lanternfishes: MutableSequence[int], days: int) -> int:
    global recursion_level
    recursion_level += 1

    if DEBUG:
        print(recursion_level)

    if not lanternfishes:
        recursion_level -= 1
        return 0

    numlanternfishes = len(lanternfishes)

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

    lanternfishes.clear()
    len_new_level = recurse_lanternfishes(new_lanternfishes, days)
    recursion_level -= 1
    return numlanternfishes + len_new_level

def print_new_lanternfishes_m(lanternfishes: MutableSequence[int], days: int) -> None:
    print(recurse_lanternfishes(lanternfishes, days))

lanternfishes_len = 0
recursion_level = 0
days = 150
lanternfishes = read_list_from_file()
print(lanternfishes)
# print_new_lanternfishes(lanternfishes, days)
print_new_lanternfishes_m(lanternfishes, days)

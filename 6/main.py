from collections.abc import Sequence, MutableSequence, Iterable
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


def recurse_lanternfishes(lanternfishes: Iterable[int], days: int) -> int:
    global current_num
    global recursion_level
    recursion_level += 1

    # if DEBUG:
    #     print(recursion_level)

    if not lanternfishes:
        recursion_level -= 1
        return 0

    num_lanternfishes = 0

    for timer in lanternfishes:
        new_fishes_num = math.ceil((timer - days) / -7)
        num_lanternfishes += 1
        num_lanternfishes += recurse_lanternfishes(
            range(
                # Shift by the distance from 0 (+ 1 but I'm not sure why)
                8 + timer + 1,
                # Cycle goes for 7 days
                8 + timer + 1 + 7 * new_fishes_num,
                7
            ),
            days
        )


    if num_lanternfishes > current_num:
        current_num = num_lanternfishes
        print(recursion_level, current_num)

    recursion_level -= 1
    return num_lanternfishes

def print_new_lanternfishes_m(lanternfishes: MutableSequence[int], days: int) -> None:
    print(recurse_lanternfishes(lanternfishes, days))

current_num = 0
lanternfishes_len = 0
recursion_level = 0
days = 256
lanternfishes = read_list_from_file()
print(lanternfishes)
# print_new_lanternfishes(lanternfishes, days)
print_new_lanternfishes_m(lanternfishes, days)

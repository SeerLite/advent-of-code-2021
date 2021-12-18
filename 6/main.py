from collections.abc import Sequence, MutableSequence, Iterable
from typing import Any, Union
from time import sleep
import math

EXAMPLE = False
DEBUG = False

def read_list_from_file() -> list[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]


def recurse_lanternfishes(lanternfishes: Iterable[int], days: int, range_result_cache=None, current_max=0, recursion_level=0) -> int:
    recursion_level += 1

    if not lanternfishes:
        recursion_level -= 1
        return 0

    num_lanternfishes = 0

    if range_result_cache is None:
        range_result_cache = {}

    for timer in lanternfishes:
        new_fishes_num = math.ceil((timer - days) / -7)
        num_lanternfishes += 1
        next_range =  range(
            # Shift by the distance from 0 (+ 1 but I'm not sure why)
            8 + timer + 1,
            # Cycle goes for 7 days
            8 + timer + 1 + 7 * new_fishes_num,
            7
        )

        if next_range in range_result_cache:
            range_result = range_result_cache[next_range]
        else:
            range_result = recurse_lanternfishes(next_range, days, range_result_cache, current_max, recursion_level)
            range_result_cache[next_range] = range_result
        num_lanternfishes += range_result

    if num_lanternfishes > current_max:
        current_max = num_lanternfishes
        if DEBUG:
            print(recursion_level, current_max)

    recursion_level -= 1
    return num_lanternfishes

days = 256
lanternfishes = read_list_from_file()
print(recurse_lanternfishes(lanternfishes, days))

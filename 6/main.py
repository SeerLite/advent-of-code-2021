from collections.abc import Sequence
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

lanternfishes = read_list_from_file()
print(lanternfishes)

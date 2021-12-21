from __future__ import annotations
import itertools
from collections.abc import Sequence
from dataclasses import dataclass
from typing import NamedTuple
import aocutils
from aocutils import printd

aocutils.DEBUG = True
aocutils.USE_EXAMPLE_INPUT = True
aocutils.EXAMPLE_OUTPUTS = [1656]

OctopusMap = Sequence[Sequence[int]]

@dataclass
class Coordinate:
    x: int
    y: int
    def __add__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x - other.x, self.y - other.y)

def read_input() -> OctopusMap:
    filename = "input.example.txt" if aocutils.USE_EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [list(int(x) for x in line) for line in input_file.read().strip().split("\n")]

def print_map(o_map: OctopusMap) -> None:
    printd("\n".join("".join(str(c) for c in line) for line in o_map))

def main() -> list[int]:
    outputs: list[int] = []
    o_map = read_input()
    print_map(o_map)

    return outputs

if __name__ == "__main__":
    aocutils.assert_outputs(main())

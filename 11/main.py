from __future__ import annotations
import itertools
from collections.abc import Sequence
from dataclasses import dataclass
from typing import NamedTuple

DEBUG = True
EXAMPLE_INPUT = True
EXAMPLE_OUTPUTS: list[int] = [1656]
outputs: list[int] = []

OctopusMap = Sequence[Sequence[int]]

@dataclass
class Coordinate:
    x: int
    y: int
    def __add__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x - other.x, self.y - other.y)

def printd(*args, **kwargs) -> None: # type: ignore
    if DEBUG:
        print(*args, **kwargs)

def print_map(o_map: OctopusMap) -> None:
    printd("\n".join("".join(str(c) for c in line) for line in o_map))

def read_input() -> OctopusMap:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [list(int(x) for x in line) for line in input_file.read().strip().split("\n")]

o_map = read_input()
print_map(o_map)

for i, output, example_output in zip(itertools.count(1), outputs, EXAMPLE_OUTPUTS):
    assert output == example_output, f"output {i} doesn't match with one from official example: got {output}, should be {example_output}"

assert len(outputs) >= len(EXAMPLE_OUTPUTS), f"got only {len(outputs)} out of {len(EXAMPLE_OUTPUTS)} outputs"

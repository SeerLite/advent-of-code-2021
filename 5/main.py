from typing import NamedTuple
from itertools import chain
from collections import defaultdict
import math

EXAMPLE_MODE = False

if EXAMPLE_MODE:
    from sys import stdout
    from time import sleep

    UPDATE_DELAY = 0.2

    def display_map(map: "Map") -> None:
        # Clear screen via terminal escape sequence
        stdout.write("\x1b[H\x1b[J")
        max_x = 0
        min_x = float("inf")
        for y in range(min(map.keys()), max(map.keys()) + 1):
            if map[y].keys():
                max_x = max(*map[y].keys(), max_x)
                min_x = min(*map[y].keys(), min_x)

        min_x = int(min_x)

        for y in range(min(map.keys()), max(map.keys()) + 1):
            for x in range(min_x, max_x + 1): # int() is redundant but mypy complains
                stdout.write(str(map[y][x]) if map[y][x] > 0 else ".")
            stdout.write("\n")
        stdout.flush()


class Coordinate(NamedTuple):
    x: int
    y: int

class Vector(NamedTuple):
    start: Coordinate
    end: Coordinate

Map = defaultdict[int, defaultdict[int, int]]

def read_input_file() -> str:
    filename = "input.txt" if not EXAMPLE_MODE else "input.example.txt"
    with open(filename) as input_file:
        return input_file.read().strip()

def parse_vectors(raw_vectors: list[str]) -> list[Vector]:
    vectors = []
    for vector in raw_vectors:
        raw_start, raw_end = vector.split(" -> ")
        start = Coordinate(*(int(n) for n in raw_start.split(",")))
        end = Coordinate(*(int(n) for n in raw_end.split(",")))
        vectors.append(Vector(start, end))

    return vectors


def fill_lines(vectors: list[Vector]) -> Map:
    map: Map = defaultdict(lambda: defaultdict(int))
    for vector in vectors:
        x_increment = int(math.copysign(1, vector.end.x - vector.start.x))
        y_increment = int(math.copysign(1, vector.end.y - vector.start.y))

        if vector.start.x == vector.end.x:
            x = vector.start.x
            for y in range(vector.start.y, vector.end.y + y_increment, y_increment):
                map[y][x] += 1
                if EXAMPLE_MODE:
                    display_map(map)
                    print(x, y)
                    print()
                    sleep(UPDATE_DELAY)
        elif vector.start.y == vector.end.y:
            y = vector.start.y
            for x in range(vector.start.x, vector.end.x + x_increment, x_increment):
                map[y][x] += 1
                if EXAMPLE_MODE:
                    display_map(map)
                    print(x, y)
                    print()
                    sleep(UPDATE_DELAY)
        else:
            for x, y in zip(
                range(vector.start.x, vector.end.x + x_increment, x_increment),
                range(vector.start.y, vector.end.y + y_increment, y_increment)
            ):
                map[y][x] += 1
                if EXAMPLE_MODE:
                    display_map(map)
                    print(x, y)
                    print()
                    sleep(UPDATE_DELAY)

    return map

def count_overlapping_cells(map: Map) -> int:
    flattened_map = chain(*(row.values() for row in map.values()))
    return [x >= 2 for x in flattened_map].count(True)

vectors: list[Vector] = parse_vectors(read_input_file().split("\n"))
map: Map = fill_lines(vectors)
overlapping_cells = count_overlapping_cells(map)

print(f"Number of overlapping vents: {overlapping_cells}")

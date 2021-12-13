from typing import List, Tuple, NamedTuple, DefaultDict
from itertools import chain
from collections import defaultdict

class Coordinate(NamedTuple):
    x: int
    y: int

class Vector(NamedTuple):
    start: Coordinate
    end: Coordinate

Map = DefaultDict[int, DefaultDict[int, int]]

def read_input_file() -> str:
    with open("input.txt") as input_file:
        return input_file.read().strip()

def parse_vectors(raw_vectors: List[str]) -> List[Vector]:
    vectors = []
    for vector in raw_vectors:
        raw_start, raw_end = vector.split(" -> ")
        start = Coordinate(*(int(n) for n in raw_start.split(",")))
        end = Coordinate(*(int(n) for n in raw_end.split(",")))
        vectors.append(Vector(start, end))

    return vectors


def fill_aligned_lines(vectors: List[Vector]) -> Map:
    map: Map = defaultdict(lambda: defaultdict(int))
    for vector in vectors:
        if vector.start.x == vector.end.x:
            for y in range(min(vector.start.y, vector.end.y), max(vector.start.y, vector.end.y) + 1):
                map[y][vector.start.x] += 1
        elif vector.start.y == vector.end.y:
            for x in range(min(vector.start.x, vector.end.x), max(vector.start.x, vector.end.x) + 1):
                map[vector.start.y][x] += 1
    return map

def count_overlapping_lines(map: Map) -> int:
    flattened_map = chain(*(row.values() for row in map.values()))
    return [x >= 2 for x in flattened_map].count(True)

vectors: List[Vector] = parse_vectors(read_input_file().split("\n"))
map: Map = fill_aligned_lines(vectors)
overlapping_lines = count_overlapping_lines(map)

print(f"Number of overlapping vents: {overlapping_lines}")

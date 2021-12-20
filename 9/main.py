from typing import NamedTuple, Iterable, Sequence, Union
from copy import deepcopy
from time import sleep

DEBUG = True
EXAMPLE_INPUT = False
EXPECTED_EXAMPLE_OUTPUT_1 = 15
EXPECTED_EXAMPLE_OUTPUT_2 = 1134
output_1 = 0
output_2 = 0

HeightMap = Sequence[Sequence[int]]

class Coordinate(NamedTuple):
    x: int
    y: int

def read_input() -> HeightMap:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [[int(x) for x in line] for line in input_file.read().strip().split("\n")]

def print_map(height_map: Union[HeightMap, Sequence[Sequence[Union[str, int]]]]) -> None:
    print("\n".join("".join(str(x) for x in line) for line in height_map))

def get_neighbors(height_map: HeightMap, coordinate: Coordinate) -> dict[Coordinate, int]:
    map_height, map_width = len(height_map), len(height_map[0])
    neighbors: dict[Coordinate, int] = {}
    if coordinate.x > 0:
        neighbors[Coordinate(coordinate.x - 1, coordinate.y)] = height_map[coordinate.y][coordinate.x - 1]
    if coordinate.x < map_width - 1:
        neighbors[Coordinate(coordinate.x + 1, coordinate.y)] = height_map[coordinate.y][coordinate.x + 1]
    if coordinate.y > 0:
        neighbors[Coordinate(coordinate.x, coordinate.y - 1)] = height_map[coordinate.y - 1][coordinate.x]
    if coordinate.y < map_height - 1:
        neighbors[Coordinate(coordinate.x, coordinate.y + 1)] = height_map[coordinate.y + 1][coordinate.x]

    return neighbors

def get_low_points(height_map: HeightMap) -> dict[Coordinate, int]:
    low_points: dict[Coordinate, int] = {}
    for y, row in enumerate(height_map):
        for x, value in enumerate(row):
            neighbors = get_neighbors(height_map, Coordinate(x, y))
            if all(value < neighbor_value for neighbor_value in neighbors.values()):
                low_points[Coordinate(x, y)] = value
    return low_points

def get_greater_neighbors(height_map: HeightMap, points: Iterable[Coordinate]) -> set[Coordinate]:
    greater_neighbors = set[Coordinate]()
    for coordinate in points:
        for neighbor_coord, neighbor_value in get_neighbors(height_map, coordinate).items():
            if 9 > neighbor_value > height_map[coordinate.y][coordinate.x]:
                greater_neighbors.add(neighbor_coord)

    return greater_neighbors

def get_basin_sizes(height_map: HeightMap, points: Iterable[Coordinate]) -> list[int]:
    sizes: list[int] = []
    if DEBUG:
        debug_map: list[list[Union[str, int]]] = [
            [value for value in row] for row in height_map
        ]

    for i, coordinate in enumerate(points):
        size = 1
        neighbors: Iterable[Coordinate] = [coordinate]
        prev_neighbors = set[Coordinate]()
        while (neighbors := get_greater_neighbors(height_map, neighbors)):
            neighbors -= prev_neighbors
            prev_neighbors.update(neighbors)
            size += len(neighbors)

            if DEBUG:
                for neighbor in neighbors:
                    debug_map[neighbor.y][neighbor.x] = " "
                print_map(debug_map)
                print()
                if EXAMPLE_INPUT:
                    sleep(0.2)

        sizes.append(size)
    return sizes

height_map = read_input()

if DEBUG:
    print_map(height_map)

low_points = get_low_points(height_map)

if DEBUG:
    print(low_points)

total_risk_level = sum(low_points.values()) + len(low_points)
output_1 = total_risk_level

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT_1 is not None:
    assert output_1 == EXPECTED_EXAMPLE_OUTPUT_1,  f"output doesn't match with one from official example: got {output_1}, should be {EXPECTED_EXAMPLE_OUTPUT_1}"

print(f"The total risk level is {total_risk_level}")

basin_sizes = get_basin_sizes(height_map, low_points.keys())
if DEBUG:
    print(basin_sizes)

largest_basins_product = 1
for size in sorted(basin_sizes, reverse=True)[:3]:
    largest_basins_product *= size

output_2 = largest_basins_product

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT_2 is not None:
    assert output_2 == EXPECTED_EXAMPLE_OUTPUT_2,  f"output doesn't match with one from official example: got {output_2}, should be {EXPECTED_EXAMPLE_OUTPUT_2}"

print(f"The product of the three largest basins is {largest_basins_product}")

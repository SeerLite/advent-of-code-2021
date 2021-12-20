from typing import NamedTuple

DEBUG = True
EXAMPLE_INPUT = True
EXPECTED_EXAMPLE_OUTPUT_1 = 15
EXPECTED_EXAMPLE_OUTPUT_2 = 1134
output_1 = 0
output_2 = 0

HeightMap = list[list[int]]

class Coordinate(NamedTuple):
    x: int
    y: int

def read_input() -> HeightMap:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [[int(x) for x in line] for line in input_file.read().strip().split("\n")]

def print_map(height_map: HeightMap) -> None:
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

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT_2 is not None:
    assert output_2 == EXPECTED_EXAMPLE_OUTPUT_2,  f"output doesn't match with one from official example: got {output_2}, should be {EXPECTED_EXAMPLE_OUTPUT_2}"

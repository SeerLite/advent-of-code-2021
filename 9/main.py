DEBUG = True
EXAMPLE_INPUT = True
EXPECTED_EXAMPLE_OUTPUT = 15
output = 0

HeightMap = list[list[int]]

def read_input() -> HeightMap:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [[int(x) for x in line] for line in input_file.read().strip().split("\n")]

def print_map(height_map: HeightMap) -> None:
    print("\n".join("".join(str(x) for x in line) for line in height_map))

def get_low_points(height_map: HeightMap) -> list[int]:
    map_height, map_width = len(height_map), len(height_map[0])
    low_points: list[int] = []
    for x in range(map_width):
        for y in range(map_height):
            if ((x == 0 or height_map[y][x] < height_map[y][x - 1])
            and (x == map_width - 1 or height_map[y][x] < height_map[y][x + 1])
            and (y == 0 or height_map[y][x] < height_map[y - 1][x])
            and (y == map_height - 1 or height_map[y][x] < height_map[y + 1][x])):
                low_points.append(height_map[y][x])
    return low_points

height_map = read_input()

if DEBUG:
    print_map(height_map)

low_points = get_low_points(height_map)

if DEBUG:
    print(low_points)

total_risk_level = sum(low_points) + len(low_points)
output = total_risk_level

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT is not None:
    assert output == EXPECTED_EXAMPLE_OUTPUT,  f"output doesn't match with one from official example: got {output}, should be {EXPECTED_EXAMPLE_OUTPUT}"

print(f"The total risk level is {total_risk_level}")

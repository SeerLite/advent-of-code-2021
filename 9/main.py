DEBUG = True
EXAMPLE_INPUT = True
EXPECTED_EXAMPLE_OUTPUT = 15
output = 0

def read_input() -> list[list[int]]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return [[int(x) for x in line] for line in input_file.read().strip().split("\n")]

def print_map(height_map: list[list[int]]) -> None:
    print("\n".join("".join(str(x) for x in line) for line in height_map))

height_map = read_input()

if DEBUG:
    print_map(height_map)

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT is not None:
    assert output == EXPECTED_EXAMPLE_OUTPUT,  f"output doesn't match with one from official example: got {output}, should be {EXPECTED_EXAMPLE_OUTPUT}"

from typing import Any

DEBUG = True
EXAMPLE_INPUT = True
EXPECTED_EXAMPLE_OUTPUT: Any = None
output: Any = None

def read_input() -> list[str]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return input_file.read().strip().split(",")

input_content = read_input()

if DEBUG:
    print(input_content)

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT is not None:
    assert output == EXPECTED_EXAMPLE_OUTPUT,  f"output doesn't match with one from official example: got {output}, should be {EXPECTED_EXAMPLE_OUTPUT}"

from __future__ import annotations
import aocutils
from aocutils import printd

aocutils.DEBUG = True
aocutils.USE_EXAMPLE_INPUT = True
aocutils.EXAMPLE_OUTPUTS = []

def read_input() -> list[str]:
    filename = "input.example.txt" if aocutils.USE_EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return input_file.read().strip().split(",")

def main() -> list[int]:
    outputs: list[int] = []
    input_content = read_input()
    printd(input_content)

    return outputs

if __name__ == "__main__":
    aocutils.assert_outputs(main())

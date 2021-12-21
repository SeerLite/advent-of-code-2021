import itertools

DEBUG = True
EXAMPLE_INPUT = True
EXAMPLE_OUTPUTS: list[int] = []
outputs: list[int] = []

def read_input() -> list[str]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return input_file.read().strip().split(",")

input_content = read_input()

if DEBUG:
    print(input_content)

for i, output, example_output in zip(itertools.count(1), outputs, EXAMPLE_OUTPUTS):
    assert output == example_output, f"output {i} doesn't match with one from official example: got {output}, should be {example_output}"

assert len(outputs) >= len(EXAMPLE_OUTPUTS), f"got only {len(outputs)} out of {len(EXAMPLE_OUTPUTS)} outputs"

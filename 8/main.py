from typing import Union, Sequence, MutableSequence, cast

EXAMPLE_INPUT = False
DEBUG = True

def read_input() -> tuple[list[list[str]], list[list[str]]]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        patterns: list[list[str]] = []
        codes: list[list[str]] = []
        for line in input_file:
            # Only get what's after the pipe character
            # NOTE: input is assumed to never split lines at
            # the pipe character, even if it's the example
            pattern, code = line.split("|")
            patterns.append(pattern.strip().split())
            codes.append(code.strip().split())

        return patterns, codes

def replace_known_numbers(lines: Sequence[MutableSequence[Union[str, int]]]):
    for line in lines:
        for i, number in enumerate(line):
            if isinstance(number, str):
                if len(number) == 2:
                    line[i] = 1
                elif len(number) == 4:
                    line[i] = 4
                elif len(number) == 3:
                    line[i] = 7
                elif len(number) == 7:
                    line[i] = 8

patterns: list[list[Union[str, int]]] = []
codes: list[list[Union[str, int]]] = []
# Apparently mypy doesn't catch copy.deepcopy() so I'm doing it manually
for pattern, code in zip(*read_input()):
    patterns.append([])
    patterns[-1].extend(pattern)
    codes.append([])
    codes[-1].extend(code)

replace_known_numbers(patterns)
replace_known_numbers(codes)

print(codes)

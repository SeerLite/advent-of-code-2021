from typing import Any, Tuple, Optional
from collections.abc import Iterable

DEBUG = True
EXAMPLE_INPUT = True
EXPECTED_EXAMPLE_OUTPUT_1 = 26397
EXPECTED_EXAMPLE_OUTPUT_2 = 288957
output_1: Optional[int] = None
output_2: Optional[int] = None
MATCHES = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

ERROR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AUTOCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def read_input() -> list[str]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return input_file.read().strip().split("\n")

def get_syntax_error_score(lines: Iterable[str]) -> int:
    scores: list[int] = []
    for line in lines:
        openings: list[str] = []
        for c in line:
            if c in MATCHES.keys():
                openings.append(c)
            else:
                expected_closing = MATCHES[openings.pop()]
                if expected_closing != c:
                    scores.append(ERROR_POINTS[c])
                    break

    return sum(scores)

lines = read_input()

if DEBUG:
    print(lines)

syntax_error_score = get_syntax_error_score(lines)
output_1 = syntax_error_score

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT_1 is not None:
    assert output_1 == EXPECTED_EXAMPLE_OUTPUT_1,  f"output_1 doesn't match with one from official example: got {output_1}, should be {EXPECTED_EXAMPLE_OUTPUT_1}"

print(f"The total syntax error score is {syntax_error_score}")

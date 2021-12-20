from typing import Any, Tuple, Optional
from collections.abc import Iterable

DEBUG = True
EXAMPLE_INPUT = False
EXPECTED_EXAMPLE_OUTPUT = 26397
output: Optional[int] = None
MATCHES = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def read_input() -> list[str]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        return input_file.read().strip().split("\n")

def check_syntax(line: str) -> Optional[Tuple[str, str]]:
    openings: list[str] = []
    for c in line:
        if c in MATCHES.keys():
            openings.append(c)
        else:
            expected_closing = MATCHES[openings.pop()]
            if expected_closing != c:
                return c, expected_closing

    return None

def get_syntax_error_score(lines: Iterable[str]) -> int:
    scores: list[int] = []
    for line in lines:
        score = 0
        if (syntax_error := check_syntax(line)):
            error, _ = syntax_error
            score += POINTS[error]
        scores.append(score)

    return sum(scores)

lines = read_input()

if DEBUG:
    print(lines)

syntax_error_score = get_syntax_error_score(lines)
output = syntax_error_score

if EXAMPLE_INPUT and EXPECTED_EXAMPLE_OUTPUT is not None:
    assert output == EXPECTED_EXAMPLE_OUTPUT,  f"output doesn't match with one from official example: got {output}, should be {EXPECTED_EXAMPLE_OUTPUT}"

print(f"The total syntax error score is {syntax_error_score}")

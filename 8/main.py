from collections.abc import Sequence, MutableSequence
from collections import defaultdict
from typing import Union, Any

EXAMPLE_INPUT = False
DEBUG = True

def read_input() -> tuple[list[list[frozenset[str]]], list[list[frozenset[str]]]]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        patterns: list[list[frozenset[str]]] = []
        codes: list[list[frozenset[str]]] = []
        for line in input_file:
            # Only get what's after the pipe character
            # NOTE: input is assumed to never split lines at
            # the pipe character, even if it's the example
            pattern, code = line.split("|")
            patterns.append([frozenset[str](number) for number in pattern.strip().split()])
            codes.append([frozenset[str](number) for number in code.strip().split()])

        return patterns, codes


def deduce_numbers(sequence: Sequence[frozenset[str]]) -> dict[frozenset[str], int]:
    deduced_numbers = {}
    for number in sequence:
        if len(number) == 2:
            deduced_numbers[number] = 1
        elif len(number) == 4:
            deduced_numbers[number] = 4
        elif len(number) == 3:
            deduced_numbers[number] = 7
        elif len(number) == 7:
            deduced_numbers[number] = 8

    return deduced_numbers

def deduce_code(patterns: Sequence[Sequence[frozenset[str]]], codes: Sequence[Sequence[frozenset[str]]]) -> None:
    PossibleSegments = defaultdict[int, set[str]]
    def segment_set():
        return set("abcdefg")

    for pattern, code in zip(patterns, codes):
        possible_segments = PossibleSegments(segment_set)
        # NOTE: the better way to concatenate Sequences
        # is with itertools.chain.from_iterable
        deduced_numbers = deduce_numbers(list(pattern) + list(code))
        substituted_code: list[Union[int, frozenset[str]]] = []
        for number in code:
            if number in deduced_numbers:
                substituted_code.append(deduced_numbers[number])
            else:
                substituted_code.append(number)

        if DEBUG:
            print_substituted_code(substituted_code)

def print_substituted_code(input_code: list[Union[int, frozenset[str]]]) -> None:
    printable_substituted_code: list[Union[int, str]] = []
    for number in input_code:
        if isinstance(number, frozenset):
            printable_substituted_code.append("".join(number))
        else:
            printable_substituted_code.append(number)

    print(printable_substituted_code)

# Apparently mypy doesn't catch copy.deepcopy() so I'm doing it manually
patterns, codes = read_input()
deduce_code(patterns, codes)

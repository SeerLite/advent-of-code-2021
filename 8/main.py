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


def deduce_numbers(sequence: Sequence[frozenset[str]]) -> dict[int, frozenset[str]]:
    deduced_numbers = {}
    for number in sequence:
        if len(number) == 2:
            deduced_numbers[1] = number
        elif len(number) == 4:
            deduced_numbers[4] = number
        elif len(number) == 3:
            deduced_numbers[7] = number
        elif len(number) == 7:
            deduced_numbers[8] = number

    deduced_numbers[9] = deduced_numbers[7].union(deduced_numbers[4])

    for number in sequence:
        if number in deduced_numbers.values():
            continue
        elif len(number - deduced_numbers[7]) == 3:
            deduced_numbers[3] = number
        elif len(deduced_numbers[8] - deduced_numbers[1] - number) == 0:
            deduced_numbers[6] = number

    for number in sequence:
        if number in deduced_numbers.values():
            continue
        elif len(number - deduced_numbers[6]) == 0 or len(number - deduced_numbers[4]) == 2:
            deduced_numbers[5] = number
        elif len(number - deduced_numbers[6]) == 1:
            deduced_numbers[2] = number

    for number in sequence:
        if number in deduced_numbers.values():
            continue
        elif len(deduced_numbers[8] - number) == 1:
            deduced_numbers[0] = number

    return deduced_numbers

def deduce_code(patterns: Sequence[Sequence[frozenset[str]]], codes: Sequence[Sequence[frozenset[str]]]) -> None:
    for pattern, code in zip(patterns, codes):
        # NOTE: the better way to concatenate Sequences
        # is with itertools.chain.from_iterable
        deduced_numbers = deduce_numbers(list(pattern) + list(code))

        top: Any = deduced_numbers[7].difference(deduced_numbers[1])
        top = [x for x in top][0]


        rev_deduced_numbers = {combination: number for number, combination in deduced_numbers.items()}
        substituted_code: list[Union[int, frozenset[str]]] = []
        for number in code:
            if number in rev_deduced_numbers:
                substituted_code.append(rev_deduced_numbers[number])
            else:
                substituted_code.append(number)

        if DEBUG:
            print_substituted_code(substituted_code, code)

def print_substituted_code(input_code: list[Union[int, frozenset[str]]], input_original_code: Sequence[frozenset[str]]) -> None:
    printable_substituted_code: list[Union[int, str]] = []
    for number in input_code:
        if isinstance(number, frozenset):
            printable_substituted_code.append("".join(sorted(number)))
        else:
            printable_substituted_code.append(number)


    if any(isinstance(number, frozenset) for number in input_code):
        printable_original_code: list[Union[int, str]] = []
        for number in input_original_code:
            printable_original_code.append("".join(sorted(number)))
        print(printable_substituted_code, printable_original_code)
    else:
        print(printable_substituted_code)


# Apparently mypy doesn't catch copy.deepcopy() so I'm doing it manually
patterns, codes = read_input()
deduce_code(patterns, codes)

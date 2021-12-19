from collections.abc import Sequence, MutableSequence
from collections import defaultdict
from typing import Union, Any

EXAMPLE_INPUT = True
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

    for number in sequence:
        if number in deduced_numbers.values():
            continue
        elif len(number - deduced_numbers[7]) == 2:
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

    for number in sequence:
        if number in deduced_numbers.values():
            continue
        else:
            deduced_numbers[9] = number

    return deduced_numbers

def deduce_codes(patterns: Sequence[Sequence[frozenset[str]]], codes: Sequence[Sequence[frozenset[str]]]) -> list[int]:
    substituted_codes: list[int] = []
    for pattern, code in zip(patterns, codes):
        # NOTE: the better way to concatenate Sequences
        # is with itertools.chain.from_iterable
        deduced_numbers = deduce_numbers(list(pattern) + list(code))

        rev_deduced_numbers = {combination: number for number, combination in deduced_numbers.items()}
        substituted_code: list[Union[int, frozenset[str]]] = []
        for number in code:
            if number in rev_deduced_numbers:
                substituted_code.append(rev_deduced_numbers[number])
            else:
                substituted_code.append(number)

        if DEBUG:
            print_substituted_code(substituted_code, pattern, code, deduced_numbers)

        assert all(isinstance(x, int) for x in substituted_code)
        substituted_codes.append(int("".join(str(x) for x in substituted_code)))

    return substituted_codes

def print_substituted_code(input_substituted_code: list[Union[int, frozenset[str]]], input_pattern: Sequence[frozenset[str]], input_code: Sequence[frozenset[str]], input_deductions: dict[int, frozenset]) -> None:
    printable_substituted_code: list[Union[int, str]] = []
    for number in input_substituted_code:
        if isinstance(number, frozenset):
            printable_substituted_code.append("".join(sorted(number)))
        else:
            printable_substituted_code.append(number)


    if any(isinstance(number, frozenset) for number in input_substituted_code):
        printable_pattern: list[Union[int, str]] = []
        printable_code: list[Union[int, str]] = []
        printable_deductions: dict[int, str] = {}

        for number in input_pattern:
            printable_pattern.append("".join(sorted(number)))

        for number in input_code:
            printable_code.append("".join(sorted(number)))

        for number, combination in sorted(input_deductions.items()):
            printable_deductions[number] = "".join(sorted(combination))

        print(printable_substituted_code)
        print("|", printable_pattern, printable_code)
        print("\\", printable_deductions)
    else:
        print(printable_substituted_code)


# Apparently mypy doesn't catch copy.deepcopy() so I'm doing it manually
patterns, codes = read_input()
deduced_codes = deduce_codes(patterns, codes)

if DEBUG:
    print(deduced_codes)

total_sum = sum(deduced_codes)
print(f"The sum of all output values is: {total_sum}")

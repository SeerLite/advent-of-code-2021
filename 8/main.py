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
    sequence = list(sequence)
    deduced_numbers: dict[int, frozenset[str]] = {}
    while sequence:
        combination = sequence.pop()

        if len(combination) == 2:
            number = 1
        elif len(combination) == 4:
            number = 4
        elif len(combination) == 3:
            number = 7
        elif len(combination) == 7:
            number = 8
        elif 7 in deduced_numbers and len(combination - deduced_numbers[7]) == 2:
            number = 3
        elif 8 in deduced_numbers and 1 in deduced_numbers and len(deduced_numbers[8] - deduced_numbers[1] - combination) == 0:
            number = 6
        elif (6 in deduced_numbers and len(combination - deduced_numbers[6]) == 0) or (4 in deduced_numbers and len(combination - deduced_numbers[4]) == 2):
            number = 5
        elif 6 in deduced_numbers and len(combination - deduced_numbers[6]) == 1:
            number = 2
        elif 8 in deduced_numbers and len(deduced_numbers[8] - combination) == 1:
            number = 0
        elif len(deduced_numbers) == 8:
            number = (set(range(9)) - set(deduced_numbers)).pop()
            if DEBUG:
                print(f"Number {number} deduced by process of elimination")
        elif len(sequence) > 0:
            sequence.insert(0, combination)

        deduced_numbers[number] = combination
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
            print_readable_combinations(substituted_code)

        if not all(isinstance(x, int) for x in substituted_code):
            if DEBUG:
                print_readable_combinations("|", pattern, code)
                print_readable_combinations("\\", deduced_numbers)
            assert False, "some numbers were not deduced"

        substituted_codes.append(int("".join(str(x) for x in substituted_code)))

    return substituted_codes

def print_readable_combinations(*args: Union[str, Sequence[Union[int, frozenset[str]]], dict[int, frozenset[str]]]) -> None:
    printable_args: list[Union[str, list[Union[int, str]], dict[int, str]]] = []
    for arg in args:
        if isinstance(arg, str):
            printable_args.append(arg)
        elif isinstance(arg, Sequence):
            printable_list: list[Union[int, str]] = []
            for element in arg:
                if isinstance(element, frozenset):
                    printable_list.append("".join(sorted(element)))
                else:
                    printable_list.append(element)

            printable_args.append(printable_list)
        elif isinstance(arg, dict):
            printable_dict: dict[int, str] = {}
            for number, combination in sorted(arg.items()):
                printable_dict[number] = "".join(sorted(combination))

            printable_args.append(printable_dict)

    print(*printable_args)


patterns, codes = read_input()
deduced_codes = deduce_codes(patterns, codes)

if DEBUG:
    print(deduced_codes)

total_sum = sum(deduced_codes)
if EXAMPLE_INPUT:
    assert total_sum == 61229, f"sum doesn't match with one from official example: got {total_sum}, should be 61229"

print(f"The sum of all output values is: {total_sum}")

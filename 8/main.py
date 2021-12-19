EXAMPLE_INPUT = False
DEBUG = True

def read_input() -> list[str]:
    filename = "input.example.txt" if EXAMPLE_INPUT else "input.txt"
    with open(filename) as input_file:
        pin_code_lines: list[str] = []
        for line in input_file:
            # Only get what's after the pipe character
            # NOTE: input is assumed to never split lines at
            # the pipe character, even if it's the example
            pin_code_lines.append(line.split("|")[1].strip())

        numbers: list[str] = []
        for line in pin_code_lines:
            numbers.extend(line.split())

        return numbers

def count_unique_numbers(numbers: list[str]) -> int:
    unique_numbers = 0
    for number in numbers:
        if len(number) in (2, 4, 3, 7):
            unique_numbers += 1

    return unique_numbers

numbers = read_input()
num_unique_numbers = count_unique_numbers(numbers)
print(f"Unique numbers in all PINs: {num_unique_numbers}")


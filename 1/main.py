def get_increases():
    """For part 1. Very basic and compares as it reads the file line by line."""
    with open("input.txt") as input_file:
        previous_number = int(input_file.readline())
        num_of_increases = 0
        for line in input_file:
            number = int(line)
            if number > previous_number:
                current_min = number
                num_of_increases += 1
            previous_number = number
        return num_of_increases

def get_increases_by_window():
    """For part 2. Read the whole file to RAM because it's easier to manage."""
    with open("input.txt") as input_file:
        data = [int(line) for line in input_file.read().strip().split("\n")]

    previous_sum = None
    increases = 0
    for window in zip(data, data[1:], data[2:]):
        current_sum = sum(window)
        if previous_sum is not None and current_sum > previous_sum:
            increases += 1
        previous_sum = current_sum

    return increases

print(f"Part 1, increases: {get_increases()}")
print(f"Part 2, increases by windows of 3: {get_increases_by_window()}")

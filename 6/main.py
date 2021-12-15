from typing import List

EXAMPLE_MODE = False

def read_list_from_file() -> List[int]:
    if not EXAMPLE_MODE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def pass_days(lanternfish: List[int], days: int) -> None:
    for day in range(days):
        for i in range(len(lanternfish)):
            lanternfish[i] -= 1
            if lanternfish[i] < 0:
                lanternfish[i] = 6
                lanternfish.append(8)

lanternfish = read_list_from_file()
days = 80
pass_days(lanternfish, days)
print(f"Number of lanternfish after {days} days: {len(lanternfish)}")

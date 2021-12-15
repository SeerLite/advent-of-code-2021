from typing import List

EXAMPLE = False
DEBUG = True

def read_list_from_file() -> List[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def pass_days(lanternfish_input: List[int], days: int) -> List[int]:
    lanternfish = lanternfish_input.copy()
    for day in range(days):
        for i in range(len(lanternfish)):
            lanternfish[i] -= 1
            if lanternfish[i] < 0:
                lanternfish[i] = 6
                lanternfish.append(8)
        if DEBUG:
            print(f"Day {day} out of {days} had {len(lanternfish)} lanternfish.")

    return lanternfish

lanternfish = read_list_from_file()
lanternfish_after_80 = pass_days(lanternfish, 80)
lanternfish_after_256 = pass_days(lanternfish, 256)

print(f"Number of lanternfish after 80 days: {len(lanternfish_after_80)}")
# OK I see what you're doing
print(f"Number of lanternfish after 256 days: {len(lanternfish_after_256)}")

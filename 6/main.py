from typing import List, Sequence

EXAMPLE = True
DEBUG = True

def read_list_from_file() -> List[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def pass_days(lanternfish_input: Sequence[int], days: int) -> Sequence[int]:
    if DEBUG:
        print(f"DAYS: {days}")
    lanternfish = [x for x in lanternfish_input]
    # OK so what if I immediately subtract days from all of them and then add accordingly
    for i in range(len(lanternfish)):
        if DEBUG:
            print(lanternfish[i], lanternfish[i] - days, (lanternfish[i] - days) // -6, end=" ")
        lanternfish[i] -= days
        new_lanternfish: Sequence[int] = (8,) * (lanternfish[i] // -6)
        if DEBUG:
            print(new_lanternfish)
        lanternfish += pass_days_for_new(new_lanternfish, days - 1)

    return lanternfish

def pass_days_for_new(lanternfish_input: Sequence[int], days: int) -> Sequence[int]:
    global stack
    stack += 1
    # print(stack, days)
    if days < 0:
        stack -= 1
        return lanternfish_input

    lanternfish = [x for x in lanternfish_input]
    for i in range(len(lanternfish)):
        if DEBUG and i > 3:
            print(i, days)
        # if DEBUG:
        #     print(lanternfish[i], lanternfish[i] - days, (lanternfish[i] - days) // -6)
        #     print(f"DAYSS: {days}")
        lanternfish[i] -= days
        days -= 1
        new_lanternfish = (8,) * (lanternfish[i] // -6)
        lanternfish += pass_days_for_new(new_lanternfish, days)

    stack -= 1
    return lanternfish

stack = 0

lanternfish = read_list_from_file()
lanternfish_after_days = {
    x: pass_days(lanternfish, x) for x in (3, 80)
}

for days, lanternfish_after in lanternfish_after_days.items():
    print(f"Number of lanternfish after {days} days: {len(lanternfish)}")
    print(f" The lanternfish: {lanternfish_after}")
    # OK I see what you're doing

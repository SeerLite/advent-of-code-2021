from collections.abc import Sequence, MutableSequence
from time import sleep
import math

EXAMPLE = True
DEBUG = True

def read_list_from_file() -> list[int]:
    if not EXAMPLE:
        filename = "input.txt"
    else:
        filename = "input.example.txt"

    with open(filename) as input_file:
        return [int(x) for x in input_file.read().strip().split(",")]

def visualize_days(lanternfish: Sequence[int], days: int) -> None:
    visualize_days_mathematical(lanternfish, days)
    print()
    visualize_days_imperative(lanternfish, days)
    print()

def visualize_days_mathematical(lanternfish: Sequence[int], days: int) -> None:
    lanternfish = list(lanternfish)
    children_fishes: list[int] = []
    new_lanternfish: list[int] = []
    for timer in lanternfish:
        amount_of_new_fishes = math.ceil((timer - days) / -7)
        children_fishes.append(amount_of_new_fishes)
        new_lanternfish += [8] * amount_of_new_fishes

    print(f"Mathematical: {children_fishes}")
    print(f"New fishes from mathematical: {new_lanternfish}")

# I know the mathematical way is still imperative and that I'm using
# the wrong word but I'm too lazy to change it now
def visualize_days_imperative(lanternfish: Sequence[int], days: int) -> None:
    lanternfish = list(lanternfish)
    children_fishes = [0] * len(lanternfish)
    new_lanternfish: list[int] = []
    for day in range(days):
        # print(lanternfish)
        # sleep(0.2)
        for i in range(len(lanternfish)):
            lanternfish[i] -= 1
            if lanternfish[i] < 0:
                children_fishes[i] += 1
                lanternfish[i] = 6
                new_lanternfish.append(8)

    print(f"Imperative: {children_fishes}")
    print(f"New fishes from imperative: {new_lanternfish}")

def pass_days(lanternfish_input: Sequence[int], days: int) -> list[int]:
    lanternfish = list(lanternfish_input)
    if days <= 0:
        return lanternfish
    new_lanternfish: list[int] = []
    # OK so what if I immediately subtract days from all of them and then add accordingly
    for i in range(len(lanternfish)):
        lanternfish[i] -= days
        new_fishes_in_days = math.ceil((lanternfish[i]) / -7)
        # my_range = list(range(8, 8 + new_fishes_in_days * 7, 7))
        my_range = list(range(8, 8 - new_fishes_in_days, -1))
        # new_lanternfish += (8,) * new_fishes_in_days
        new_lanternfish += my_range

    if DEBUG:
        print(new_lanternfish)

    new_lanternfish = pass_days(new_lanternfish, days - 1)
    lanternfish += new_lanternfish
    # new_lanternfish = pass_days(new_lanternfish, days - 1)
    # lanternfish += new_lanternfish

    return lanternfish


lanternfish = read_list_from_file()
# lanternfish_after_days = {
#     x: pass_days(lanternfish, x) for x in (18,)
# }

visualize_days(lanternfish, 18)
visualize_days(lanternfish, 30)

# for days, lanternfish_after in lanternfish_after_days.items():
#     print(f"Number of lanternfish after {days} days: {len(lanternfish_after)}")
#     # print(f" The lanternfish: {lanternfish_after}")
#     # OK I see what you're doing

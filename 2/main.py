from collections import namedtuple

# Coded this on my phone while traveling so it's
# probably not as thought out as it could be

# The use of namedtuple is probably unnecessary but
# I want to learn how to use it

Location = namedtuple("Location", ["position", "depth"])
def calculate_location(moves):
    depth = 0
    position = 0
    for move in moves:
        direction, amount = move.split()
        amount = int(amount)
        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        elif direction == "forward":
            position += amount

    return Location(position, depth)

def calculate_location_fixed(moves):
    aim = 0
    position = 0
    depth = 0
    for move in moves:
        command, amount = move.split()
        amount = int(amount)
        if command == "up":
            aim -= amount
        elif command == "down":
            aim += amount
        elif command == "forward":
            position += amount
            depth += aim * amount

    return Location(position, depth)

with open("input.txt") as input_file:
    moves = input_file.read().strip().split("\n")

submarine_location = calculate_location(moves)
product = submarine_location.position * submarine_location.depth

print(f"Product: {product}")

submarine_location_fixed = calculate_location_fixed(moves)
product_fixed = submarine_location_fixed.position * submarine_location_fixed.depth
print(f"Product of fixed: {product_fixed}")

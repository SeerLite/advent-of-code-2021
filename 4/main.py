# I'm gonna try to catch up to the newer puzzles as fast as possible
# so don't expect the best code.
# I'll be treating all these numbers as strings.
#
# Maybe I learn something about avoiding premature optimization.

from typing import Any, Optional

# boards = [
#     [ # board
#         {"2": False, "28": False, "33": False}, # row
#         {"11": False, "99": False, "21": False}, # row
#         {"2": False, "28": False, "33": False} # row
#     ],
#     [ # board
#         {"8": False, "9": False, "42": False} # row
#         ...
#     ]
#     ...
# ]

Board = list[dict[str, bool]]

def read_input_file() ->  tuple[str, str]:
    with open("input.txt") as input_file:
        order = input_file.readline().strip()

        # Empty line separator
        input_file.readline()

        boards = input_file.read().strip()

        return order, boards

def parse_raw_boards(raw_boards: str) -> list[Board]:
    boards = []

    # Spiltting at every double newline will split at every board
    # separation, as they're separated by empty lines
    for raw_board in raw_boards.split("\n\n"):
        board = []
        for raw_row in raw_board.split("\n"):
            row = {}
            for number in raw_row.split():
                row[number] = False
            board.append(row)
        boards.append(board)

    return boards

def board_wins_row(board: Board) -> bool:
    return any(all(row.values()) for row in board)

def board_wins_column(board: Board) -> bool:
    board_size = len(board[0])
    for column in range(board_size):
        if all(list(board[row].values())[column] for row in range(board_size)):
            return True

    return False

def pop_winning_boards(boards: list[Board]) -> Optional[list[Board]]:
    winning_indexes = []
    for i, board in enumerate(boards):
        if board_wins_row(board) or board_wins_column(board):
            winning_indexes.append(i)

    winning_boards = []
    for i in reversed(winning_indexes):
        winning_boards.append(boards[i])
        del boards[i]

    return winning_boards or None

def play_boards_until_win(boards: list[Board]) -> Optional[tuple[list[Board], int]]:
    while len(order) > 0 and not (winning_boards := pop_winning_boards(boards)):
        number = order.pop()
        for board in boards:
            for row in board:
                if number in row:
                    row[number] = True

    if winning_boards:
        return winning_boards, int(number)
    else:
        return None

def play_boards_until_last_win(boards: list[Board]) -> tuple[list[Board], int]:
    while (result := play_boards_until_win(boards)):
        last_winning_result = result
    return last_winning_result

def sum_all_unmarked(board: Board) -> int:
    sum = 0
    for row in board:
        for number, marked in row.items():
            if not marked:
                sum += int(number)

    return sum

raw_order, raw_boards = read_input_file()
order = raw_order.split(",")
order.reverse()
boards = parse_raw_boards(raw_boards)

if (result := play_boards_until_win(boards)):
    winning_boards, winning_number = result

last_winning_boards, last_winning_number = play_boards_until_last_win(boards)

first_winning_score = sum_all_unmarked(winning_boards[0]) * winning_number
last_winning_score = sum_all_unmarked(last_winning_boards[0]) * last_winning_number

print(f"Score of first winning board: {first_winning_score}")
print(f"Score of last winning board: {last_winning_score}")

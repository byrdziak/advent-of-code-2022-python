# https://adventofcode.com/2022/day/5


import os
from functions import list_to_chunks, read_file
import numpy as np
from pprint import pprint as pp
import re


def replace_many_with_empty(text: str, to_replace: str):
    for value in to_replace:
        text = text.replace(value, '')
    return text


def rows_to_crates(rows: list[str]):
    for i, row in enumerate(rows):
        no_white_spaces = row.replace(' ', '')
        if no_white_spaces:
            check = all([x.isnumeric() for x in no_white_spaces])
            if check:
                crates_end_index = i
                break

    crates = []

    for row in rows[:crates_end_index]:
        chunks = list_to_chunks(row, 4)

        row_char_list_cleared = [replace_many_with_empty(
            x, ' ][') for x in chunks]

        crates.append(row_char_list_cleared)

    matrix = np.flip(np.flip(crates, axis=1)).T.tolist()

    filtered = [list(filter(None, x)) for x in matrix]

    return {i+1: item for i, item in enumerate(filtered)}


def get_instruction_tuples(rows):
    instruction_rows = [x for x in rows if 'move' in x]

    instruction_tuples = [tuple(re.findall(r'\d+', x))
                          for x in instruction_rows]

    return instruction_tuples


def move_crates(crates: dict, instruction: tuple[int, int, int], reverse: bool):
    move_how_many = int(instruction[0])
    move_from = int(instruction[1])
    move_to = int(instruction[2])

    crate_from_length = len(crates[int(move_from)])

    crates_to_move = crates[
        move_from][crate_from_length-move_how_many:]
    if reverse:
        crates_to_move.reverse()

    crates[move_to].extend(crates_to_move)
    crates[move_from] = crates[move_from][:crate_from_length-move_how_many]

    return crates


def main():
    file = read_file('src/5_input.txt')
    rows = file.split(os.linesep)

    crates = rows_to_crates(rows)
    pp(crates)

    instruction_tuples = get_instruction_tuples(rows)  # (how many, from, to)

    for instruction in instruction_tuples:
        crates = move_crates(crates, instruction, reverse=True)

    top_stack = ''.join([v[-1:][0] for k, v in crates.items()])
    print(top_stack)

    # step 2

    crates = rows_to_crates(rows)

    for instruction in instruction_tuples:
        crates = move_crates(crates, instruction, reverse=False)

    top_stack = ''.join([v[-1:][0] for k, v in crates.items()])
    print(top_stack)


if __name__ == '__main__':
    main()

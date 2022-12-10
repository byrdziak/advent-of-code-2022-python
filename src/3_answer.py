# https://adventofcode.com/2022/day/3


import os
from functions import list_to_chunks, read_file


def decode_ascii(char: str):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38


def main():
    file = read_file('src/3_input.txt')
    rows = file.split(os.linesep)

    # rows = ['vJrwpWtwJgWrhcsFMMfFFhFp',
    #         'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    #         'PmmdzqPrVvPwwTWBwg',
    #         'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    #         'ttgJtRGJQctTZtZT',
    #         'CrZsJsPPZsGzwwsLwLmpwMDw']

    score = 0

    for row in rows:
        half_index = int(len(row)/2)
        comp1, comp2 = row[:half_index], row[half_index:]

        assert len(comp1) == len(comp2)

        comp1 = set(comp1)
        comp2 = set(comp2)

        for char in comp1:
            if char in comp2:
                score += decode_ascii(char)

    print(score)

    # step 2

    score_2 = 0

    chunks = list(list_to_chunks(rows, 3))

    for chunk in chunks:
        assert(len(chunk)) == 3
        for char in set(chunk[0]):
            if char in chunk[1] and char in chunk[2]:
                score_2 += decode_ascii(char)

    print(score_2)


if __name__ == '__main__':
    main()

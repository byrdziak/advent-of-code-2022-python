# https://adventofcode.com/2022/day/4


import os
from functions import read_file


def range_to_sections(elf_range):
    splited = elf_range.split('-')
    assert len(splited) == 2
    lower, upper = splited

    return range(int(lower), int(upper)+1)


def main():
    file = read_file('src/4_input.txt')
    rows = file.split(os.linesep)

    # part 1

    number_of_overlapping = 0

    for row in rows:
        splited = row.split(',')
        assert len(splited) == 2
        elf1_range, elf2_range = splited

        elf1_sections = range_to_sections(elf1_range)
        elf2_sections = range_to_sections(elf2_range)

        if all([x in elf2_sections for x in elf1_sections]):
            number_of_overlapping += 1
            continue
        elif all([x in elf1_sections for x in elf2_sections]):
            number_of_overlapping += 1
            continue

    print(number_of_overlapping)

    # part 2

    overlap_at_any = 0

    for row in rows:
        splited = row.split(',')
        assert len(splited) == 2
        elf1_range, elf2_range = splited

        elf1_sections = range_to_sections(elf1_range)
        elf2_sections = range_to_sections(elf2_range)

        if any([x in elf2_sections for x in elf1_sections]):
            overlap_at_any += 1
            continue
        elif any([x in elf1_sections for x in elf2_sections]):
            overlap_at_any += 1
            continue

    print(overlap_at_any)


if __name__ == '__main__':
    main()

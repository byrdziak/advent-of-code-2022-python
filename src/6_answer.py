# https://adventofcode.com/2022/day/5


import os
from functions import read_file

from pprint import pprint as pp


def main():
    file = read_file('src/6_input.txt')
    rows = file.split(os.linesep)
    input = rows[0]

    for i in range(len(input)-4):
        end_index = i+4
        test_value = input[i:end_index]
        if len(set(test_value)) == 4:
            print(end_index)
            break

    # step 2

    for i in range(len(input)-14):
        end_index = i+14
        test_value = input[i:end_index]
        if len(set(test_value)) == 14:
            print(end_index)
            break


if __name__ == '__main__':
    main()

# https://adventofcode.com/2022/day/1

import os

from functions import read_file


class Elf:
    def __init__(self, name: str, *calories: int):
        assert all(isinstance(x, int) for x in calories)
        self._calories = calories
        self._name = name

    @property
    def calories(self):
        return self._calories

    @property
    def total_calories(self):
        return sum(self._calories)

    def __str__(self):
        return f"{self._name}, calories: {self.total_calories}"


def main():
    # reading file
    file = read_file('src/1_input.txt').split(os.linesep+os.linesep)
    chunks = [x.split(os.linesep) for x in file]
    chunks_int = [[int(y) for y in x] for x in chunks]

    # step 1
    elfs = [Elf(i, *x) for i, x in enumerate(chunks_int)]
    print(max(elfs, key=lambda x: x.total_calories))

    # step 2
    elfs = sorted(elfs, key=lambda x: x.total_calories, reverse=True)
    total_calories_top_3 = sum([x.total_calories for x in elfs[:3]])
    print('Total calories top 3:', total_calories_top_3)


if __name__ == '__main__':
    main()

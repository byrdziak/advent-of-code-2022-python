# https://adventofcode.com/2022/day/2

# oponent abc | me xyz

# A X Rock - 1 point
# B Y Paper - 2 points
# C Z Scissors - 3 points

# 0 lost
# 3 draw
# 6 win

import os
from functions import read_file


def main():
    file = read_file('src/2_input.txt')
    rows = file.split(os.linesep)

    mapping = {
        'A': ('rock', 1),
        'B': ('paper', 2),
        'C': ('scissors', 3),
        'X': ('rock', 1),
        'Y': ('paper', 2),
        'Z': ('scissors', 3)
    }

    # step 1

    score = 0

    for row in rows:
        oponent, me = row.split(' ')
        oponent = mapping[oponent]
        me = mapping[me]

        loss_value = me[1]
        win_value = 6 + me[1]

        if oponent == me:
            score += 3 + me[1]
        elif oponent[0] == 'scissors' and me[0] == 'rock':
            score += win_value
        elif oponent[0] == 'scissors' and me[0] == 'paper':
            score += loss_value
        elif oponent[0] == 'rock' and me[0] == 'scissors':
            score += loss_value
        elif oponent[0] == 'rock' and me[0] == 'paper':
            score += win_value
        elif oponent[0] == 'paper' and me[0] == 'rock':
            score += loss_value
        elif oponent[0] == 'paper' and me[0] == 'scissors':
            score += win_value
        else:
            raise Exception

    print(score)

    # step 2

    # X - need to lose
    # Y - draw needed
    # Z - win needed

    score_pt2 = 0

    for row in rows:
        oponent, me = row.split(' ')
        oponent_mapped = mapping[oponent]

        if me == 'X':
            score_pt2 += 0
            if oponent == 'A':
                score_pt2 += 3
            if oponent == 'B':
                score_pt2 += 1
            if oponent == 'C':
                score_pt2 += 2
        elif me == 'Y':
            score_pt2 += 3 + oponent_mapped[1]
        elif me == 'Z':
            score_pt2 += 6
            if oponent == 'A':
                score_pt2 += 2
            if oponent == 'B':
                score_pt2 += 3
            if oponent == 'C':
                score_pt2 += 1
        else:
            raise Exception

    print(score_pt2)


if __name__ == '__main__':
    main()

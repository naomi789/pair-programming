# https://www.hackerrank.com/challenges/magic-square-forming/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pass

def is_magic(s):
    top_left_diag, top_right_diag = check_diagonals(s)
    if not top_left_diag == top_right_diag:
        return False

    s = np.array(s)
    array_width = 3

    whole_row = top_right_diag # just to make sure that diagonals are equal to rows
    for row in s:
        # print(row)
        if whole_row != sum(row):
            return False
        whole_row = sum(row)
        # print(whole_row)

    whole_col = whole_row # makes sure rows == columns
    for col_num in range(0, array_width):
        col = s[:, col_num]
        # print(col)
        if whole_col != sum(col):
            return False
        whole_col = sum(col)
        # print(whole_col)
    print('Matches all ways')
    return True


def check_diagonals(s):
    top_left_diag = sum(np.diagonal(s))
    top_right_diag = sum(np.diagonal(np.fliplr(s)))
    # print(top_left_diag)
    # print(top_right_diag)
    return top_left_diag, top_right_diag



def help_form(s, num):
    pass

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = []
#
#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))
#
#     result = formingMagicSquare(s)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


def main():
    magic_square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    print(is_magic(magic_square))

main()
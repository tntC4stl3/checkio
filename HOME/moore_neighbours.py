#!/usr/bin/python
# coding: utf-8

def count_neighbours(grid, row, col):
    surround = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    surround = [(item[0]+row, item[1]+col) for item in surround]
    len_row = len(grid)
    len_col = len(grid[0])

    count = 0
    for (row_1, col_1) in surround:
        if row_1 < 0 or row_1 >= len_row or \
            col_1 < 0 or col_1 >= len_col:
            pass
        else:
            count += grid[row_1][col_1]
    return count


# http://www.checkio.org/mission/count-neighbours/publications/gyahun_dash/python-3/first/?ordering=most_voted
def checkio_highest_vote(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))

    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"


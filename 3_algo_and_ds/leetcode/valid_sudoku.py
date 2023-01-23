"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
import math

from rich import pretty


def main(board: list[list[str]]) -> bool:
    """
    ran out of time, this solution is from the one on the site (Sep 15, 2022)
    """
    N = 9
    rows = [[] for _ in range(N)]
    columns = [[] for _ in range(N)]
    boxes = [[] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            num = board[r][c]
            if num == ".":
                continue

            if num in rows[r]:
                return False
            rows[r].append(num)

            if num in columns[c]:
                return False
            columns[c].append(num)

            box_row = (r // 3) * 3
            box_col = c // 3
            box = boxes[box_row + box_col]
            if num in box:
                return False
            box.append(num)

    return True


def test_true():
    assert (
        main(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is True
    )


def test_false():
    assert (
        main(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is False
    )


def test_false_2():
    assert (
        main(
            [
                ["7", ".", ".", ".", "4", ".", ".", ".", "."],
                [".", ".", ".", "8", "6", "5", ".", ".", "."],
                [".", "1", ".", "2", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "9", ".", ".", "."],
                [".", ".", ".", ".", "5", ".", "5", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ]
        )
        is False
    )

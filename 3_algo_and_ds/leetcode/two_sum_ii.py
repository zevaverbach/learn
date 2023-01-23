"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


def main(numbers: list[int], target: int) -> tuple[int, int]:
    ...


def test_one():
    assert main([2,7,11,15], 9) == [1, 2]


def test_two():
    assert main(numbers = [2,3,4], target = 6) == [1, 3]


def test_three():
    assert main(numbers = [-1,0], target = -1) == [1, 2]



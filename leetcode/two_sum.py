"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def main(nums: list[int], target: int) -> list[int]:
    mates = {}
    for ix, num in enumerate(nums):
        if num in mates:
            return sorted([mates[num], ix])
        mates[target - num] = num
    raise Exception


def test_one():
    return main([2,7,11,15], 9) == [0, 1]


def test_two():
    return main([1, 3, 5, 7], 10) == [1, 3]


def test_three():
    return main([9, 8, 5, 2, 0], 5) == [2, 4]

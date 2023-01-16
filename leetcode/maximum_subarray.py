"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Ran out of time on this one (Sep 14, 2022), the below is what I implemented after reading the _description_ of the first O(n) solution.
"""

def main(nums: list[int]) -> int:
    current_sum = nums[0]
    largest_sum = current_sum

    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        largest_sum = max(current_sum, largest_sum)

    return largest_sum


def test_one():
    assert main([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_again():
    assert main([1,2,-1,-2,2,1,-2,1,4,-5,4]) == 6


def test_two():
    assert main([5,4,-1,7,8]) == 23


def test_three():
    assert main([1]) == 1


def test_four():
    assert main([-2,1]) == 1


def test_five():
    assert main([-2,-3,-1]) == -1

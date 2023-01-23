"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""


def main(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    prev_num = nums[0]
    current_streak_prod = prev_num
    max_ = prev_num
    max_single_val = prev_num
    for num in nums[1:]:
        current_streak_prod *= num
        if current_streak_prod > max_:
            max_ = current_streak_prod
        if num > max_single_val:
            max_single_val = num
        prev_num = num
    return max_ if max_ > max_single_val else max_single_val



def test_one():
    assert main([2,3,-2,4]) == 6


def test_two():
    assert main([-2,0,-1]) == 0


def test_three():
    assert main([-3,-1,-1]) == 3


def test_forr():
    assert main([-3]) == -3


def test_five():
    assert main([0, 2]) == 2


def test_six():
    assert main([2,-5,-2,-4,3]) == 24

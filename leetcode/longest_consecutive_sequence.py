"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


def main(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    nums = sorted(nums)
    longest = 1
    current_streak = 1
    prev_num = nums[0]
    for num in nums[1:]:
        diff = num - prev_num 
        if diff == 1:
            current_streak += 1
            if current_streak > longest:
                longest = current_streak
        elif diff == 0:
            continue
        else:
            current_streak = 1
        prev_num = num

    return longest


def test_one():
    assert main([5, 1, 2, 9, 11]) == 2


def test_two():
    assert main([3, 4, 5, 1, 2, 9, 11]) == 5


def test_three():
    assert main([3, 4, 5, 1, 2, 8, 9, 10, 11]) == 5


def test_negative():
    assert main([4, 3, -10, -9, -8, -7, 1, 2, 3]) == 4


def test_five():
    assert main([1,2,0,1]) == 3

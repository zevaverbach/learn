"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
import collections as c


def main(nums: list[int]) -> list[list[int]]:
    triplets = []
    lu = c.defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            missing = -(nums[i] + nums[j])
            if missing in lu:
                for ix in lu[missing]:
                    if ix not in (i, j):
                        triplets.append(sorted([i, j, ix]))
            else:
                lu[missing].append(


def test_one():
    assert main([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]


def test_two():
    assert main([0,1,1]) == []

def test_three():
    assert main([0, 0, 0]) == [[0,0,0]]

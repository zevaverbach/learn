"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
import collections as c


def main(nums: list[int], k: int) -> list[int]:
    buckets = []
    for _ in range(len(nums) + 1):
        buckets.append([])

    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num, count in counter.items():
        buckets[count].append(num)

    most_freq = []

    for count in range(len(nums), 1, -1): 
        for num in buckets[count]:
            most_freq.append(num)
            if len(most_freq) == k:
                break

    return most_freq



def test_one():
    assert main([1, 2, 3, 4, 4], 1) == [4]


def test_two():
    assert main([1, 2, 3, 4, 4, 2], 1) in ([4], [2])


def test_three():
    assert sorted(main([1, 1, 1, 2, 3, 4, 4, 2], 2)) in ([1, 2], [1, 4])


def test_four():
    assert sorted(main([1, 1, 1, 2, 3, 4, 4, 2], 3)) == [1, 2, 4]


def test_five():
    assert sorted(main([1, 2, 3, 4, 1, 2, 3, 4, 5], 4)) == [1, 2, 3, 4]



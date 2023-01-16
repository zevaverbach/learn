import collections


# def main(nums: list[int], k: int) -> list[int]:
#     """
#     Given an integer array `nums` and an integer `k`, return the k most frequent elements. 
#     You may return the answer in any order.

#     time: 11 mins
#     """
#     num_counts = collections.defaultdict(int)
#     for num in nums:
#         num_counts[num] += 1
#     num_count_tups = tuple(num_counts.items())
#     sorted_num_count_tups = sorted(num_count_tups, key=lambda tup: tup[1], reverse=True)
#     return [i[0] for i in sorted_num_count_tups[:k]]

# def main(nums: list[int], k: int) -> list[int]:
#     """
#     Given an integer array `nums` and an integer `k`, return the k most frequent elements. 
#     You may return the answer in any order.

#     time: 5 mins
#     """
#     c = collections.Counter(nums)
#     return [i[0] for i in c.most_common(k)]


def main(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array `nums` and an integer `k`, return the k most frequent elements. 
    You may return the answer in any order.

    bucket sort, introduced by neetcode video
    """
    if len(nums) == k:
        return nums
    buckets = [[] for _ in range(len(nums) + 1)]
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    for num, count in counter.items():
        buckets[count].append(num)

    most_freq = []

    for i in range(len(nums), 0, -1):
        if len(most_freq) == k:
            return most_freq
        for item in buckets[i]:
            most_freq.append(item)
    return most_freq



def test_one():
    assert main([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_two():
    assert main(nums = [1], k = 1) == [1]


def test_three():
    assert main(nums = [1, 2], k = 2) == [1, 2]

def test_four():
    assert main(nums = [-1, -1], k = 1) == [-1]

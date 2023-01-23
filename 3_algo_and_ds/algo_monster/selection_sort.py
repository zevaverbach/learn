

def selection_sort(nums: list[int]) -> list[int]:
    """
    find the smallest num and swap it with the first num, rinse and repeat

    O(n^2)
    """
    index_smallest_num = 0
    for idx, num in enumerate(nums):
        if num < nums[index_smallest_num]:
            index_smallest_num = idx




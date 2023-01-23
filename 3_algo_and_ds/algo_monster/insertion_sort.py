def insertion_sort(nums: list[int]) -> list[int]:
    """
    for each num in nums[1:], swap it with the num before it if it's smaller

    O(n^2) because it has a nested loop (average- and worst-case)
    best case: O(n)
    """
    for idx in range(len(nums)):
        # O(n)
        current = idx
        while current and nums[current] < nums[current - 1]:
            # O(n - 1) since we're skipping the first element
            # on average, nums[current] will be less than nums[current - 1] 50% of the time,
            #   so O(n) * .5
            # on average, this swap will occur midway through the array, 
            #   so `O(n -1) * .5` which simplifies to O(n) * .5
            nums[current], nums[current - 1] = nums[current - 1], nums[current]
            current -= 1
    # O(n) * .5 * O(n) * .5 ==> O(n^2) * .25 ==> O(n^2)
    return nums

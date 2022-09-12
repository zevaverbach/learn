def main(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    products = []
    for num in nums:



def test_one():
    assert main([-1,1,0,-3,3]) == [0,0,9,0,0]


def test_one()
    assert main([1,2,3,4]) == [24,12,8,6]

# def main(nums: list[int]) -> list[int]:
#     """
#     Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#     You must write an algorithm that runs in O(n) time and without using the division operation.

#     This answer fails the log(N) requirement and runs out of time on Leetcode.
#     """
#     answer = []
#     for idx in range(len(nums)):
#         answer.append(math.prod([num for ix, num in enumerate(nums) if ix != idx]))
            
#     return answer


def main(nums: list[int]) -> list[int]:
    """
    I read the description of solution 1 on LC without reading the implementation.

    Then I copied the solution, as mine was still hitting against the time limit.
    """
    length = len(nums)
    L = [0] * length
    R = [0] * length
    L[0] = 1
    R[-1] = 1
    print(nums)
    for idx in range(1, length):
        L[idx] = nums[idx - 1] * L[idx - 1]
        print(nums[idx - 1])
    print()
    for idx in reversed(range(length - 1)):
        R[idx] = nums[idx + 1] * R[idx + 1]
        print(nums[idx + 1])
    answer = []
    for idx in range(length):
        answer.append(L[idx] * R[idx])
    return answer



def test_one():
    assert main([-1,1,0,-3,3]) == [0,0,9,0,0]


def test_two():
    assert main([1,2,3,4]) == [24,12,8,6]

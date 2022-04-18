"""
Given a list of integers and a single sum value,
return indices of elements in array that sum up to sum value
Example: sum_indices_simple([10, 5, 2, 3, 7, 5], 10) -> [1, 5]
"""


def sum_indices_simple(nums, target_sum):
    """
    Approach: Brute force, O(n ^ 2)
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                return [i, j]

    return [-1, -1]

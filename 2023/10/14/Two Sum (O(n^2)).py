from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    :param nums: list of integer numbers
    :param target: number for sum of nums
    :return: list of indexes of numbers for target sum

    """
    for i in range(0, len(nums) + 1 // 2):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
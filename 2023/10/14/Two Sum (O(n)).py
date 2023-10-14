from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    :param nums: list of integer numbers
    :param target: number for sum of nums
    :return: list of indexes of numbers for target sum

    """
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

    return []


print(two_sum(nums=[3, 2, 4], target=6))

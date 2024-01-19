# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# 33. Search in Rotated Sorted Array
from typing import List


def bs_rotated(nums, target):
    def bs(lst, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if lst[mid] < target:
            return bs(lst, mid + 1, end)
        elif lst[mid] > target:
            return bs(lst, start, mid - 1)
        else:
            return mid

    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    added = nums + nums[:left]

    result = bs(added, left, len(added) - 1)
    return result if result == -1 else result % len(nums)
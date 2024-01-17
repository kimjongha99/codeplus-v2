# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

        for i in nums:
            print(i,end=",")
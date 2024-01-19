# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 167. Two Sum II - Input Array Is Sorted
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right =len(numbers)-1

        while left<right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]


            elif current_sum < target:
                left += 1
            else:
                right -= 1




sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Expected output: [1,2]
print(sol.twoSum([2,3,4], 6))      # Expected output: [1,3]
print(sol.twoSum([-1,0], -1))      # Expected output: [1,2]

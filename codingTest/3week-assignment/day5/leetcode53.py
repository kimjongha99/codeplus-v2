# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0] #nums의 첫 번째 요소로 dp 배열을 초기화합니다

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # dp[i-1] +num[i] 와  num[i]를 비교하여 최대값을 찾는 라인

        return max(dp)

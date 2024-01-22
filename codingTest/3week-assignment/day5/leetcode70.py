# https://leetcode.com/problems/climbing-stairs/
# 계단오르기


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def calculate_ways(steps):  #동일한 단계 수에 대해 경로 수를 다시 계산하지 않도록 memo에 저장
            if steps in memo:
                return memo[steps]
            memo[steps] = calculate_ways(steps - 1) + calculate_ways(steps - 2)
            return memo[steps]

        return calculate_ways(n)

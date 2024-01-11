# Subsets
# 부분 집합 https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  #결과물을 넣을 result 초기화

        def dfs(index, path):
            result.append(path) # 일단 첫번째 경로를 넣음

            for i in range(index, len(nums)): # 0부터 nums 끝까지 반복
                dfs(i + 1, path + [nums[i]])  #재귀적으로 dfs  호출은 현재 요소를 path에 추가하고, 다음 요소로 이동합니다 (i + 1).


        dfs(0, [])
        return result


sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))

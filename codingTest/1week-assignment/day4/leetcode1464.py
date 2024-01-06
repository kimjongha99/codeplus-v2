import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)  # 힙으로 변환해줘야 함
        n = len(nums)
        for _ in range(n-2):
            heapq.heappop(nums)

        n1= heapq.heappop(nums)
        n2= heapq.heappop(nums)

        return (n1-1) * (n2-1)



if __name__ == "__main__":
    nums =[10,2,5,2]
    sol = Solution()
    result = sol.maxProduct(nums)
    print("Output:", result)

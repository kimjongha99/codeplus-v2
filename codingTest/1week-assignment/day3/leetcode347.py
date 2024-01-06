from collections import Counter
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        ans2 = num_counts.most_common(k)
        result =[]
        for i in ans2:
            result.append(i[0])

        return result



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    print("Output:", result)

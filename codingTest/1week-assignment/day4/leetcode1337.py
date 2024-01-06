import heapq  #1337. The K Weakest Rows in a Matrix
from typing import List

#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
    #2차원 배열에서의 1은 군인  0 은 민간인
    # 행렬에서  한 행의 군인의 수 얼마나 많은지

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for index, row in enumerate(mat):
            soldier_count = sum(row)
            heapq.heappush(heap, (soldier_count, index))

        # Extract the indices of the k weakest rows
        min_list = [0] * k
        for i in range(k):
            _, index = heapq.heappop(heap)  # Pops the tuple and unpacks it
            min_list[i] = index

        return min_list








if __name__ == "__main__":
    mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
    k = 2
    sol = Solution()
    result = sol.kWeakestRows(mat,k)
    print("Output:", result)

#배열에서 K번째로 큰 요소
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 이문제는 최소 힙 만들고
        # len(heap) -k 해서 나온 값만큼 힙을 pop 하고 남은 heap[0]이 정답
        heap =[]  # 힙을 초기화해준다.

        for num in nums:
            heapq.heappush(heap, num)

        n = len(heap)-k
        for i in range(n):
            heapq.heappop(heap)


        return heap[0]

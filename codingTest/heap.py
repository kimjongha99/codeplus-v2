import heapq

heap =[]  # 힙을 초기화해준다.



heapq.heappush(heap,10)
print(heap)
heapq.heappush(heap, 1)
print(heap)
heapq.heappush(heap, 5)
print(heap)


# 가장 작은 요소를 뺴보자
small_heap= heapq.heappop(heap)
print(small_heap)

#그럼 이제 5, 10 이남게 된다.
print(heap)



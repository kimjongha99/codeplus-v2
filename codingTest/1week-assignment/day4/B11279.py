import heapq
import sys

tc = int(sys.stdin.readline())

heap=[]
for _ in range(tc):
    num = int(sys.stdin.readline())

    if num == 0:
        if heap:
            change_num=heapq.heappop(heap)
            print(-change_num)
        else:
            print('0')
    else:
        heapq.heappush(heap,-num)

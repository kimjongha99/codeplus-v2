import heapq
import sys

tc = int(sys.stdin.readline())

heap = []

for _ in range(tc):
    num = int(sys.stdin.readline())    #int(input) 하면 시간초과
    


    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')
    else:
        heapq.heappush(heap, num)

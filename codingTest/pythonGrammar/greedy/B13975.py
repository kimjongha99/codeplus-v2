#https://www.acmicpc.net/problem/13975
#파일 합치기3
from heapq import heapify, heappop, heappush

tc = int(input())

for _ in range(tc):
    n = int(input())
    file =list(map(int,input().split()))
    heapify(file)
    ans= 0
    for _ in range(n-1):
        a = heappop(file)
        b = heappop(file)
        ans += a+b
        heappush(file,a+b)
    print(ans)

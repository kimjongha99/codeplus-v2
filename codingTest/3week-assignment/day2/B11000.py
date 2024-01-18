# https://www.acmicpc.net/problem/11000
#
# 강의실 배정
import heapq

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int,input().split(' '))))

print(time)
time.sort(key=lambda x : (x[0],x[1])) # 0번순으로 정렬하고 같으면 1번순으로?

print(time)

heap = [time[0][1]] # 힙에 첫 번째 강의의 끝나는 시간을 저장

for i in range(1,N):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap) # 현재 강의의 시작 시간이 지금힙 시작시간 보다 크거나 같으면, 힙에서 해당 시간을 제거
    heapq.heappush(heap,time[i][1]) # 현재 강의의 끝나는 시간을 힙에 추가


print(len(heap)) # 힙의 크기 출력 (필요한 최소 강의실의 수)
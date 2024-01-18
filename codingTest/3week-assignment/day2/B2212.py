# 센서
# https://www.acmicpc.net/problem/2212


import sys
input = sys.stdin.readline

n = int(input())  # 센서 개수
k = int(input())  # 집중국 개수
sensors = list(map(int, input().split()))  # 센서 좌표
sensors.sort()

# 센서 간 거리 리스트 생성 및 내림차순 정렬
dist = list(sensors[i] - sensors[i - 1] for i in range(1, n))
dist.sort(reverse=True)

# 센서 간 거리가 가장 먼 k-1개를 제외하고 나머지 거리의 합 출력
print(sum(dist[k-1:]))
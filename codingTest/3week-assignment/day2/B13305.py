# https://www.acmicpc.net/problem/13305
# 주유소


n = int(input())  # 도시의 개수

load = list(map(int, input().split()))  # 거리

city = list(map(int, input().split())) # 도시의 주유 비용


res =0

c = city[0]  # 0번째의 도시 비용을 가져옴

for i in range(n-1):  #반복을하면서
    if c>city[i]: # 첫번째 도시의 비용이  i번째 비용보다 크면
        c=city[i] # c에 i번째 도시의 비용을 넣고
    res += c*load[i] # res에 c 에 해당하는 길이를 곱해준다.

print(res)
# https://www.acmicpc.net/problem/1931
# 회의실 배정


n = int(input())

meeting = [tuple(map(int,input().split())) for _ in range(n)]

meeting.sort(key=lambda x: (x[1], x[0]))

ans =0
now =0

for start, end in meeting:
    if now<=start:
        now = end
        ans+=1

print(ans)

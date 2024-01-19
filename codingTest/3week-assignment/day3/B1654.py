#https://www.acmicpc.net/problem/1654
#랜선자르기


k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

max_length = max(lan)
min_length = 1  # 최소 길이를 0이 아닌 1로 설정

while min_length < max_length:
    mid = (max_length + min_length) // 2
    count = sum(lan_length // mid for lan_length in lan)

    if count < n:
        max_length = mid
    else:
        min_length = mid + 1

print(min_length - 1)
# https://www.acmicpc.net/problem/2108
# 통계힉
import sys
from collections import Counter

# 입력 받기
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
#답
result=[0]*4
numbers.sort()
num_sum=0
for i in numbers:
    num_sum+=i
result[0]=round(num_sum/N)
#중간값
result[1]=numbers[N//2]




counter = Counter(numbers)# 숫자 빈도 계산

max_freq = max(counter.values()) # 최대빈도찾기

modes = []
for num, freq in counter.items():
    if freq == max_freq:
        modes.append(num)  # 최대 빈도를 찾으면 modes에 저장

modes.sort() #정렬

if len(modes) == 1:
    result[2] = modes[0]
else:
    result[2] = modes[1]

    # 범위
result[3] = abs(numbers[-1] - numbers[0])

for i in result:
    print(i)
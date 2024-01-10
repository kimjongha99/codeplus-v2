
# https://www.acmicpc.net/problem/15903
# 카드 합체 놀이



input_data = input()
n, m = map(int, input_data.split())

nums =[]

nums += map(int, input().split())

nums.sort()

for _ in range(m):
    n1 = nums.pop(0)
    n2 = nums.pop(0)
    sum = n1 + n2
    nums.append(sum)
    nums.append(sum)
    nums.sort()

sum=0

for n in nums:
    sum+=n


print(sum)
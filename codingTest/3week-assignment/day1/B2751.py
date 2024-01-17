# https://www.acmicpc.net/problem/2751
# 수 정렬하기2

n = int(input())

arr = [0]*n

for i in range(n):
    arr[i] = int(input())

arr.sort()

for i in arr:
    print(i)
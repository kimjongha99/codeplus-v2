# https://www.acmicpc.net/problem/21921

# 블로그

N, X = map(int, input().split())

arr = list(map(int, input().split()))

windowSum = 0
maxSum = 0
count = 0

for i in range(len(arr)):
    windowSum += arr[i]
    if i >= X - 1:
        if maxSum == windowSum:
            count += 1
        elif windowSum > maxSum:
            count = 1

        maxSum = max(windowSum, maxSum)
        windowSum -= arr[i - (X - 1)]

if maxSum == 0:
    print("SAD")
else:
    print(maxSum)
    print(count)

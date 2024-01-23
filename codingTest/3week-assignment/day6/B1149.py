# https://www.acmicpc.net/problem/1149
# RGB거리


t =int(input())

arr = []

for _ in range(t):
    arr.append(list(map(int,input().split())))


print(arr)

dp = [[0]*3 for _ in range(t)]

print(dp)

dp[0] = arr[0]

print(dp)

for i in range(1, t):
    dp[i][0]= min(dp[i-1][1], dp[i-1][2])+arr[i][0]
    dp[i][1]= min(dp[i-1][0], dp[i-1][2])+arr[i][1]
    dp[i][2]= min(dp[i-1][0], dp[i-1][1])+arr[i][2]


print(min(dp[t-1]))

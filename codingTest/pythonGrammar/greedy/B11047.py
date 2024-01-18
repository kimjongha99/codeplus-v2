#https://www.acmicpc.net/problem/11047

#동전

n , money = map(int,input().split())
coins=[int(input()) for _ in range(n)]


ans =0
for  i in range(n-1, -1, -1):
    ans += money//coins[i]
    money %= coins[i]
print(ans)
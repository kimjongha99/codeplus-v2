# https://www.acmicpc.net/problem/11399
# ATM


n = int(input())

atm = list(map(int,input().split()))

atm.sort() # 입력받은값 정렬
ans=0
for i in range(len(atm)):
    sequence_sum = sum(atm[0:i + 1]) #1번부터 N번까지 더하고
    ans+=sequence_sum # 추가 반복

print(ans)
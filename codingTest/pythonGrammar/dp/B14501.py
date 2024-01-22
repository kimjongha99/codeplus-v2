# https://www.acmicpc.net/problem/14501
# 퇴사


N = int(input())
table = []
for _ in range(N):
    t, p = map(int, input().split())
    table.append((t, p))


print(table)

max_val = 0
def dp(idx, pay):
    global max_val
    if idx >= N:
        if pay > max_val:
            max_val = pay
        return

    t, p = table[idx]

    for i in range(2):
        if i == 1:
            if idx + t > N:
                return
            dp(idx + t, pay + p)
        else:
            dp(idx + 1, pay)
dp(0, 0)
print(max_val)
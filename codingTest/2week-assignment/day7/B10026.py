#https://www.acmicpc.net/problem/10026
#적녹색약


import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한을 늘림


def dfsR(row, col):
    visited[row][col] = True
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 'R':
            dfsR(nx, ny)

def dfsB(row, col):
    visited[row][col] = True
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 'B':
            dfsB(nx, ny)

def dfsG(row, col):
    visited[row][col] = True
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 'G':
            dfsG(nx, ny)

def dfsRG(row, col):
    visited[row][col] = True
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
            dfsRG(nx, ny)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


ans = 0
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            if graph[row][col] == 'R':
                dfsR(row, col)
                ans += 1
            elif graph[row][col] == 'B':
                dfsB(row, col)
                ans += 1
            elif graph[row][col] == 'G':
                dfsG(row, col)
                ans += 1

visited = [[False] * n for _ in range(n)]
ans2 = 0
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            if graph[row][col] == 'B':
                dfsB(row, col)
                ans2+=1
            else:
                dfsRG(row, col)
                ans2 += 1

print(ans, ans2)
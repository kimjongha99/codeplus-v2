# https://www.acmicpc.net/problem/11725
# 트리에 부모찾기

def dfs(curr_idx):
    visited[curr_idx] = True

    for i in range(len(graph[curr_idx])):
        next_idx = graph[curr_idx][i]
        if visited[next_idx] == False:
            answer[next_idx] = curr_idx
            dfs(next_idx)


N = int(input())

graph = [None] * (N + 1)
for i in range(1, N + 1):
    graph[i] = []

visited = [False] * (N + 1)
answer = [0] * (N + 1)

for i in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)


for i in range(2,len(answer)):
    print(answer[i])

for i in range(1, N + 1):
    print(f"Node {i}: {graph[i]}")

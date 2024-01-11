com = int(input())
n = int(input())

visited = [0] * (com + 1)
graph = [[] for _ in range(com + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global count
    visited[start] = 1
    count += 1

    for i in graph[start]:
        if visited[i]==0:
            dfs(i)


count = 0
dfs(1)

print( count - 1)

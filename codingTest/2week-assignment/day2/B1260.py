from collections import deque

n ,m ,k = map(int,input().split())


visited = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]  # 그래프를 초기화


for _ in range(m):
    x , y = map(int,input().split())
    graph[x][y]=graph[y][x]=1


def dfs(k):
    visited[k]=1
    print(k, end=' ')
    for i in range(1,n+1):
        if visited[i]==0 and graph[k][i]==1:
            dfs(i)


dfs(k)
print()


def bfs(k):
    visited2=[0]*(n+1)
    queue = deque()
    queue.append(k)
    visited2[k]=1

    while queue:
        idx = queue.popleft()
        print(idx , end=" ")
        for i in range(1,n+1):
            if visited2[i]==0 and graph[idx][i]==1:
                queue.append(i)
                visited2[i]=1


bfs(k)
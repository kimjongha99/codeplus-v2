#https://www.acmicpc.net/problem/7562
#나이트 이동하기
from collections import deque

tc =int(input())


def bfs(x, y, x1, y1):
    dx = [-2, -2, -1, 1, 2, 2, -1, 1]
    dy = [1, -1, 2, 2, -1, 1, -2, -2]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        current_x, current_y, moves = queue.popleft()

        if current_x == x1 and current_y == y1:
            return moves

        for i in range(8):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1
for _ in range(tc):
    n = int(input())
    visited =[[False]*n for _ in range(n)]

    x , y = map(int,input().split())

    x1, y1 = map(int,input().split())

    print(bfs(x,y,x1,y1))



# 검정색 영역 구하기
# 2차월배열입력받기
from collections import deque

n = 5
grid = []
count = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(n):
    row = list(map(int, list(input())))
    grid.append(row)


def bfs(x, y):
    q = deque()
    q.append([x,y])
    grid[x][y]=0
    level =0
    while q:
        n= len(q)
        for i in range(n):
            x, y = q.popleft()
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if nx>=0 and nx < 5 and ny >=0 and ny<5 and grid[nx][ny]==1:
                    q.append([nx,ny])
                    grid[nx][ny]=0
        level+=1

for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            count+=1  
            bfs(i,j)




print(count)

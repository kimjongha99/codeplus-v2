# 검정색 영역 구하기
# 2차월배열입력받기

n = 5
grid = []
count = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(n):
    row = list(map(int, list(input())))
    grid.append(row)


def dfs(row, col):
    grid[row][col] = 0
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            dfs(nx, ny)


for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            count += 1
            dfs(row, col)

print(count)

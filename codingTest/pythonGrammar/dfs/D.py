#DFS를 이용해서 픽셀수 구하기
# 5
# 11100
# 00000
# 00000
# 00001
# 00001

# [3,2]
n = int(input())
grid = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = []
count = 0

def dfs(row, col):
    global count

    grid[row][col] = 0
    count += 1

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n and grid[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(n):
    input_row = list(map(int, input()))  # Changed variable name from 'row' to 'input_row'
    grid.append(input_row)

for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            count = 0
            dfs(row, col)
            ans.append(count)

print(ans)

def dfs(row, col):
    global countPerDanji
    visited[row][col] = True
    countPerDanji += 1

    # Directions: up, down, right, left
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        newX = row + dx[i]
        newY = col + dy[i]

        if 0 <= newX < n and 0 <= newY < n:
            if map[newX][newY] == 1 and not visited[newX][newY]:
                dfs(newX, newY)

n = int(input())
map = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    row_num = input()
    row_value = [int(i) for i in row_num]
    map.append(row_value)

countList = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            countPerDanji = 0
            dfs(i, j)
            countList.append(countPerDanji)


print(len(countList))
for count in sorted(countList):
    print(count)
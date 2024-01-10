def island_dfs_stack(grid):
    dx = [0,0 ,-1,1]
    dy = [1,-1,0,0]
    rows , cols = len(grid),len(grid[0])
    cnt =0;


    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue # 1이아니라면 계속 반복

            cnt +=1 # 1이라면 +1 하고 dfs타자
            stack = [(row,col)]

            while stack: #스택이 존재하면 반복
                x,y = stack.pop()
                grid[x][y]='0'
                for i in range(4):
                    nx= x+dx[i]
                    ny= y+dy[i]
                    if nx<0 or ny <0 or nx >=rows or ny >= cols or grid[nx][ny] !='1':
                        # nx가 0보다 작거나 ny가 0보다 작은 경우, 즉 그리드의 범위를 벗어난 경우
                        # 또는 nx가 행의 수보다 크거나 같거나 ny가 열의 수보다 크거나 같은 경우, 즉 그리드의 범위를 벗어난 경우
                        # 또는 grid[nx][nx]가 '1'이 아닌 경우
                        continue
                    stack.append((nx,ny))

        return cnt



    assert island_dfs_stack(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1
    assert island_dfs_stack(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
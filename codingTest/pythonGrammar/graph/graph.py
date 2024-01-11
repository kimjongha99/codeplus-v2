# 정점과 정점을 선으로만 연결하는것이 무방향 그래프


edge = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4]]


graph = [[0] * 1 for _ in range(6)]




SIZE = 5

adjList = [[0] for _ in range(SIZE)]

print(adjList)

SIZE = 5
adjList = []
for i in range(SIZE):
    inner_list = [0]
    adjList.append(inner_list)

print(adjList)


ROW_SIZE = 5
COL_SIZE = 7

adjMatrix = [[0 for _ in range(COL_SIZE)] for _ in range(ROW_SIZE)]
print(adjMatrix)


ROW_SIZE = 5
COL_SIZE = 7
adjMatrix = []
for i in range(ROW_SIZE):
    inner_list = []
    for j in range(COL_SIZE):
        inner_list.append(0)
    adjMatrix.append(inner_list)

print(adjMatrix)
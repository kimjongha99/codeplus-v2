cnt =0
#인접 리스트


def dfs(start , graph,visited,n):
    global cnt

    visited[start] =1
    cnt+=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i,graph,visited,n)




def solution(n, edges):
    global cnt
    visited = [0]*(n+1)
    graph =[[] for _ in range(n+1)]
    for [a,b] in edges:
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    dfs(1,graph,visited,n)

    return n-cnt


print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))


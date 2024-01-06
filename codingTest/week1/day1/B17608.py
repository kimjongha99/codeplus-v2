from sys import stdin

def solution(arr):
    answer = 0
    maxN = -1

    for i in range(len(arr)-1,-1,-1):
        if(arr[i]>maxN):
            answer+=1;
            maxN = arr[i]






    return answer


input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))



print(solution(arr))
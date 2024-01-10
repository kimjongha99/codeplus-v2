# n! 구하기
# 재귀함수를 이용해서 한번 풀어보자

# 매개변수가 5라면 5!을 구하기


n = int(input())


def dfs(n):
    if n ==1:
        return 1
    else:
        return n*dfs(n-1)


print(dfs(n))









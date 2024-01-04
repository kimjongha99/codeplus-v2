from sys import stdin


def solution(str):
    stack = []

    for s in str:
        if s == '(':  # 열린 괄호를 만나면 스택에 추가
            stack.append(s)
        elif s == ')':  # 닫힌 괄호를 만나면
            if not stack:  # 스택이 비어있으면 균형이 맞지 않음
                return "NO"
            if stack[-1] == '(':  # 스택의 마지막이 열린 괄호면 짝이 맞으므로 pop
                stack.pop()
            else:  # 짝이 맞지 않으면
                return "NO"
    # 모든 검사 후 스택이 비어있으면 균형이 맞는 것
    return "YES" if not stack else "NO"



input = stdin.readline



n = int(input())
str = ''
for i in range(n):
    str = input()
    print(solution(str))



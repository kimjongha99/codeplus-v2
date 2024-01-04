from sys import stdin

input = stdin.readline


tc = int(input())

for _ in range(tc):
    str = input()
    stack = []
    balanced =True  # 괄호가 맞는지


    for s in str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:  # 스택이 비어있을때
                print("NO")
                balanced = False
                break
            if stack[-1]=='(':
                stack.pop()
            else:
                print("NO")
                balanced=False
                break
    if balanced and not stack:  # Check if parentheses are balanced and stack is empty
        print("YES")
    elif balanced:
        print("NO")



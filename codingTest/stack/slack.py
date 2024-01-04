def solution():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.pop()
    print(stack,"1")
    print(stack[-1],"스택 젤위에있는거 확인")
    print(len(stack) == 0)  # 스택이 비어있는지 확인

    return stack



solution()


while True:
    input_data = input()
    if input_data =='.':
        break


    stack = []
    good = True

    for s in input_data:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                good = False
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                good = False
                break

    if good and not stack:
        print('yes')
    else:
        print('no')

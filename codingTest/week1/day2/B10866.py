from collections import deque
from sys import stdin

input = stdin.readline

tc = int(input().strip())

deque1 = deque()

for _ in range(tc):
    command_line = input().strip().split()
    command = command_line[0]

    if command == "push_back":
        n = int(command_line[1])
        deque1.append(n)

    elif command == "push_front":
        n = int(command_line[1])
        deque1.appendleft(n)

    elif command == "front":
        if deque1:
            print(deque1[0])
        else:
            print(-1)

    elif command == "back":
        if deque1:
            print(deque1[-1])
        else:
            print(-1)

    elif command == "pop_front":
        if deque1:
            print(deque1.popleft())
        else:
            print(-1)

    elif command == "pop_back":
        if deque1:
            print(deque1.pop())
        else:
            print(-1)

    elif command == "size":
        print(len(deque1))

    elif command == "empty":
        print(0 if deque1 else 1)
from collections import deque


def solution():
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    queue.popleft()
    print(queue)




solution()
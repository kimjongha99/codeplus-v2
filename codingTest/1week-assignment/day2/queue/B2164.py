from collections import deque
from sys import stdin

def solution(n):
    queue = deque(range(1, n + 1))
    print("초기 큐:", list(queue))

    while len(queue) > 1:
        discarded = queue.popleft()
        print("버린 상위 카드:", discarded)
        print("버린 후 큐:", list(queue))

        if queue:  # 다시 팝하기 전에 대기열이 비어 있지 않은지 확인
            moved_card = queue.popleft()
            queue.append(moved_card)
            print("새 상위 카드 아래로 이동:", moved_card)
            print("이동후 큐:", list(queue))

    print("라스트 남은카드:", queue[0])
    return queue[0]




input = stdin.readline

n = int(input())

print(solution(n))
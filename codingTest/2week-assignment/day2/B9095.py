from collections import deque

def find(n):
    queue = deque()  # BFS를 위한 큐 생성
    queue.append(0)  # 합계를 0으로 시작
    ways = 0  # 방법의 수를 초기화

    while queue:
        current_sum = queue.popleft()  # 큐에서 현재 합계를 가져옴

        if current_sum == n:
            ways += 1  # 현재 합계가 n과 같으면 방법의 수를 증가
        elif current_sum < n:
            # 현재 합계가 n보다 작으면 다음 가능한 숫자(1, 2, 3)를 큐에 추가
            queue.append(current_sum + 1)
            queue.append(current_sum + 2)
            queue.append(current_sum + 3)

    return ways  # n을 표현하는 총 방법 수를 반환

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    n = int(input())  # 각 테스트 케이스의 정수 n
    ways = find(n)  # 방법을 찾는 함수 호출
    print(ways)  # 결과 출력
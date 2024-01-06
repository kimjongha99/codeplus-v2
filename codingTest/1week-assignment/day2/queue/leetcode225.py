import collections
from collections import deque


class MyStack:

    def __init__(self):  # Python에서 __init__은 클래스의 새 인스턴스가 생성될 때 자동으로 호출되는 특수 메서드
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        for _ in range(len(self.q) - 1):  # _ 이거는 의미없는 변수. q의 제일 뒷 요소 앞에 추가.
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0  # Simplified check for emptiness


# Example usage
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print("Top:", myStack.top())  # return 2
print("Pop:", myStack.pop())  # return 2
print("Empty:", myStack.empty())  # return False

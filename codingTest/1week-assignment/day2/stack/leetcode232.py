class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        print("큐 초기화됨.")  # Queue initialized

    def push(self, x: int) -> None:
        self.input.append(x)
        print(f"{x} 입력 스택에 푸시됨.")  # x pushed to input stack

    def pop(self) -> int:
        self.peek()  # Returns the first element and does not delete it
        popped_element = self.output.pop()
        print(f"{popped_element} 출력 스택에서 팝됨.")  # popped_element popped from output stack
        return popped_element

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            print("입력 스택에서 출력 스택으로 전송됨.")  # Transferred from input stack to output stack
        return self.output[-1]

    def empty(self) -> bool:
        is_empty = not self.input and not self.output
        print(f"큐가 비어있습니까? {'예' if is_empty else '아니오'}")  # Is the queue empty? Yes/No
        return is_empty

# Example usage
myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print("가장 앞:", myQueue.peek())    # The front element
print("팝:", myQueue.pop())          # Pop
print("큐가 비어있습니까?", myQueue.empty())  # Is the queue empty?
print(myQueue.output)
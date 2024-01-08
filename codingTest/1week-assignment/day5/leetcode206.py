class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:  # curr가 none이 때 까지 초기화

            next_temp = curr.next  # 'next_temp'는 'curr'의 다음 노드를 임시로 저장합니다.
            curr.next = prev # 연결을 뒤집습니다: 'curr.next'를 'prev'로 설정합니다
            prev = curr  # 'prev'를 앞으로 이동시킵니다: 'prev'는 이제 'curr'(현재 노드)를 가리킵니다.
            curr = next_temp  # 'curr'를 앞으로 이동시킵니다: 'curr'는 이제 원본 리스트의 다음 노드를 가리킵니다.

        return prev


# Test the solution
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    sol = Solution()
    result = sol.reverseList(l1)
    print("Output:", result)

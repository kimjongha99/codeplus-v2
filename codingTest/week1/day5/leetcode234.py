# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# 팰린드롬은 이효리는 거꾸로 읽어도 이효리
# 링크드 리스트 헤드가 주어질떄 팰린드롬인지 아닌지 알아봐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr =[]
        cur_node = head

        while cur_node:
            arr.append(cur_node.val)
            cur_node = cur_node.next

        if arr == list(reversed(arr)):
            return True
        return False


if __name__ == "__main__":
    head = [1,2,2,1]
    sol = Solution()
    result = sol.isPalindrome(head)
    print("Output:", result)

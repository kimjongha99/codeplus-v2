#https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Search in a Binary Search Tree
from idlelib.tree import TreeNode
from typing import Optional


class Solution:

    def __init__(self):
        self.result = None

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        self.recur(root, low, high)
        return self.result

    def recur(self, node: TreeNode, low: int, high: int):
        # 노드가 없다 = 리프 노드의 자식 노드
        if node is None:
            return

        # 현재 노드가 문제의 범위에 포함되면 결과값에 더함
        if low <= node.val <= high:
            self.result += node.val

        # 현재 노드의 왼쪽, 오른쪽 자식 노드를 재귀적으로 탐색
        self.recur(node.left, low, high)
        self.recur(node.right, low, high)
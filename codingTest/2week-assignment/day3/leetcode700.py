# https://leetcode.com/problems/search-in-a-binary-search-tree/
#
# Search in a Binary Search Tree
from typing_extensions import Optional

#이문제는 이진탐색트리와 정수가 주어질때 , 해당 정수를 정수로 값는 노드를 반환     없음널



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if node is None:
            return None  #노드가 없으면  none 리턴
        elif node.val == val:  # 노드가 맞으면 리턴
            return node
        elif node.val > val:  #현재 노드값이 정수보다 크면 왼쪽에만있다는것이라서 탐색
            return self.searchBST(node.left, val)
        else:  # 그반대
            return self.searchBST(node.right, val)
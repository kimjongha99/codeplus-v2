#543. Diameter of Binary Tree
#https://leetcode.com/problems/diameter-of-binary-tree/description/
from idlelib.tree import TreeNode
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: TreeNode) -> int:
            nonlocal result

            if not node:   #만약 노드가 0이라면 반환
                return 0

            left_len = dfs(node.left)  #왼쪽노드의 길이를 저장
            right_len = dfs(node.right) #오른쪽노드의 길이를 저장

            current_len = left_len + right_len #합
            result = max(result, current_len)  #현재까지 발견된 최대직경 보다 높은것이있다면 갱신

            return max(left_len, right_len) + 1 # 두개중 큰직경을 리턴 , +1은 root노드

        dfs(root)
        return result



if __name__ == "__main__":
    # Create nodes
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    # Construct the tree
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    # Create a Solution object and test the function
    solution = Solution()
    print("Diameter of the tree:", solution.diameterOfBinaryTree(node1))  # Expected output: 3

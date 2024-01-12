#이진트리의 최대 깊이
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
from collections import deque
from binarytree import make_tree_by
def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3
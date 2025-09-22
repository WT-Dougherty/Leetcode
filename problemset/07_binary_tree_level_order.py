"""
Problem: Binary Tree Level Order Traversal (BFS)
------------------------------------------------
Given the root of a binary tree, return the level order traversal of its nodes' values (left to right, level by level).

Approach (BFS with queue):
- Push root, then iterate by levels collecting values.

Time: O(n) | Space: O(n)
"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q = deque([root])
    ans = []
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
    return ans

def _build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    # vals in level order, None for missing
    if not vals: return None
    it = iter(vals)
    root_val = next(it)
    if root_val is None: return None
    root = TreeNode(root_val)
    q = deque([root])
    for v_left, v_right in zip(it, it):
        node = q.popleft()
        if v_left is not None:
            node.left = TreeNode(v_left); q.append(node.left)
        if v_right is not None:
            node.right = TreeNode(v_right); q.append(node.right)
    return root

def _test():
    root = _build_tree([3,9,20,None,None,15,7])
    assert level_order(root) == [[3],[9,20],[15,7]]
    assert level_order(None) == []
    assert level_order(_build_tree([1])) == [[1]]

if __name__ == "__main__":
    _test()
    print("OK")
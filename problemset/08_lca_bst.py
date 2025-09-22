"""
Problem: Lowest Common Ancestor in a BST
----------------------------------------
Given a Binary Search Tree (BST) and two nodes p and q, find their lowest common ancestor.

Approach:
- Walk from root: if both targets < root, go left; if both > root, go right; else root is LCA.

Time: O(h) | Space: O(1) where h is tree height
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
    return cur

def _test():
    # Build a small BST:      6
    #                       /   \
    #                      2     8
    #                     / \   / \
    #                    0   4  7   9
    #                       / \
    #                      3   5
    n0=TreeNode(0); n3=TreeNode(3); n5=TreeNode(5); n4=TreeNode(4,n3,n5)
    n2=TreeNode(2,n0,n4); n7=TreeNode(7); n9=TreeNode(9); n8=TreeNode(8,n7,n9)
    n6=TreeNode(6,n2,n8)
    assert lowest_common_ancestor(n6, n2, n8) is n6
    assert lowest_common_ancestor(n6, n2, n4) is n2
    assert lowest_common_ancestor(n6, n7, n9) is n8

if __name__ == "__main__":
    _test()
    print("OK")
"""
Problem: Reverse a Singly Linked List
-------------------------------------
Reverse a singly linked list and return the new head.

Approach (Iterative):
- Traverse and rewire next pointers using prev/curr/next.

Time: O(n) | Space: O(1)
"""
from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def _to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def _from_list(vals: List[int]) -> Optional[ListNode]:
    head = None
    for x in reversed(vals):
        head = ListNode(x, head)
    return head

def _test():
    head = _from_list([1,2,3,4,5])
    rev = reverse_list(head)
    assert _to_list(rev) == [5,4,3,2,1]
    assert _to_list(reverse_list(_from_list([]))) == []
    assert _to_list(reverse_list(_from_list([7]))) == [7]

if __name__ == "__main__":
    _test()
    print("OK")
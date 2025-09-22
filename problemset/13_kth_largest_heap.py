"""
Problem: Kth Largest Element in an Array (Heap/Quickselect)
-----------------------------------------------------------
Return the k-th largest element in an unsorted array.

Approach (Min-Heap of size k):
- Maintain a min-heap of size k; push elements and pop when size > k.
- The root is the k-th largest at the end.

Time: O(n log k) | Space: O(k)
"""
from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be in 1..len(nums)")
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
    return heap[0]

def _test():
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert find_kth_largest([1], 1) == 1

if __name__ == "__main__":
    _test()
    print("OK")
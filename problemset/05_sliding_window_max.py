"""
Problem: Sliding Window Maximum (Monotonic Deque)
-------------------------------------------------
Given an integer array `nums` and an integer `k`, return an array of the maximum values in every contiguous subarray of size `k`.

Approach (Deque of indices, decreasing values):
- Maintain deque with indices whose values are decreasing.
- Pop from left when index is out of window; pop from right while current value >= last value.
- The front is the max for the current window.

Time: O(n) | Space: O(k)
"""
from collections import deque
from typing import List

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be in 1..len(nums)")
    dq = deque()  # stores indices
    out = []
    for i, x in enumerate(nums):
        # remove out-of-window indices
        if dq and dq[0] <= i - k:
            dq.popleft()
        # maintain decreasing deque
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

def _test():
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([9,8,7,6,5], 2) == [9,8,7,6]

if __name__ == "__main__":
    _test()
    print("OK")
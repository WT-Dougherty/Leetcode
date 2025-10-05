"""
Problem: Sliding Window Maximum (Monotonic Deque)
-------------------------------------------------
Given an integer array `nums` and an integer `k`, return an array of the maximum values in every contiguous subarray of size `k`.

Approach:
If I did brute-force, the runtime would be O(n * k)
I can reduce this...


"""
from collections import deque
from typing import List

def brute_force (nums: List[int], k: int) -> List[int]:
    ra = []
    if len(nums) < k or len(nums) == 0:
        return []
    for i in range(len(nums) - k+1):
        cur = nums[i:i+k]
        ra.append(max(cur))
    return ra

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    return brute_force(nums, k)

def _test():
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([], 0) == []
    assert max_sliding_window([9,8,7,6,5], 2) == [9,8,7,6]
    assert max_sliding_window([9, 2, -1, -2, -1, 0, 4], 3) == [9, 2, -1, 0, 4]

if __name__ == "__main__":
    _test()
    print("OK")
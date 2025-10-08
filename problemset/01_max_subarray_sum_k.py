"""
Problem: Maximum Sum Subarray of Size k (Static Sliding Window)
---------------------------------------------------------------
Given an array of integers `nums` and an integer `k`, return the maximum sum of any contiguous subarray of length `k`.

Approach:
- Compute the sum of the first `k` elements.
- Slide the window by 1 each step: add the incoming element and remove the outgoing one.
- Track the maximum across all windows.

Time: O(n) | Space: O(1)
"""

from typing import List


def max_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for val in nums[:k]:
        max_sum += val
    cur_sum = max_sum
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, cur_sum)
    return max_sum


def _test():
    assert max_subarray_sum([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_subarray_sum([1, 2, 3, 4, 5], 2) == 9
    assert max_subarray_sum([5, -2, 3, 1, 2], 3) == 6
    assert max_subarray_sum([10], 1) == 10


if __name__ == "__main__":
    _test()
    print("OK")

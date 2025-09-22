"""
Problem: Two Sum
----------------
Given an array of integers `nums` and a target integer `target`,
return indices of the two numbers such that they add up to `target`.
Assume exactly one solution exists and you may not use the same element twice.

Approach (Hash Map):
- Scan left-to-right; for each x, check if target-x is already seen.

Time: O(n) | Space: O(n)
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    pass

def _test():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]

if __name__ == "__main__":
    _test()
    print("OK")
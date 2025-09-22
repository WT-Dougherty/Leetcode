"""
Problem: Counting Bits (Bit DP)
--------------------------------
Given an integer n, return an array `ans` where ans[i] is the number of 1-bits (Hamming weight) of i for 0 <= i <= n.

Approach:
- DP relation: ans[i] = ans[i >> 1] + (i & 1)

Time: O(n) | Space: O(n)
"""
from typing import List

def count_bits(n: int) -> List[int]:
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

def _test():
    assert count_bits(2) == [0,1,1]
    assert count_bits(5) == [0,1,1,2,1,2]
    assert count_bits(0) == [0]

if __name__ == "__main__":
    _test()
    print("OK")
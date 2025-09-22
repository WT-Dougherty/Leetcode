"""
Problem: Permutations (Backtracking)
-----------------------------------
Given an array of distinct integers `nums`, return all possible permutations.

Approach (Backtracking):
- Build permutations incrementally, marking used elements.

Time: O(n*n!) | Space: O(n)
"""
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    used = [False]*len(nums)
    cur, out = [], []
    def backtrack():
        if len(cur) == len(nums):
            out.append(cur[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            cur.append(nums[i])
            backtrack()
            cur.pop()
            used[i] = False
    backtrack()
    return out

def _test():
    res = permute([1,2,3])
    expect = {
        (1,2,3),(1,3,2),
        (2,1,3),(2,3,1),
        (3,1,2),(3,2,1),
    }
    assert {tuple(x) for x in res} == expect
    assert permute([1]) == [[1]]

if __name__ == "__main__":
    _test()
    print("OK")
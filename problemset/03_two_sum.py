"""
Problem: Two Sum
----------------
Given an array of integers `nums` and a target integer `target`,
return indices of the two numbers such that they add up to `target`.
Assume exactly one solution exists and you may not use the same element twice.

First Brainstorm & Approach:
- First, I need to sort the two arrays. Assuming length n, this should take O(n log n)
    - Quicksort is the defult built-in sort method for Python
- Once sorted, I need to iterate once through the array:
    - For each entry, perform binary search on latter half of the array for
      the other value that is needed. This takes O(log n)
        - If other value found, return current index and index of found element
    - This should take O(n log n), since doing log n operation n times
TOTAL RUNTIME: O(n log n)

TODO:
- Implement binary search
- Implement two_sum alg

NOTE:
- There are edge cases that fail. For example, if array is [3, 3] and
  target is 6, algorithm returns [0, 0]


Since edge cases break my current algorithm, I'm going to try something new.
Hash Map Approach:
- I will iterate through the input array, checking to see if the desired value is in
  a hash-map:
    - If it is, I return the value corresponding to that key with the current index
    - If it isn't, I add the current value to the hashmap

This solution is O(n) since hash lookups are constant.

"""

if False:
    # helper functions
    def binary_search(nums: list[int], k: int, l: int, r: int):
        # k not found
        if l > r:
            return -1

        # alg logic
        mid = (r + l) // 2
        if nums[mid] == k:
            return mid
        elif nums[mid] > k:
            return binary_search(nums, k, l, mid - 1)
        else:
            return binary_search(nums, k, mid + 1, r)

    # final alg
    def two_sum(nums: list[int], target: int) -> list[int]:
        sorted_nums = [n for n in nums]
        sorted_nums.sort()

        for i in range(len(sorted_nums)):
            k = target - sorted_nums[i]
            index = binary_search(sorted_nums, k, i + 1, len(sorted_nums) - 1)
            print(i, index)
            if index > 0 and index != i:
                rv = [nums.index(sorted_nums[i]), nums.index(sorted_nums[index])]
                rv.sort()
                return rv
        return [-1, -1]


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = dict()
    for i, n in enumerate(nums):
        k = target - n
        if k in seen:
            return [seen[k], i]
        seen[n] = i
    return [-1, -1]


def _test():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, -1, 17, 2, 7, -9, 11, 15, 10], 19) == [2, 3]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    _test()
    print("OK")

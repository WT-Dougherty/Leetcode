# ----------------------- Static Window Size -----------------------------
# Given an array of nums and integer k, find the maximum sum of any subarray of length k
# Example: nums = [2, 1, 5, 1, 3, 2], k = 3; max_sum = 9
# The function:
def max_sum_k(nums, k) -> int:
    max_sum = 0
    for val in nums[:k]:
        max_sum += val
    cur_sum = max_sum
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, cur_sum)
    return max_sum
# tests
def test_max_sum_k():
    assert max_sum_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_k([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_k([5, -2, 3, 1, 2], 3) == 6
    assert max_sum_k([1, 1, 1, 1], 2) == 2
    assert max_sum_k([10], 1) == 10
    print("All static window tests passed!")
test_max_sum_k()

# ----------------------- Dynamic Window Size -----------------------------
# Given an array of positive integers and a target sum, find the length of the longest 
# subarray whose sum is less than or equal to the target
# Example: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], target = 8; max_length = 4
# The subarray [1, 2, 7] has sum 10 > 8, but [1, 2, 7, 4] has sum 14 > 8
# The longest valid subarray is [4, 2, 1, 1] with sum 8 and length 4
def longest_subarray_sum_leq(nums, target) -> int:
    left, sum, max_length = 0, 0, 0
    for i in range( len(nums) ):
        sum += nums[i]
        while sum > target:
            sum -= nums[left]
            left += 1
        max_length = max(max_length, i-left+1)
    return max_length

# tests
def test_longest_subarray_sum_leq():
    assert longest_subarray_sum_leq([3, 1, 2, 7, 4, 2, 1, 1, 5], 8) == 4
    assert longest_subarray_sum_leq([1, 2, 3, 4, 5], 9) == 3
    assert longest_subarray_sum_leq([2, 3, 1, 2, 4, 3], 7) == 3
    assert longest_subarray_sum_leq([1, 1, 1, 1], 3) == 3
    assert longest_subarray_sum_leq([5, 4, 3, 2, 1], 1) == 1
    assert longest_subarray_sum_leq([10, 5, 2, 6], 100) == 4
    assert longest_subarray_sum_leq([1, 2, 3], 0) == 0
    print("All dynamic window tests passed!")

test_longest_subarray_sum_leq()

# ----------------------- Dynamic Window Size; Strings -----------------------------
# Given a string s, find the length of the longest substring without duplicate characters.
# Example: s = "abcabcbb"; max_length = 3
# The longest substring without repeating characters is "abc" with length 3
def longest_substring_no_repeats(s) -> int:
    seen = set()
    left, max_len = 0, 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[i])
        max_len = max(max_len, i-left+1)
    return max_len


# tests
def test_longest_substring_no_repeats():
    assert longest_substring_no_repeats("abcabcbb") == 3
    assert longest_substring_no_repeats("bbbbb") == 1
    assert longest_substring_no_repeats("pwwkew") == 3
    assert longest_substring_no_repeats("") == 0
    assert longest_substring_no_repeats("a") == 1
    assert longest_substring_no_repeats("abcdef") == 6
    assert longest_substring_no_repeats("dvdf") == 3
    print("All string sliding window tests passed!")

test_longest_substring_no_repeats()
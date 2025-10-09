# Distinct Subsequences

## Problem Description

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits in a 32-bit signed integer.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

## Examples

### Example 1:

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

### Example 2:

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

## Constraints

- 1 <= s.length, t.length <= 1000
- s and t consist of only lowercase English letters.

## Desired Time Complexity

- **Time Complexity**: O(m \* n) where m is length of s and n is length of t
- **Space Complexity**: O(m \* n)

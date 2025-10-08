# Permutation in String

## Problem Description

Given two strings `s1` and `s2`, return `true` _if `s2` contains a permutation of `s1`_.

In other words, one of `s1`'s permutations is the substring of `s2`.

## Examples

### Example 1:

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2:

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters only.

## Desired Time Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

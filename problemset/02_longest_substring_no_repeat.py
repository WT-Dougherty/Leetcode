"""
Problem: Longest Substring Without Repeating Characters (Dynamic Window)
-----------------------------------------------------------------------
Given a string s, find the length of the longest substring without duplicate characters.

Approach (Sliding Window + last-seen index):
- Expand right pointer; if s[right] is inside the current window, move left to last_index+1.
- Update best length.

Time: O(n) | Space: O(min(n, Σ))
"""


def length_of_longest_substring(s: str) -> int:
    seen = set()
    left, max_len = 0, 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[i])
        max_len = max(max_len, i - left + 1)
    return max_len


def _test():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3


if __name__ == "__main__":
    _test()
    print("OK")

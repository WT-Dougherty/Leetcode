"""
Longest Substring Without Repeating Characters - LeetCode Problem 3

Given a string s, find the length of the longest substring without repeating characters.
"""

import time
import random
import string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right, max_len = 0, 0, 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    assert result1 == 3, f"Failed for '{s1}', expected 3, got {result1}"

    # Test Case 2: All same characters
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    assert result2 == 1, f"Failed for '{s2}', expected 1, got {result2}"

    # Test Case 3: Complex case
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    assert result3 == 3, f"Failed for '{s3}', expected 3, got {result3}"

    # Test Case 4: Empty string
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    assert result4 == 0, f"Failed for '{s4}', expected 0, got {result4}"

    # Test Case 5: Single character
    s5 = "a"
    result5 = solution.lengthOfLongestSubstring(s5)
    assert result5 == 1, f"Failed for '{s5}', expected 1, got {result5}"

    # Test Case 6: All unique characters
    s6 = "abcdef"
    result6 = solution.lengthOfLongestSubstring(s6)
    assert result6 == 6, f"Failed for '{s6}', expected 6, got {result6}"

    # Test Case 7: Two characters
    s7 = "au"
    result7 = solution.lengthOfLongestSubstring(s7)
    assert result7 == 2, f"Failed for '{s7}', expected 2, got {result7}"

    # Test Case 8: Space in string
    s8 = " "
    result8 = solution.lengthOfLongestSubstring(s8)
    assert result8 == 1, f"Failed for '{s8}', expected 1, got {result8}"

    # Test Case 9: Numbers and letters
    s9 = "a1b2c3d4e5"
    result9 = solution.lengthOfLongestSubstring(s9)
    assert result9 == 10, f"Failed for '{s9}', expected 10, got {result9}"

    # Test Case 10: Complex repeating pattern
    s10 = "dvdf"
    result10 = solution.lengthOfLongestSubstring(s10)
    assert result10 == 3, f"Failed for '{s10}', expected 3, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 50000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tMax Length")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        chars = string.ascii_letters + string.digits + "!@#$%^&*() "
        s = "".join(random.choices(chars, k=size))

        # Test approach
        start_time = time.time()
        result = solution.lengthOfLongestSubstring(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    s = "a" * 50000
    result = solution.lengthOfLongestSubstring(s)
    print(f"Maximum length (50k chars): {result} ✅")

    # Edge Case 2: All unique characters
    s = "".join([chr(i) for i in range(128)])  # All ASCII characters
    result = solution.lengthOfLongestSubstring(s)
    print(f"All unique ASCII chars: {result} ✅")

    # Edge Case 3: Alternating pattern
    s = "ab" * 1000
    result = solution.lengthOfLongestSubstring(s)
    print(f"Alternating pattern: {result} ✅")

    # Edge Case 4: Numbers and symbols
    s = "1234567890!@#$%^&*()"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Numbers and symbols: {result} ✅")

    # Edge Case 5: Single repeated character
    s = "z" * 1000
    result = solution.lengthOfLongestSubstring(s)
    print(f"Single repeated char: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    chars = string.ascii_letters + string.digits + "!@#$%^&*() "
    s = "".join(random.choices(chars, k=50000))

    start_time = time.time()
    result = solution.lengthOfLongestSubstring(s)
    time1 = time.time() - start_time

    print(f"Large dataset (50,000 characters):")
    print(f"Time: {time1:.6f}s, Max length: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Substring Without Repeating Characters Problem")
    print("=" * 80)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the lengthOfLongestSubstring method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use sliding window with hash set")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using sliding window with hash set")

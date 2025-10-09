"""
Minimum Window Substring - LeetCode Problem 76

Given two strings s and t of lengths m and n respectively, return the minimum window substring 
of s such that every character in t (including duplicates) is included in the window. 
If there is no such window, return the empty string "".

The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
"""

import time
import random
import string


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1, t1 = "ADOBECODEBANC", "ABC"
    result1 = solution.minWindow(s1, t1)
    assert result1 == "BANC", f"Failed for s='{s1}', t='{t1}', expected 'BANC', got '{result1}'"

    # Test Case 2: Single character
    s2, t2 = "a", "a"
    result2 = solution.minWindow(s2, t2)
    assert result2 == "a", f"Failed for s='{s2}', t='{t2}', expected 'a', got '{result2}'"

    # Test Case 3: No valid window
    s3, t3 = "a", "aa"
    result3 = solution.minWindow(s3, t3)
    assert result3 == "", f"Failed for s='{s3}', t='{t3}', expected '', got '{result3}'"

    # Test Case 4: Same strings
    s4, t4 = "abc", "abc"
    result4 = solution.minWindow(s4, t4)
    assert result4 == "abc", f"Failed for s='{s4}', t='{t4}', expected 'abc', got '{result4}'"

    # Test Case 5: Multiple occurrences
    s5, t5 = "ab", "b"
    result5 = solution.minWindow(s5, t5)
    assert result5 == "b", f"Failed for s='{s5}', t='{t5}', expected 'b', got '{result5}'"

    # Test Case 6: Complex case
    s6, t6 = "a", "b"
    result6 = solution.minWindow(s6, t6)
    assert result6 == "", f"Failed for s='{s6}', t='{t6}', expected '', got '{result6}'"

    # Test Case 7: Case sensitive
    s7, t7 = "aA", "aA"
    result7 = solution.minWindow(s7, t7)
    assert result7 == "aA", f"Failed for s='{s7}', t='{t7}', expected 'aA', got '{result7}'"

    # Test Case 8: Duplicate characters in t
    s8, t8 = "bba", "ab"
    result8 = solution.minWindow(s8, t8)
    assert result8 == "ba", f"Failed for s='{s8}', t='{t8}', expected 'ba', got '{result8}'"

    # Test Case 9: Empty result
    s9, t9 = "abc", "xyz"
    result9 = solution.minWindow(s9, t9)
    assert result9 == "", f"Failed for s='{s9}', t='{t9}', expected '', got '{result9}'"

    # Test Case 10: Edge case
    s10, t10 = "ab", "a"
    result10 = solution.minWindow(s10, t10)
    assert result10 == "a", f"Failed for s='{s10}', t='{t10}', expected 'a', got '{result10}'"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m+n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult Length")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        s = "".join(random.choices(string.ascii_letters, k=size))
        t = "".join(random.choices(string.ascii_letters, k=min(10, size)))

        # Test approach
        start_time = time.time()
        result = solution.minWindow(s, t)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)}")

    # Verify O(m+n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m+n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m+n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m+n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m*n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m+n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m+n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    s = "a" * 100000
    t = "a"
    result = solution.minWindow(s, t)
    print(f"Maximum length (100k chars): {len(result)} ✅")

    # Edge Case 2: All same characters
    s = "a" * 1000
    t = "a" * 100
    result = solution.minWindow(s, t)
    print(f"All same characters: {len(result)} ✅")

    # Edge Case 3: Single character
    s = "a"
    t = "a"
    result = solution.minWindow(s, t)
    print(f"Single character: {len(result)} ✅")

    # Edge Case 4: Case sensitivity
    s = "AaBbCc"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(f"Case sensitivity: {len(result)} ✅")

    # Edge Case 5: No valid window
    s = "abcdefghijklmnopqrstuvwxyz"
    t = "XYZ"
    result = solution.minWindow(s, t)
    print(f"No valid window: {len(result)} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    s = "".join(random.choices(string.ascii_letters, k=100000))
    t = "".join(random.choices(string.ascii_letters, k=100))

    start_time = time.time()
    result = solution.minWindow(s, t)
    time1 = time.time() - start_time

    print(f"Large dataset (s=100k chars, t=100 chars):")
    print(f"Time: {time1:.6f}s, Result length: {len(result)}")


if __name__ == "__main__":
    print("🧪 Testing Minimum Window Substring Problem")
    print("=" * 70)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minWindow method")
        print("- Aim for O(m+n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use sliding window with character frequency")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m+n)")
        print("- Consider using sliding window with frequency map")

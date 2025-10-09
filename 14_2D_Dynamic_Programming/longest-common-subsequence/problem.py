"""
Longest Common Subsequence - LeetCode Problem 1143

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

import time


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    text1_1 = "abcde"
    text2_1 = "ace"
    result1 = solution.longestCommonSubsequence(text1_1, text2_1)
    assert (
        result1 == 3
    ), f"Failed for text1='{text1_1}', text2='{text2_1}', expected 3, got {result1}"

    # Test Case 2: Same strings
    text1_2 = "abc"
    text2_2 = "abc"
    result2 = solution.longestCommonSubsequence(text1_2, text2_2)
    assert (
        result2 == 3
    ), f"Failed for text1='{text1_2}', text2='{text2_2}', expected 3, got {result2}"

    # Test Case 3: No common subsequence
    text1_3 = "abc"
    text2_3 = "def"
    result3 = solution.longestCommonSubsequence(text1_3, text2_3)
    assert (
        result3 == 0
    ), f"Failed for text1='{text1_3}', text2='{text2_3}', expected 0, got {result3}"

    # Test Case 4: Single character
    text1_4 = "a"
    text2_4 = "a"
    result4 = solution.longestCommonSubsequence(text1_4, text2_4)
    assert (
        result4 == 1
    ), f"Failed for text1='{text1_4}', text2='{text2_4}', expected 1, got {result4}"

    # Test Case 5: Complex case
    text1_5 = "abcde"
    text2_5 = "ace"
    result5 = solution.longestCommonSubsequence(text1_5, text2_5)
    assert (
        result5 == 3
    ), f"Failed for text1='{text1_5}', text2='{text2_5}', expected 3, got {result5}"

    # Test Case 6: Another case
    text1_6 = "abc"
    text2_6 = "def"
    result6 = solution.longestCommonSubsequence(text1_6, text2_6)
    assert (
        result6 == 0
    ), f"Failed for text1='{text1_6}', text2='{text2_6}', expected 0, got {result6}"

    # Test Case 7: Edge case
    text1_7 = "a"
    text2_7 = "b"
    result7 = solution.longestCommonSubsequence(text1_7, text2_7)
    assert (
        result7 == 0
    ), f"Failed for text1='{text1_7}', text2='{text2_7}', expected 0, got {result7}"

    # Test Case 8: Complex case
    text1_8 = "oxcpqrsvwf"
    text2_8 = "shmtulqrypy"
    result8 = solution.longestCommonSubsequence(text1_8, text2_8)
    assert (
        result8 == 2
    ), f"Failed for text1='{text1_8}', text2='{text2_8}', expected 2, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("len1\tlen2\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create strings with some common characters
        text1 = "a" * size + "b" * size
        text2 = "a" * size + "c" * size

        # Test approach
        start_time = time.time()
        result = solution.longestCommonSubsequence(text1, text2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{len(text1)}\t{len(text2)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity where m is length of text1 and n is length of text2
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (test_sizes[i - 1] * 2) * (test_sizes[i - 1] * 2)
            curr_complexity = (test_sizes[i] * 2) * (test_sizes[i] * 2)
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m*n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(m * n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m * n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m * n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 character each)
    text1_1 = "a"
    text2_1 = "a"
    result1 = solution.longestCommonSubsequence(text1_1, text2_1)
    assert result1 == 1, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (1000 characters each)
    text1_2 = "a" * 1000
    text2_2 = "a" * 1000
    result2 = solution.longestCommonSubsequence(text1_2, text2_2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: No common characters
    text1_3 = "abc"
    text2_3 = "def"
    result3 = solution.longestCommonSubsequence(text1_3, text2_3)
    assert result3 == 0, f"No common characters failed: {result3}"
    print(f"No common characters: ✅")

    # Edge Case 4: All same characters
    text1_4 = "aaaa"
    text2_4 = "aaaa"
    result4 = solution.longestCommonSubsequence(text1_4, text2_4)
    assert result4 == 4, f"All same characters failed: {result4}"
    print(f"All same characters: ✅")

    # Edge Case 5: One string is substring of another
    text1_5 = "abcdef"
    text2_5 = "abc"
    result5 = solution.longestCommonSubsequence(text1_5, text2_5)
    assert result5 == 3, f"Substring case failed: {result5}"
    print(f"Substring case: ✅")

    # Edge Case 6: Different lengths
    text1_6 = "a"
    text2_6 = "abc"
    result6 = solution.longestCommonSubsequence(text1_6, text2_6)
    assert result6 == 1, f"Different lengths failed: {result6}"
    print(f"Different lengths: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Longest Common Subsequence:")

    # Large dataset
    text1 = "a" * 100 + "b" * 100
    text2 = "a" * 100 + "c" * 100

    start_time = time.time()
    result = solution.longestCommonSubsequence(text1, text2)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (text1={len(text1)}, text2={len(text2)}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Common Subsequence Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the longestCommonSubsequence method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

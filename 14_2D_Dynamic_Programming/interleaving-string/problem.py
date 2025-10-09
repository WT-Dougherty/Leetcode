"""
Interleaving String - LeetCode Problem 97

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into
n and m non-empty substrings respectively, such that:

- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

Note: a + b is the concatenation of strings a and b.
"""

import time


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1_1 = "aabcc"
    s2_1 = "dbbca"
    s3_1 = "aadbbcbcac"
    result1 = solution.isInterleave(s1_1, s2_1, s3_1)
    assert (
        result1 == True
    ), f"Failed for s1='{s1_1}', s2='{s2_1}', s3='{s3_1}', expected True, got {result1}"

    # Test Case 2: False case
    s1_2 = "aabcc"
    s2_2 = "dbbca"
    s3_2 = "aadbbbaccc"
    result2 = solution.isInterleave(s1_2, s2_2, s3_2)
    assert (
        result2 == False
    ), f"Failed for s1='{s1_2}', s2='{s2_2}', s3='{s3_2}', expected False, got {result2}"

    # Test Case 3: Empty strings
    s1_3 = ""
    s2_3 = ""
    s3_3 = ""
    result3 = solution.isInterleave(s1_3, s2_3, s3_3)
    assert (
        result3 == True
    ), f"Failed for s1='{s1_3}', s2='{s2_3}', s3='{s3_3}', expected True, got {result3}"

    # Test Case 4: Single character
    s1_4 = "a"
    s2_4 = "b"
    s3_4 = "ab"
    result4 = solution.isInterleave(s1_4, s2_4, s3_4)
    assert (
        result4 == True
    ), f"Failed for s1='{s1_4}', s2='{s2_4}', s3='{s3_4}', expected True, got {result4}"

    # Test Case 5: Different order
    s1_5 = "a"
    s2_5 = "b"
    s3_5 = "ba"
    result5 = solution.isInterleave(s1_5, s2_5, s3_5)
    assert (
        result5 == True
    ), f"Failed for s1='{s1_5}', s2='{s2_5}', s3='{s3_5}', expected True, got {result5}"

    # Test Case 6: Complex case
    s1_6 = "aabcc"
    s2_6 = "dbbca"
    s3_6 = "aadbbcbcac"
    result6 = solution.isInterleave(s1_6, s2_6, s3_6)
    assert (
        result6 == True
    ), f"Failed for s1='{s1_6}', s2='{s2_6}', s3='{s3_6}', expected True, got {result6}"

    # Test Case 7: Edge case
    s1_7 = "a"
    s2_7 = ""
    s3_7 = "a"
    result7 = solution.isInterleave(s1_7, s2_7, s3_7)
    assert (
        result7 == True
    ), f"Failed for s1='{s1_7}', s2='{s2_7}', s3='{s3_7}', expected True, got {result7}"

    # Test Case 8: False case
    s1_8 = "a"
    s2_8 = "b"
    s3_8 = "c"
    result8 = solution.isInterleave(s1_8, s2_8, s3_8)
    assert (
        result8 == False
    ), f"Failed for s1='{s1_8}', s2='{s2_8}', s3='{s3_8}', expected False, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [20, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("s1_len\ts2_len\ts3_len\tTime\t\tResult")
    print("-" * 60)

    for size in test_sizes:
        # Generate test data - create strings with interleaving
        s1 = "a" * size
        s2 = "b" * size
        s3 = "ab" * size

        # Test approach
        start_time = time.time()
        result = solution.isInterleave(s1, s2, s3)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{len(s1)}\t{len(s2)}\t{len(s3)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity where m is length of s1 and n is length of s2
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * test_sizes[i - 1]
            curr_complexity = test_sizes[i] * test_sizes[i]
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

    # Edge Case 1: Minimum constraint (0 characters each)
    s1_1 = ""
    s2_1 = ""
    s3_1 = ""
    result1 = solution.isInterleave(s1_1, s2_1, s3_1)
    assert result1 == True, f"Empty strings failed: {result1}"
    print(f"Empty strings: ✅")

    # Edge Case 2: Maximum constraint (100 characters each)
    s1_2 = "a" * 100
    s2_2 = "b" * 100
    s3_2 = "ab" * 100
    result2 = solution.isInterleave(s1_2, s2_2, s3_2)
    assert isinstance(result2, bool), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: One empty string
    s1_3 = "abc"
    s2_3 = ""
    s3_3 = "abc"
    result3 = solution.isInterleave(s1_3, s2_3, s3_3)
    assert result3 == True, f"One empty string failed: {result3}"
    print(f"One empty string: ✅")

    # Edge Case 4: Single character
    s1_4 = "a"
    s2_4 = "b"
    s3_4 = "ab"
    result4 = solution.isInterleave(s1_4, s2_4, s3_4)
    assert result4 == True, f"Single character failed: {result4}"
    print(f"Single character: ✅")

    # Edge Case 5: All same characters
    s1_5 = "aaa"
    s2_5 = "aaa"
    s3_5 = "aaaaaa"
    result5 = solution.isInterleave(s1_5, s2_5, s3_5)
    assert result5 == True, f"All same characters failed: {result5}"
    print(f"All same characters: ✅")

    # Edge Case 6: No interleaving possible
    s1_6 = "abc"
    s2_6 = "def"
    s3_6 = "xyz"
    result6 = solution.isInterleave(s1_6, s2_6, s3_6)
    assert result6 == False, f"No interleaving possible failed: {result6}"
    print(f"No interleaving possible: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Interleaving String:")

    # Large dataset
    s1 = "a" * 50
    s2 = "b" * 50
    s3 = "ab" * 50

    start_time = time.time()
    result = solution.isInterleave(s1, s2, s3)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (s1={len(s1)}, s2={len(s2)}, s3={len(s3)}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Interleaving String Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isInterleave method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

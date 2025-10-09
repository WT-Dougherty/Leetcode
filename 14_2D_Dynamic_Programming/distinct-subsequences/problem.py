"""
Distinct Subsequences - LeetCode Problem 115

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits in a 32-bit signed integer.

A string's subsequence is a new string formed from the original string by deleting some
(can be none) of the characters without disturbing the remaining characters' relative
positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""

import time


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "rabbbit"
    t1 = "rabbit"
    result1 = solution.numDistinct(s1, t1)
    assert result1 == 3, f"Failed for s='{s1}', t='{t1}', expected 3, got {result1}"

    # Test Case 2: Another case
    s2 = "babgbag"
    t2 = "bag"
    result2 = solution.numDistinct(s2, t2)
    assert result2 == 5, f"Failed for s='{s2}', t='{t2}', expected 5, got {result2}"

    # Test Case 3: Single character
    s3 = "a"
    t3 = "a"
    result3 = solution.numDistinct(s3, t3)
    assert result3 == 1, f"Failed for s='{s3}', t='{t3}', expected 1, got {result3}"

    # Test Case 4: No match
    s4 = "abc"
    t4 = "def"
    result4 = solution.numDistinct(s4, t4)
    assert result4 == 0, f"Failed for s='{s4}', t='{t4}', expected 0, got {result4}"

    # Test Case 5: Empty target
    s5 = "abc"
    t5 = ""
    result5 = solution.numDistinct(s5, t5)
    assert result5 == 1, f"Failed for s='{s5}', t='{t5}', expected 1, got {result5}"

    # Test Case 6: Complex case
    s6 = "aabbcc"
    t6 = "abc"
    result6 = solution.numDistinct(s6, t6)
    assert result6 == 8, f"Failed for s='{s6}', t='{t6}', expected 8, got {result6}"

    # Test Case 7: Edge case
    s7 = "a"
    t7 = "b"
    result7 = solution.numDistinct(s7, t7)
    assert result7 == 0, f"Failed for s='{s7}', t='{t7}', expected 0, got {result7}"

    # Test Case 8: Same strings
    s8 = "abc"
    t8 = "abc"
    result8 = solution.numDistinct(s8, t8)
    assert result8 == 1, f"Failed for s='{s8}', t='{t8}', expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("s_len\tt_len\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create strings with some matches
        s = "a" * size + "b" * size
        t = "ab"

        # Test approach
        start_time = time.time()
        result = solution.numDistinct(s, t)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{len(s)}\t{len(t)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity where m is length of s and n is length of t
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (test_sizes[i - 1] * 2) * 2  # s_len * t_len
            curr_complexity = (test_sizes[i] * 2) * 2
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
    s1 = "a"
    t1 = "a"
    result1 = solution.numDistinct(s1, t1)
    assert result1 == 1, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (1000 characters each)
    s2 = "a" * 1000
    t2 = "a" * 1000
    result2 = solution.numDistinct(s2, t2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Empty target string
    s3 = "abc"
    t3 = ""
    result3 = solution.numDistinct(s3, t3)
    assert result3 == 1, f"Empty target failed: {result3}"
    print(f"Empty target: ✅")

    # Edge Case 4: Target longer than source
    s4 = "ab"
    t4 = "abc"
    result4 = solution.numDistinct(s4, t4)
    assert result4 == 0, f"Target longer than source failed: {result4}"
    print(f"Target longer than source: ✅")

    # Edge Case 5: All same characters
    s5 = "aaaa"
    t5 = "aa"
    result5 = solution.numDistinct(s5, t5)
    assert result5 == 6, f"All same characters failed: {result5}"
    print(f"All same characters: ✅")

    # Edge Case 6: No matches
    s6 = "abcdef"
    t6 = "xyz"
    result6 = solution.numDistinct(s6, t6)
    assert result6 == 0, f"No matches failed: {result6}"
    print(f"No matches: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Distinct Subsequences:")

    # Large dataset
    s = "a" * 100 + "b" * 100
    t = "ab"

    start_time = time.time()
    result = solution.numDistinct(s, t)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (s={len(s)}, t={len(t)}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Distinct Subsequences Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the numDistinct method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

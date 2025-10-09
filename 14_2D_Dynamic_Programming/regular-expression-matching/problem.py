"""
Regular Expression Matching - LeetCode Problem 10

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""

import time


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "aa"
    p1 = "a"
    result1 = solution.isMatch(s1, p1)
    assert (
        result1 == False
    ), f"Failed for s='{s1}', p='{p1}', expected False, got {result1}"

    # Test Case 2: Star case
    s2 = "aa"
    p2 = "a*"
    result2 = solution.isMatch(s2, p2)
    assert (
        result2 == True
    ), f"Failed for s='{s2}', p='{p2}', expected True, got {result2}"

    # Test Case 3: Dot case
    s3 = "ab"
    p3 = ".*"
    result3 = solution.isMatch(s3, p3)
    assert (
        result3 == True
    ), f"Failed for s='{s3}', p='{p3}', expected True, got {result3}"

    # Test Case 4: Complex case
    s4 = "aab"
    p4 = "c*a*b"
    result4 = solution.isMatch(s4, p4)
    assert (
        result4 == True
    ), f"Failed for s='{s4}', p='{p4}', expected True, got {result4}"

    # Test Case 5: Mismatch case
    s5 = "mississippi"
    p5 = "mis*is*p*."
    result5 = solution.isMatch(s5, p5)
    assert (
        result5 == False
    ), f"Failed for s='{s5}', p='{p5}', expected False, got {result5}"

    # Test Case 6: Empty string
    s6 = ""
    p6 = "a*"
    result6 = solution.isMatch(s6, p6)
    assert (
        result6 == True
    ), f"Failed for s='{s6}', p='{p6}', expected True, got {result6}"

    # Test Case 7: Single character
    s7 = "a"
    p7 = "a"
    result7 = solution.isMatch(s7, p7)
    assert (
        result7 == True
    ), f"Failed for s='{s7}', p='{p7}', expected True, got {result7}"

    # Test Case 8: Edge case
    s8 = "a"
    p8 = "ab*"
    result8 = solution.isMatch(s8, p8)
    assert (
        result8 == True
    ), f"Failed for s='{s8}', p='{p8}', expected True, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 20, 30]
    times = []

    print("\nTime Complexity Analysis:")
    print("s_len\tp_len\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create strings with patterns
        s = "a" * size
        p = "a*"

        # Test approach
        start_time = time.time()
        result = solution.isMatch(s, p)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{len(s)}\t{len(p)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity where m is length of s and n is length of p
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * 2  # p_len = 2
            curr_complexity = test_sizes[i] * 2
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
    p1 = "a"
    result1 = solution.isMatch(s1, p1)
    assert result1 == True, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (20 characters each)
    s2 = "a" * 20
    p2 = "a*"
    result2 = solution.isMatch(s2, p2)
    assert isinstance(result2, bool), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Empty string
    s3 = ""
    p3 = "a*"
    result3 = solution.isMatch(s3, p3)
    assert result3 == True, f"Empty string failed: {result3}"
    print(f"Empty string: ✅")

    # Edge Case 4: Dot pattern
    s4 = "ab"
    p4 = ".*"
    result4 = solution.isMatch(s4, p4)
    assert result4 == True, f"Dot pattern failed: {result4}"
    print(f"Dot pattern: ✅")

    # Edge Case 5: Star pattern
    s5 = "aaa"
    p5 = "a*"
    result5 = solution.isMatch(s5, p5)
    assert result5 == True, f"Star pattern failed: {result5}"
    print(f"Star pattern: ✅")

    # Edge Case 6: No match
    s6 = "abc"
    p6 = "def"
    result6 = solution.isMatch(s6, p6)
    assert result6 == False, f"No match failed: {result6}"
    print(f"No match: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Regular Expression Matching:")

    # Large dataset
    s = "a" * 20
    p = "a*"

    start_time = time.time()
    result = solution.isMatch(s, p)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (s={len(s)}, p={len(p)}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Regular Expression Matching Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isMatch method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

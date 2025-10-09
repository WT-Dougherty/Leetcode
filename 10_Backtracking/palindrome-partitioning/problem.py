"""
Palindrome Partitioning - LeetCode Problem 131

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""

import time
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "aab"
    result1 = solution.partition(s1)
    expected1 = [["a", "a", "b"], ["aa", "b"]]
    assert len(result1) == len(
        expected1
    ), f"Failed for 'aab', expected {len(expected1)} partitions, got {len(result1)}"
    for partition in expected1:
        assert (
            partition in result1
        ), f"Missing partition {partition} in result {result1}"

    # Test Case 2: Single character
    s2 = "a"
    result2 = solution.partition(s2)
    expected2 = [["a"]]
    assert result2 == expected2, f"Failed for 'a', expected {expected2}, got {result2}"

    # Test Case 3: All same characters
    s3 = "aaa"
    result3 = solution.partition(s3)
    expected3 = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    assert len(result3) == len(
        expected3
    ), f"Failed for 'aaa', expected {len(expected3)} partitions, got {len(result3)}"
    for partition in expected3:
        assert (
            partition in result3
        ), f"Missing partition {partition} in result {result3}"

    # Test Case 4: No palindromes except single characters
    s4 = "abc"
    result4 = solution.partition(s4)
    expected4 = [["a", "b", "c"]]
    assert (
        result4 == expected4
    ), f"Failed for 'abc', expected {expected4}, got {result4}"

    # Test Case 5: Palindrome string
    s5 = "aba"
    result5 = solution.partition(s5)
    expected5 = [["a", "b", "a"], ["aba"]]
    assert len(result5) == len(
        expected5
    ), f"Failed for 'aba', expected {len(expected5)} partitions, got {len(result5)}"
    for partition in expected5:
        assert (
            partition in result5
        ), f"Missing partition {partition} in result {result5}"

    # Test Case 6: Longer string
    s6 = "aabb"
    result6 = solution.partition(s6)
    expected6 = [["a", "a", "b", "b"], ["a", "a", "bb"], ["aa", "b", "b"], ["aa", "bb"]]
    assert len(result6) == len(
        expected6
    ), f"Failed for 'aabb', expected {len(expected6)} partitions, got {len(result6)}"
    for partition in expected6:
        assert (
            partition in result6
        ), f"Missing partition {partition} in result {result6}"

    # Test Case 7: Empty string
    s7 = ""
    result7 = solution.partition(s7)
    assert result7 == [[]], f"Failed for empty string, expected [[]], got {result7}"

    # Test Case 8: Two characters
    s8 = "ab"
    result8 = solution.partition(s8)
    expected8 = [["a", "b"]]
    assert result8 == expected8, f"Failed for 'ab', expected {expected8}, got {result8}"

    # Verify all partitions are valid palindromes
    for s in ["aab", "aaa", "abc", "aba", "aabb"]:
        result = solution.partition(s)
        for partition in result:
            # Check that partition reconstructs original string
            reconstructed = "".join(partition)
            assert (
                reconstructed == s
            ), f"Partition {partition} doesn't reconstruct '{s}'"
            # Check that each part is a palindrome
            for part in partition:
                assert part == part[::-1], f"Part '{part}' is not a palindrome"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [5, 8, 10]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        s = "a" * size

        # Test approach
        start_time = time.time()
        result = solution.partition(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} partitions")

    # Verify O(2^N) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(2^N) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = 2 ** (test_sizes[i] - test_sizes[i - 1])
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(2^N): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance for exponential complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(2^N)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(2^N) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(2^N), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(2^N)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 character)
    s1 = "a"
    result1 = solution.partition(s1)
    assert result1 == [["a"]], f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (16 characters)
    s2 = "a" * 16
    result2 = solution.partition(s2)
    assert len(result2) > 0, f"Max constraint failed: {len(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same characters
    s3 = "a" * 10
    result3 = solution.partition(s3)
    assert len(result3) > 0, f"All same characters failed: {len(result3)}"
    print(f"All same characters: ✅")

    # Edge Case 4: No palindromes except single characters
    s4 = "abcdefghij"
    result4 = solution.partition(s4)
    assert len(result4) == 1, f"No palindromes failed: {len(result4)}"
    print(f"No palindromes except single chars: ✅")

    # Edge Case 5: Alternating pattern
    s5 = "abababab"
    result5 = solution.partition(s5)
    assert len(result5) > 0, f"Alternating pattern failed: {len(result5)}"
    print(f"Alternating pattern: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Palindrome Partitioning:")

    # Large dataset
    s = "aabbccddee"

    start_time = time.time()
    result = solution.partition(s)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10 characters):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} partitions")


if __name__ == "__main__":
    print("🧪 Testing Palindrome Partitioning Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the partition method")
        print("- Aim for O(2^N) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(2^N)")
        print("- Consider using backtracking with palindrome checking")

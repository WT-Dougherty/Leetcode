"""
Partition Labels - LeetCode Problem 763

You are given a string s. We want to partition the string into as many parts as
possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in
order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""

import time


class Solution:
    def partitionLabels(self, s):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "ababcbacadefegdehijhklij"
    result1 = solution.partitionLabels(s1)
    expected1 = [9, 7, 8]
    assert (
        result1 == expected1
    ), f"Failed for s='{s1}', expected {expected1}, got {result1}"

    # Test Case 2: Single partition
    s2 = "eccbbbbdec"
    result2 = solution.partitionLabels(s2)
    expected2 = [10]
    assert (
        result2 == expected2
    ), f"Failed for s='{s2}', expected {expected2}, got {result2}"

    # Test Case 3: Each character separate
    s3 = "abcdef"
    result3 = solution.partitionLabels(s3)
    expected3 = [1, 1, 1, 1, 1, 1]
    assert (
        result3 == expected3
    ), f"Failed for s='{s3}', expected {expected3}, got {result3}"

    # Test Case 4: All same characters
    s4 = "aaaa"
    result4 = solution.partitionLabels(s4)
    expected4 = [4]
    assert (
        result4 == expected4
    ), f"Failed for s='{s4}', expected {expected4}, got {result4}"

    # Test Case 5: Two partitions
    s5 = "ababcbacadefegde"
    result5 = solution.partitionLabels(s5)
    expected5 = [9, 7]
    assert (
        result5 == expected5
    ), f"Failed for s='{s5}', expected {expected5}, got {result5}"

    # Test Case 6: Complex case
    s6 = "ababcbacadefegdehijhklij"
    result6 = solution.partitionLabels(s6)
    expected6 = [9, 7, 8]
    assert (
        result6 == expected6
    ), f"Failed for s='{s6}', expected {expected6}, got {result6}"

    # Test Case 7: Edge case
    s7 = "a"
    result7 = solution.partitionLabels(s7)
    expected7 = [1]
    assert (
        result7 == expected7
    ), f"Failed for s='{s7}', expected {expected7}, got {result7}"

    # Test Case 8: Mixed case
    s8 = "ababcbacadefegdehijhklij"
    result8 = solution.partitionLabels(s8)
    expected8 = [9, 7, 8]
    assert (
        result8 == expected8
    ), f"Failed for s='{s8}', expected {expected8}, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - alternating pattern
        s = "ab" * (size // 2) + "a" * (size % 2)

        # Test approach
        start_time = time.time()
        result = solution.partitionLabels(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} partitions")

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

    # Edge Case 1: Single character
    s = "a"
    result = solution.partitionLabels(s)
    print(f"Single character: {result} ✅")

    # Edge Case 2: Two characters
    s = "ab"
    result = solution.partitionLabels(s)
    print(f"Two characters: {result} ✅")

    # Edge Case 3: All same characters
    s = "aaaa"
    result = solution.partitionLabels(s)
    print(f"All same characters: {result} ✅")

    # Edge Case 4: Long string
    s = "a" * 1000
    result = solution.partitionLabels(s)
    print(f"Long string (1000 chars): {len(result)} partitions ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset - alternating pattern
    size = 100000
    s = "ab" * (size // 2)

    start_time = time.time()
    result = solution.partitionLabels(s)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} characters, alternating):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} partitions")

    # Large dataset - all same characters
    s2 = "a" * size

    start_time = time.time()
    result2 = solution.partitionLabels(s2)
    elapsed_time2 = time.time() - start_time

    print(f"\nLarge dataset ({size} characters, all same):")
    print(f"Time: {elapsed_time2:.6f}s, Result: {len(result2)} partitions")


if __name__ == "__main__":
    print("🧪 Testing Partition Labels Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the partitionLabels method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using greedy approach with last occurrence tracking")

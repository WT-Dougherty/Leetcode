"""
Insert Interval - LeetCode Problem 57

You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith
interval and intervals is sorted in ascending order by starti. You are also
given an interval newInterval = [start, end] that represents the start
and end of another interval.

Insert newInterval into intervals such that intervals is still sorted
in ascending order by starti and intervals still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

import time


class Solution:
    def insert(self, intervals, newInterval):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    result1 = solution.insert(intervals1, newInterval1)
    expected1 = [[1, 5], [6, 9]]
    assert (
        result1 == expected1
    ), f"Failed for intervals={intervals1}, newInterval={newInterval1}, expected {expected1}, got {result1}"

    # Test Case 2: Complex case
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    result2 = solution.insert(intervals2, newInterval2)
    expected2 = [[1, 2], [3, 10], [12, 16]]
    assert (
        result2 == expected2
    ), f"Failed for intervals={intervals2}, newInterval={newInterval2}, expected {expected2}, got {result2}"

    # Test Case 3: Empty intervals
    intervals3 = []
    newInterval3 = [5, 7]
    result3 = solution.insert(intervals3, newInterval3)
    expected3 = [[5, 7]]
    assert (
        result3 == expected3
    ), f"Failed for intervals={intervals3}, newInterval={newInterval3}, expected {expected3}, got {result3}"

    # Test Case 4: No overlap
    intervals4 = [[1, 2], [3, 4]]
    newInterval4 = [5, 6]
    result4 = solution.insert(intervals4, newInterval4)
    expected4 = [[1, 2], [3, 4], [5, 6]]
    assert (
        result4 == expected4
    ), f"Failed for intervals={intervals4}, newInterval={newInterval4}, expected {expected4}, got {result4}"

    # Test Case 5: Complete overlap
    intervals5 = [[1, 5]]
    newInterval5 = [2, 3]
    result5 = solution.insert(intervals5, newInterval5)
    expected5 = [[1, 5]]
    assert (
        result5 == expected5
    ), f"Failed for intervals={intervals5}, newInterval={newInterval5}, expected {expected5}, got {result5}"

    # Test Case 6: Edge case
    intervals6 = [[1, 3], [6, 9]]
    newInterval6 = [4, 5]
    result6 = solution.insert(intervals6, newInterval6)
    expected6 = [[1, 3], [4, 5], [6, 9]]
    assert (
        result6 == expected6
    ), f"Failed for intervals={intervals6}, newInterval={newInterval6}, expected {expected6}, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        intervals = [[i, i + 1] for i in range(0, size, 2)]
        newInterval = [size // 2, size // 2 + 1]

        start_time = time.time()
        result = solution.insert(intervals, newInterval)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} intervals")

    # Verify O(n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Empty intervals
    intervals = []
    newInterval = [1, 2]
    result = solution.insert(intervals, newInterval)
    print(f"Empty intervals: {result} ✅")

    # Edge Case 2: Single interval
    intervals = [[1, 2]]
    newInterval = [3, 4]
    result = solution.insert(intervals, newInterval)
    print(f"Single interval: {result} ✅")

    # Edge Case 3: Large values
    intervals = [[1000000, 1000001]]
    newInterval = [1000002, 1000003]
    result = solution.insert(intervals, newInterval)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 100000
    intervals = [[i, i + 1] for i in range(0, size, 2)]
    newInterval = [size // 2, size // 2 + 1]

    start_time = time.time()
    result = solution.insert(intervals, newInterval)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} intervals):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} intervals")


if __name__ == "__main__":
    print("🧪 Testing Insert Interval Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the insert method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using linear scan with merge logic")

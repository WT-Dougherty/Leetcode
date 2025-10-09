"""
Merge Intervals - LeetCode Problem 56

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.
"""

import time


class Solution:
    def merge(self, intervals):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = solution.merge(intervals1)
    expected1 = [[1, 6], [8, 10], [15, 18]]
    assert (
        result1 == expected1
    ), f"Failed for intervals={intervals1}, expected {expected1}, got {result1}"

    # Test Case 2: Adjacent intervals
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    expected2 = [[1, 5]]
    assert (
        result2 == expected2
    ), f"Failed for intervals={intervals2}, expected {expected2}, got {result2}"

    # Test Case 3: Single interval
    intervals3 = [[1, 4]]
    result3 = solution.merge(intervals3)
    expected3 = [[1, 4]]
    assert (
        result3 == expected3
    ), f"Failed for intervals={intervals3}, expected {expected3}, got {result3}"

    # Test Case 4: No overlaps
    intervals4 = [[1, 2], [3, 4], [5, 6]]
    result4 = solution.merge(intervals4)
    expected4 = [[1, 2], [3, 4], [5, 6]]
    assert (
        result4 == expected4
    ), f"Failed for intervals={intervals4}, expected {expected4}, got {result4}"

    # Test Case 5: All merge into one
    intervals5 = [[1, 4], [2, 3]]
    result5 = solution.merge(intervals5)
    expected5 = [[1, 4]]
    assert (
        result5 == expected5
    ), f"Failed for intervals={intervals5}, expected {expected5}, got {result5}"

    # Test Case 6: Complex case
    intervals6 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result6 = solution.merge(intervals6)
    expected6 = [[1, 6], [8, 10], [15, 18]]
    assert (
        result6 == expected6
    ), f"Failed for intervals={intervals6}, expected {expected6}, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n * log n)"""
    solution = Solution()

    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        intervals = [[i, i + 1] for i in range(size)]

        start_time = time.time()
        result = solution.merge(intervals)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} intervals")

    # Verify O(n * log n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * (test_sizes[i - 1].bit_length())
            curr_complexity = test_sizes[i] * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n * log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n * log n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n * log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * log n)")
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
    result = solution.merge(intervals)
    print(f"Empty intervals: {result} ✅")

    # Edge Case 2: Single interval
    intervals = [[1, 2]]
    result = solution.merge(intervals)
    print(f"Single interval: {result} ✅")

    # Edge Case 3: Large values
    intervals = [[1000000, 1000001], [1000002, 1000003]]
    result = solution.merge(intervals)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 10000
    intervals = [[i, i + 1] for i in range(size)]

    start_time = time.time()
    result = solution.merge(intervals)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} intervals):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} intervals")


if __name__ == "__main__":
    print("🧪 Testing Merge Intervals Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the merge method")
        print("- Aim for O(n * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n)")
        print("- Consider using sorting approach")

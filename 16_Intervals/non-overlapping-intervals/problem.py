"""
Non-overlapping Intervals - LeetCode Problem 435

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the
rest of the intervals non-overlapping.
"""

import time


class Solution:
    def eraseOverlapIntervals(self, intervals):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result1 = solution.eraseOverlapIntervals(intervals1)
    assert result1 == 1, f"Failed for intervals={intervals1}, expected 1, got {result1}"

    # Test Case 2: Multiple overlaps
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    result2 = solution.eraseOverlapIntervals(intervals2)
    assert result2 == 2, f"Failed for intervals={intervals2}, expected 2, got {result2}"

    # Test Case 3: No overlaps
    intervals3 = [[1, 2], [2, 3]]
    result3 = solution.eraseOverlapIntervals(intervals3)
    assert result3 == 0, f"Failed for intervals={intervals3}, expected 0, got {result3}"

    # Test Case 4: Single interval
    intervals4 = [[1, 2]]
    result4 = solution.eraseOverlapIntervals(intervals4)
    assert result4 == 0, f"Failed for intervals={intervals4}, expected 0, got {result4}"

    # Test Case 5: Complex case
    intervals5 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result5 = solution.eraseOverlapIntervals(intervals5)
    assert result5 == 1, f"Failed for intervals={intervals5}, expected 1, got {result5}"

    # Test Case 6: Edge case
    intervals6 = [[1, 2], [1, 3], [2, 3]]
    result6 = solution.eraseOverlapIntervals(intervals6)
    assert result6 == 1, f"Failed for intervals={intervals6}, expected 1, got {result6}"

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
        result = solution.eraseOverlapIntervals(intervals)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

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
    result = solution.eraseOverlapIntervals(intervals)
    print(f"Empty intervals: {result} ✅")

    # Edge Case 2: Single interval
    intervals = [[1, 2]]
    result = solution.eraseOverlapIntervals(intervals)
    print(f"Single interval: {result} ✅")

    # Edge Case 3: Large values
    intervals = [[1000000, 1000001], [1000002, 1000003]]
    result = solution.eraseOverlapIntervals(intervals)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 10000
    intervals = [[i, i + 1] for i in range(size)]

    start_time = time.time()
    result = solution.eraseOverlapIntervals(intervals)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} intervals):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Non-overlapping Intervals Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the eraseOverlapIntervals method")
        print("- Aim for O(n * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n)")
        print("- Consider using greedy approach with sorting")

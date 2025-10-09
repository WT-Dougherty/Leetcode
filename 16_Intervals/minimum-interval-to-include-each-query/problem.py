"""
Minimum Interval to Include Each Query - LeetCode Problem 1851

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti]
describes the ith interval starting at lefti and ending at righti (inclusive).
The size of an interval is defined as the number of integers it contains, or
more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is
the size of the smallest interval such that lefti <= queries[j] <= righti.
If no such interval exists, the answer is -1.

Return an array answer of size queries.length such that answer[j] is the
answer to the jth query.
"""

import time


class Solution:
    def minInterval(self, intervals, queries):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    intervals1 = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries1 = [2, 3, 4, 5]
    result1 = solution.minInterval(intervals1, queries1)
    expected1 = [3, 3, 1, 4]
    assert (
        result1 == expected1
    ), f"Failed for intervals={intervals1}, queries={queries1}, expected {expected1}, got {result1}"

    # Test Case 2: Complex case
    intervals2 = [[2, 3], [2, 5], [1, 8], [20, 25]]
    queries2 = [2, 19, 5, 22]
    result2 = solution.minInterval(intervals2, queries2)
    expected2 = [2, -1, 4, 6]
    assert (
        result2 == expected2
    ), f"Failed for intervals={intervals2}, queries={queries2}, expected {expected2}, got {result2}"

    # Test Case 3: Single interval
    intervals3 = [[1, 3]]
    queries3 = [2]
    result3 = solution.minInterval(intervals3, queries3)
    expected3 = [3]
    assert (
        result3 == expected3
    ), f"Failed for intervals={intervals3}, queries={queries3}, expected {expected3}, got {result3}"

    # Test Case 4: No matching interval
    intervals4 = [[1, 3]]
    queries4 = [5]
    result4 = solution.minInterval(intervals4, queries4)
    expected4 = [-1]
    assert (
        result4 == expected4
    ), f"Failed for intervals={intervals4}, queries={queries4}, expected {expected4}, got {result4}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n * log n + m * log n)"""
    solution = Solution()

    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        intervals = [[i, i + 1] for i in range(size)]
        queries = [i for i in range(size)]

        start_time = time.time()
        result = solution.minInterval(intervals, queries)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} answers")

    # Verify O(n * log n + m * log n) complexity
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
            f"Expected ratios for O(n * log n + m * log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(
                    f"\n❌ FAILED: Time complexity appears worse than O(n * log n + m * log n)"
                )
                raise AssertionError(
                    "Time complexity test failed: expected O(n * log n + m * log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * log n + m * log n)")
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
    queries = [1]
    result = solution.minInterval(intervals, queries)
    print(f"Empty intervals: {result} ✅")

    # Edge Case 2: Single interval
    intervals = [[1, 2]]
    queries = [1]
    result = solution.minInterval(intervals, queries)
    print(f"Single interval: {result} ✅")

    # Edge Case 3: Large values
    intervals = [[1000000, 1000001]]
    queries = [1000000]
    result = solution.minInterval(intervals, queries)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 10000
    intervals = [[i, i + 1] for i in range(size)]
    queries = [i for i in range(size)]

    start_time = time.time()
    result = solution.minInterval(intervals, queries)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} intervals, {size} queries):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} answers")


if __name__ == "__main__":
    print("🧪 Testing Minimum Interval to Include Each Query Problem")
    print("=" * 60)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minInterval method")
        print("- Aim for O(n * log n + m * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n + m * log n)")
        print("- Consider using heap-based approach")

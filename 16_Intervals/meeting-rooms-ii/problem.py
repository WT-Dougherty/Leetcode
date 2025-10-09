"""
Meeting Rooms II - LeetCode Problem 253

Given an array of meeting time intervals intervals where
intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

import time


class Solution:
    def minMeetingRooms(self, intervals):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Overlapping meetings
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    result1 = solution.minMeetingRooms(intervals1)
    assert result1 == 2, f"Failed for intervals={intervals1}, expected 2, got {result1}"

    # Test Case 2: Non-overlapping meetings
    intervals2 = [[7, 10], [2, 4]]
    result2 = solution.minMeetingRooms(intervals2)
    assert result2 == 1, f"Failed for intervals={intervals2}, expected 1, got {result2}"

    # Test Case 3: Single meeting
    intervals3 = [[13, 15]]
    result3 = solution.minMeetingRooms(intervals3)
    assert result3 == 1, f"Failed for intervals={intervals3}, expected 1, got {result3}"

    # Test Case 4: Empty intervals
    intervals4 = []
    result4 = solution.minMeetingRooms(intervals4)
    assert result4 == 0, f"Failed for intervals={intervals4}, expected 0, got {result4}"

    # Test Case 5: Adjacent meetings
    intervals5 = [[1, 2], [2, 3], [3, 4]]
    result5 = solution.minMeetingRooms(intervals5)
    assert result5 == 1, f"Failed for intervals={intervals5}, expected 1, got {result5}"

    # Test Case 6: Complex case
    intervals6 = [[1, 3], [2, 4], [3, 5]]
    result6 = solution.minMeetingRooms(intervals6)
    assert result6 == 2, f"Failed for intervals={intervals6}, expected 2, got {result6}"

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
        result = solution.minMeetingRooms(intervals)
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
    result = solution.minMeetingRooms(intervals)
    print(f"Empty intervals: {result} ✅")

    # Edge Case 2: Single meeting
    intervals = [[1, 2]]
    result = solution.minMeetingRooms(intervals)
    print(f"Single meeting: {result} ✅")

    # Edge Case 3: Same start and end
    intervals = [[1, 1], [2, 2]]
    result = solution.minMeetingRooms(intervals)
    print(f"Same start and end: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 10000
    intervals = [[i, i + 1] for i in range(size)]

    start_time = time.time()
    result = solution.minMeetingRooms(intervals)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} intervals):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Meeting Rooms II Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minMeetingRooms method")
        print("- Aim for O(n * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n)")
        print("- Consider using heap-based approach")

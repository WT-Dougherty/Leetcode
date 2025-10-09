"""
Daily Temperatures - LeetCode Problem 739

Given an array of integers temperatures represents the daily temperatures, return an array
answer such that answer[i] is the number of days you have to wait after the ith day to
get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""

import time
import random


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.dailyTemperatures(temps1)
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert (
        result1 == expected1
    ), f"Failed for {temps1}, expected {expected1}, got {result1}"

    # Test Case 2: Increasing temperatures
    temps2 = [30, 40, 50, 60]
    result2 = solution.dailyTemperatures(temps2)
    expected2 = [1, 1, 1, 0]
    assert (
        result2 == expected2
    ), f"Failed for {temps2}, expected {expected2}, got {result2}"

    # Test Case 3: Decreasing temperatures
    temps3 = [30, 60, 90]
    result3 = solution.dailyTemperatures(temps3)
    expected3 = [1, 1, 0]
    assert (
        result3 == expected3
    ), f"Failed for {temps3}, expected {expected3}, got {result3}"

    # Test Case 4: Single element
    temps4 = [30]
    result4 = solution.dailyTemperatures(temps4)
    expected4 = [0]
    assert (
        result4 == expected4
    ), f"Failed for {temps4}, expected {expected4}, got {result4}"

    # Test Case 5: All same temperatures
    temps5 = [50, 50, 50, 50]
    result5 = solution.dailyTemperatures(temps5)
    expected5 = [0, 0, 0, 0]
    assert (
        result5 == expected5
    ), f"Failed for {temps5}, expected {expected5}, got {result5}"

    # Test Case 6: Decreasing then increasing
    temps6 = [70, 60, 50, 60, 70]
    result6 = solution.dailyTemperatures(temps6)
    expected6 = [0, 2, 1, 1, 0]
    assert (
        result6 == expected6
    ), f"Failed for {temps6}, expected {expected6}, got {result6}"

    # Test Case 7: Edge case with minimum constraint
    temps7 = [30, 31]
    result7 = solution.dailyTemperatures(temps7)
    expected7 = [1, 0]
    assert (
        result7 == expected7
    ), f"Failed for {temps7}, expected {expected7}, got {result7}"

    # Test Case 8: Edge case with maximum constraint
    temps8 = [99, 100]
    result8 = solution.dailyTemperatures(temps8)
    expected8 = [1, 0]
    assert (
        result8 == expected8
    ), f"Failed for {temps8}, expected {expected8}, got {result8}"

    # Test Case 9: Complex case
    temps9 = [34, 80, 80, 34, 34, 80, 80, 80, 80, 34]
    result9 = solution.dailyTemperatures(temps9)
    expected9 = [1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    assert (
        result9 == expected9
    ), f"Failed for {temps9}, expected {expected9}, got {result9}"

    # Test Case 10: Alternating pattern
    temps10 = [50, 60, 50, 60, 50]
    result10 = solution.dailyTemperatures(temps10)
    expected10 = [1, 0, 1, 0, 0]
    assert (
        result10 == expected10
    ), f"Failed for {temps10}, expected {expected10}, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tMax Wait")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        temperatures = [random.randint(30, 100) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.dailyTemperatures(temperatures)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        max_wait = max(result) if result else 0
        print(f"{size}\t{elapsed_time:.6f}s\t{max_wait}")

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

    # Edge Case 1: Maximum constraint length
    temperatures = [random.randint(30, 100) for _ in range(100000)]
    result = solution.dailyTemperatures(temperatures)
    print(f"Maximum length (100k elements): {len(result)} ✅")

    # Edge Case 2: Maximum constraint values
    temperatures = [100] * 1000
    result = solution.dailyTemperatures(temperatures)
    assert all(x == 0 for x in result)
    print(f"Maximum constraint values: {len(result)} ✅")

    # Edge Case 3: Minimum constraint values
    temperatures = [30] * 1000
    result = solution.dailyTemperatures(temperatures)
    assert all(x == 0 for x in result)
    print(f"Minimum constraint values: {len(result)} ✅")

    # Edge Case 4: Strictly increasing
    temperatures = list(range(30, 131))
    result = solution.dailyTemperatures(temperatures)
    expected = [1] * 100 + [0]
    assert result == expected
    print(f"Strictly increasing: {len(result)} ✅")

    # Edge Case 5: Strictly decreasing
    temperatures = list(range(100, 29, -1))
    result = solution.dailyTemperatures(temperatures)
    expected = [0] * 71
    assert result == expected
    print(f"Strictly decreasing: {len(result)} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    temperatures = [random.randint(30, 100) for _ in range(100000)]

    start_time = time.time()
    result = solution.dailyTemperatures(temperatures)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Max wait: {max(result)}")


if __name__ == "__main__":
    print("🧪 Testing Daily Temperatures Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the dailyTemperatures method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use monotonic stack")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using monotonic stack")

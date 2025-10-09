"""
Largest Rectangle in Histogram - LeetCode Problem 84

Given an array of integers heights representing the histogram's bar height where the width
of each bar is 1, return the area of the largest rectangle in the histogram.
"""

import time
import random
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    heights1 = [2, 1, 5, 6, 2, 3]
    result1 = solution.largestRectangleArea(heights1)
    assert result1 == 10, f"Failed for heights={heights1}, expected 10, got {result1}"

    # Test Case 2: Simple case
    heights2 = [2, 4]
    result2 = solution.largestRectangleArea(heights2)
    assert result2 == 4, f"Failed for heights={heights2}, expected 4, got {result2}"

    # Test Case 3: Single element
    heights3 = [5]
    result3 = solution.largestRectangleArea(heights3)
    assert result3 == 5, f"Failed for heights={heights3}, expected 5, got {result3}"

    # Test Case 4: All same heights
    heights4 = [3, 3, 3, 3]
    result4 = solution.largestRectangleArea(heights4)
    assert result4 == 12, f"Failed for heights={heights4}, expected 12, got {result4}"

    # Test Case 5: Increasing heights
    heights5 = [1, 2, 3, 4, 5]
    result5 = solution.largestRectangleArea(heights5)
    assert result5 == 9, f"Failed for heights={heights5}, expected 9, got {result5}"

    # Test Case 6: Decreasing heights
    heights6 = [5, 4, 3, 2, 1]
    result6 = solution.largestRectangleArea(heights6)
    assert result6 == 9, f"Failed for heights={heights6}, expected 9, got {result6}"

    # Test Case 7: Zero heights
    heights7 = [0, 0, 0]
    result7 = solution.largestRectangleArea(heights7)
    assert result7 == 0, f"Failed for heights={heights7}, expected 0, got {result7}"

    # Test Case 8: Mixed with zeros
    heights8 = [0, 2, 0]
    result8 = solution.largestRectangleArea(heights8)
    assert result8 == 2, f"Failed for heights={heights8}, expected 2, got {result8}"

    # Test Case 9: Complex case
    heights9 = [6, 2, 5, 4, 5, 1, 6]
    result9 = solution.largestRectangleArea(heights9)
    assert result9 == 12, f"Failed for heights={heights9}, expected 12, got {result9}"

    # Test Case 10: Edge case with minimum constraint
    heights10 = [1]
    result10 = solution.largestRectangleArea(heights10)
    assert result10 == 1, f"Failed for heights={heights10}, expected 1, got {result10}"

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
        # Generate test data
        heights = [random.randint(0, 1000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.largestRectangleArea(heights)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

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
    heights = [random.randint(0, 10000) for _ in range(100000)]
    result = solution.largestRectangleArea(heights)
    print(f"Maximum length (100k elements): {result} ✅")

    # Edge Case 2: Maximum constraint values
    heights = [10000] * 1000
    result = solution.largestRectangleArea(heights)
    assert result == 10000000
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    heights = [0] * 1000
    result = solution.largestRectangleArea(heights)
    assert result == 0
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All same heights
    heights = [5] * 10000
    result = solution.largestRectangleArea(heights)
    assert result == 50000
    print(f"All same heights: {result} ✅")

    # Edge Case 5: Alternating pattern
    heights = [1, 0] * 5000
    result = solution.largestRectangleArea(heights)
    assert result == 5000
    print(f"Alternating pattern: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    heights = [random.randint(0, 1000) for _ in range(100000)]

    start_time = time.time()
    result = solution.largestRectangleArea(heights)
    time1 = time.time() - start_time

    print(f"Large dataset (100k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Largest Rectangle in Histogram Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the largestRectangleArea method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use stack data structure")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using stack data structure")

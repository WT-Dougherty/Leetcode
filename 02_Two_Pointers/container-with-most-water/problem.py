"""
Container With Most Water - LeetCode Problem 11

You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

import time
import random
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.maxArea(height1)
    assert result1 == 49, f"Failed for {height1}, expected 49, got {result1}"

    # Test Case 2: Minimum length
    height2 = [1, 1]
    result2 = solution.maxArea(height2)
    assert result2 == 1, f"Failed for {height2}, expected 1, got {result2}"

    # Test Case 3: Increasing heights
    height3 = [1, 2, 3, 4, 5]
    result3 = solution.maxArea(height3)
    assert result3 == 6, f"Failed for {height3}, expected 6, got {result3}"

    # Test Case 4: Decreasing heights
    height4 = [5, 4, 3, 2, 1]
    result4 = solution.maxArea(height4)
    assert result4 == 6, f"Failed for {height4}, expected 6, got {result4}"

    # Test Case 5: All same heights
    height5 = [3, 3, 3, 3]
    result5 = solution.maxArea(height5)
    assert result5 == 9, f"Failed for {height5}, expected 9, got {result5}"

    # Test Case 6: Single peak
    height6 = [1, 2, 1]
    result6 = solution.maxArea(height6)
    assert result6 == 2, f"Failed for {height6}, expected 2, got {result6}"

    # Test Case 7: Two peaks
    height7 = [1, 3, 2, 5, 25, 24, 5]
    result7 = solution.maxArea(height7)
    assert result7 == 24, f"Failed for {height7}, expected 24, got {result7}"

    # Test Case 8: Edge case with zeros
    height8 = [0, 2, 0]
    result8 = solution.maxArea(height8)
    assert result8 == 0, f"Failed for {height8}, expected 0, got {result8}"

    # Test Case 9: Large numbers
    height9 = [10000, 1, 10000]
    result9 = solution.maxArea(height9)
    assert result9 == 20000, f"Failed for {height9}, expected 20000, got {result9}"

    # Test Case 10: Complex case
    height10 = [2, 3, 4, 5, 18, 17, 6]
    result10 = solution.maxArea(height10)
    assert result10 == 17, f"Failed for {height10}, expected 17, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tMax Area")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        height = [random.randint(0, 10000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.maxArea(height)
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

            if not (min_expected <= actual <= max_expected):
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

    # Edge Case 1: Minimum length
    height = [1, 1]
    result = solution.maxArea(height)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    height = [10000] * 100000
    result = solution.maxArea(height)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: All zeros
    height = [0] * 1000
    result = solution.maxArea(height)
    print(f"All zeros: {result} ✅")

    # Edge Case 4: Alternating pattern
    height = [1, 10000] * 500
    result = solution.maxArea(height)
    print(f"Alternating pattern: {result} ✅")

    # Edge Case 5: Single peak in middle
    height = [1] * 500 + [10000] + [1] * 500
    result = solution.maxArea(height)
    print(f"Single peak in middle: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    height = [random.randint(0, 10000) for _ in range(100000)]

    start_time = time.time()
    result = solution.maxArea(height)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Max area: {result}")


if __name__ == "__main__":
    print("🧪 Testing Container With Most Water Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxArea method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two pointers approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using two pointers from both ends")

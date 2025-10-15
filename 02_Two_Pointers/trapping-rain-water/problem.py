"""
Trapping Rain Water - LeetCode Problem 42

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

import time
import random
from typing import List

import math


class Solution:
    def trap(self, height: List[int]) -> int:
        """Algorithm v2:

        left, right = 0, 1
        area = 0
        while left < len(height) - 1:
            # search for an end to the current left edge
            while height[right] < height[left]:
                right += 1

                # condition: we didn't find a right edge
                if right == len(height):
                    right = left + 1
                    break

            # if we found a bucket, add to area; else, continue search for buckets
            if right != left + 1:
                area += (right - left - 1) * min(height[left], height[right]) - sum(
                    height[left + 1 : right]
                )
                left = right
                right += 1
            else:
                left += 1
                right = left + 1

        return area

        Problem: buckets with the limiting edge on the right are not detected.
        I need a way to keep track of the max & corresponding index on the right,
        and check that it creates a bucket w/ the left edge
        """

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        area = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]

        return area


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution.trap(height1)
    assert result1 == 6, f"Failed for {height1}, expected 6, got {result1}"

    # Test Case 2: Another basic case
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = solution.trap(height2)
    assert result2 == 9, f"Failed for {height2}, expected 9, got {result2}"

    # Test Case 3: No water trapped
    height3 = [3, 2, 1]
    result3 = solution.trap(height3)
    assert result3 == 0, f"Failed for {height3}, expected 0, got {result3}"

    # Test Case 4: Single element
    height4 = [1]
    result4 = solution.trap(height4)
    assert result4 == 0, f"Failed for {height4}, expected 0, got {result4}"

    # Test Case 5: Two elements
    height5 = [1, 2]
    result5 = solution.trap(height5)
    assert result5 == 0, f"Failed for {height5}, expected 0, got {result5}"

    # Test Case 6: All same height
    height6 = [2, 2, 2, 2]
    result6 = solution.trap(height6)
    assert result6 == 0, f"Failed for {height6}, expected 0, got {result6}"

    # Test Case 7: Increasing heights
    height7 = [1, 2, 3, 4, 5]
    result7 = solution.trap(height7)
    assert result7 == 0, f"Failed for {height7}, expected 0, got {result7}"

    # Test Case 8: Decreasing heights
    height8 = [5, 4, 3, 2, 1]
    result8 = solution.trap(height8)
    assert result8 == 0, f"Failed for {height8}, expected 0, got {result8}"

    # Test Case 9: Complex case
    height9 = [3, 0, 2, 0, 4]
    result9 = solution.trap(height9)
    assert result9 == 7, f"Failed for {height9}, expected 7, got {result9}"

    # Test Case 10: Smaller right edge
    height10 = [4, 2, 3]
    result10 = solution.trap(height10)
    assert result10 == 1, f"Failed for {height10}, expected 1, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 20000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tWater Trapped")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        height = [random.randint(0, 100000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.trap(height)
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

    # Edge Case 1: Minimum length
    height = [1]
    result = solution.trap(height)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    height = [100000] * 20000
    result = solution.trap(height)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: All zeros
    height = [0] * 1000
    result = solution.trap(height)
    print(f"All zeros: {result} ✅")

    # Edge Case 4: Alternating pattern
    height = [1, 0] * 1000
    result = solution.trap(height)
    print(f"Alternating pattern: {result} ✅")

    # Edge Case 5: Single peak
    height = [1] * 500 + [100000] + [1] * 500
    result = solution.trap(height)
    print(f"Single peak: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    height = [random.randint(0, 100000) for _ in range(20000)]

    start_time = time.time()
    result = solution.trap(height)
    time1 = time.time() - start_time

    print(f"Large dataset (20,000 elements):")
    print(f"Time: {time1:.6f}s, Water trapped: {result}")


if __name__ == "__main__":
    print("🧪 Testing Trapping Rain Water Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the trap method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two pointers or stack approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using two pointers or stack")

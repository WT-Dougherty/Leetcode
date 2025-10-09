"""
Maximum Product Subarray - LeetCode Problem 152

Given an integer array nums, find a contiguous non-empty subarray within
the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous part of an array.
"""

import time
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [2, 3, -2, 4]
    result1 = solution.maxProduct(nums1)
    assert result1 == 6, f"Failed for {nums1}, expected 6, got {result1}"

    # Test Case 2: With zero
    nums2 = [-2, 0, -1]
    result2 = solution.maxProduct(nums2)
    assert result2 == 0, f"Failed for {nums2}, expected 0, got {result2}"

    # Test Case 3: Single element
    nums3 = [5]
    result3 = solution.maxProduct(nums3)
    assert result3 == 5, f"Failed for {nums3}, expected 5, got {result3}"

    # Test Case 4: All negative
    nums4 = [-2, -3, -4]
    result4 = solution.maxProduct(nums4)
    assert result4 == 12, f"Failed for {nums4}, expected 12, got {result4}"

    # Test Case 5: All positive
    nums5 = [1, 2, 3, 4]
    result5 = solution.maxProduct(nums5)
    assert result5 == 24, f"Failed for {nums5}, expected 24, got {result5}"

    # Test Case 6: Mixed case
    nums6 = [2, -5, -2, -4, 3]
    result6 = solution.maxProduct(nums6)
    assert result6 == 24, f"Failed for {nums6}, expected 24, got {result6}"

    # Test Case 7: Complex case
    nums7 = [-1, -2, -9, -6]
    result7 = solution.maxProduct(nums7)
    assert result7 == 108, f"Failed for {nums7}, expected 108, got {result7}"

    # Test Case 8: Edge case
    nums8 = [0, 2]
    result8 = solution.maxProduct(nums8)
    assert result8 == 2, f"Failed for {nums8}, expected 2, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with mixed values
        nums = [i % 21 - 10 for i in range(size)]  # Values from -10 to 10

        # Test approach
        start_time = time.time()
        result = solution.maxProduct(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity
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

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n) complexity")
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

    # Edge Case 1: Minimum constraint (1 element)
    nums1 = [10]
    result1 = solution.maxProduct(nums1)
    assert result1 == 10, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (20000 elements)
    nums2 = [i % 21 - 10 for i in range(20000)]
    result2 = solution.maxProduct(nums2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (10)
    nums3 = [10, 10, 10]
    result3 = solution.maxProduct(nums3)
    assert result3 == 1000, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (-10)
    nums4 = [-10, -10, -10]
    result4 = solution.maxProduct(nums4)
    assert result4 == -1000, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All zeros
    nums5 = [0, 0, 0, 0]
    result5 = solution.maxProduct(nums5)
    assert result5 == 0, f"All zeros failed: {result5}"
    print(f"All zeros: ✅")

    # Edge Case 6: Single negative
    nums6 = [-5]
    result6 = solution.maxProduct(nums6)
    assert result6 == -5, f"Single negative failed: {result6}"
    print(f"Single negative: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Maximum Product Subarray:")

    # Large dataset
    nums = [i % 21 - 10 for i in range(1000)]

    start_time = time.time()
    result = solution.maxProduct(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 elements):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Maximum Product Subarray Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxProduct method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming with tracking min/max")

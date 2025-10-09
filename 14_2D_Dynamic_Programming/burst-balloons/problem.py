"""
Burst Balloons - LeetCode Problem 312

You have n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it
represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon
with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""

import time
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [3, 1, 5, 8]
    result1 = solution.maxCoins(nums1)
    assert result1 == 167, f"Failed for {nums1}, expected 167, got {result1}"

    # Test Case 2: Two balloons
    nums2 = [1, 5]
    result2 = solution.maxCoins(nums2)
    assert result2 == 10, f"Failed for {nums2}, expected 10, got {result2}"

    # Test Case 3: Single balloon
    nums3 = [5]
    result3 = solution.maxCoins(nums3)
    assert result3 == 5, f"Failed for {nums3}, expected 5, got {result3}"

    # Test Case 4: Three balloons
    nums4 = [3, 1, 5]
    result4 = solution.maxCoins(nums4)
    assert result4 == 35, f"Failed for {nums4}, expected 35, got {result4}"

    # Test Case 5: All same values
    nums5 = [2, 2, 2]
    result5 = solution.maxCoins(nums5)
    assert result5 == 12, f"Failed for {nums5}, expected 12, got {result5}"

    # Test Case 6: Increasing values
    nums6 = [1, 2, 3, 4]
    result6 = solution.maxCoins(nums6)
    assert result6 == 40, f"Failed for {nums6}, expected 40, got {result6}"

    # Test Case 7: Complex case
    nums7 = [7, 9, 8, 0, 2, 1, 3, 5, 2, 2]
    result7 = solution.maxCoins(nums7)
    assert result7 == 1654, f"Failed for {nums7}, expected 1654, got {result7}"

    # Test Case 8: Edge case
    nums8 = [1, 2]
    result8 = solution.maxCoins(nums8)
    assert result8 == 4, f"Failed for {nums8}, expected 4, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 20, 30]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with random values
        nums = [i % 100 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.maxCoins(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n^3) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n^3) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] / test_sizes[i - 1]) ** 3
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n^3): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 3.0  # Allow 300% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^3)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n^3) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n^3), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^3)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 balloon)
    nums1 = [100]
    result1 = solution.maxCoins(nums1)
    assert result1 == 100, f"Single balloon failed: {result1}"
    print(f"Single balloon: ✅")

    # Edge Case 2: Maximum constraint (300 balloons)
    nums2 = [i % 100 + 1 for i in range(300)]
    result2 = solution.maxCoins(nums2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (100)
    nums3 = [100, 100, 100]
    result3 = solution.maxCoins(nums3)
    assert result3 == 10200, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (0)
    nums4 = [0, 0, 0]
    result4 = solution.maxCoins(nums4)
    assert result4 == 0, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All zeros
    nums5 = [0] * 10
    result5 = solution.maxCoins(nums5)
    assert result5 == 0, f"All zeros failed: {result5}"
    print(f"All zeros: ✅")

    # Edge Case 6: Two balloons
    nums6 = [1, 2]
    result6 = solution.maxCoins(nums6)
    assert result6 == 4, f"Two balloons failed: {result6}"
    print(f"Two balloons: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Burst Balloons:")

    # Large dataset
    nums = [i % 10 + 1 for i in range(50)]

    start_time = time.time()
    result = solution.maxCoins(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (50 balloons):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Burst Balloons Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxCoins method")
        print("- Aim for O(n^3) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^3)")
        print("- Consider using dynamic programming with memoization")

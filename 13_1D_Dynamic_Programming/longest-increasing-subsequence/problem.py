"""
Longest Increasing Subsequence - LeetCode Problem 300

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no
elements without changing the order of the remaining elements. For example,
[3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""

import time
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            j = 0
            while j < i:
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                j += 1
        return max(dp)


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result1 = solution.lengthOfLIS(nums1)
    assert result1 == 4, f"Failed for {nums1}, expected 4, got {result1}"

    # Test Case 2: Another case
    nums2 = [0, 1, 0, 3, 2, 3]
    result2 = solution.lengthOfLIS(nums2)
    assert result2 == 4, f"Failed for {nums2}, expected 4, got {result2}"

    # Test Case 3: All same values
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    result3 = solution.lengthOfLIS(nums3)
    assert result3 == 1, f"Failed for {nums3}, expected 1, got {result3}"

    # Test Case 4: Single element
    nums4 = [0]
    result4 = solution.lengthOfLIS(nums4)
    assert result4 == 1, f"Failed for {nums4}, expected 1, got {result4}"

    # Test Case 5: Decreasing sequence
    nums5 = [3, 2, 1]
    result5 = solution.lengthOfLIS(nums5)
    assert result5 == 1, f"Failed for {nums5}, expected 1, got {result5}"

    # Test Case 6: Increasing sequence
    nums6 = [1, 2, 3, 4, 5]
    result6 = solution.lengthOfLIS(nums6)
    assert result6 == 5, f"Failed for {nums6}, expected 5, got {result6}"

    # Test Case 7: Complex case
    nums7 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    result7 = solution.lengthOfLIS(nums7)
    assert result7 == 6, f"Failed for {nums7}, expected 6, got {result7}"

    # Test Case 8: Edge case
    nums8 = [2, 2, 2, 2, 2]
    result8 = solution.lengthOfLIS(nums8)
    assert result8 == 1, f"Failed for {nums8}, expected 1, got {result8}"

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
        # Generate test data - create array with random values
        nums = [i % 100 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.lengthOfLIS(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * log n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n * log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * (test_sizes[i - 1].bit_length())
            curr_complexity = test_sizes[i] * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n*log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n * log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n * log n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n * log n), but got worse complexity"
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

    # Edge Case 1: Minimum constraint (1 element)
    nums1 = [0]
    result1 = solution.lengthOfLIS(nums1)
    assert result1 == 1, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (2500 elements)
    nums2 = [i % 1000 for i in range(2500)]
    result2 = solution.lengthOfLIS(nums2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (10^4)
    nums3 = [10000, 1, 2, 3]
    result3 = solution.lengthOfLIS(nums3)
    assert result3 == 3, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (-10^4)
    nums4 = [-10000, -9999, -9998]
    result4 = solution.lengthOfLIS(nums4)
    assert result4 == 3, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All negative
    nums5 = [-5, -4, -3, -2, -1]
    result5 = solution.lengthOfLIS(nums5)
    assert result5 == 5, f"All negative failed: {result5}"
    print(f"All negative: ✅")

    # Edge Case 6: Mixed positive and negative
    nums6 = [-1, 0, 1, -2, 2]
    result6 = solution.lengthOfLIS(nums6)
    assert result6 == 4, f"Mixed values failed: {result6}"
    print(f"Mixed values: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Longest Increasing Subsequence:")

    # Large dataset
    nums = [i % 100 for i in range(1000)]

    start_time = time.time()
    result = solution.lengthOfLIS(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 elements):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Increasing Subsequence Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the lengthOfLIS method")
        print("- Aim for O(n * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n)")
        print("- Consider using binary search with patience sorting")

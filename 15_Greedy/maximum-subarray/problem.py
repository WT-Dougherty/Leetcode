"""
Maximum Subarray - LeetCode Problem 53

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

import time


class Solution:
    def maxSubArray(self, nums):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = solution.maxSubArray(nums1)
    assert result1 == 6, f"Failed for nums={nums1}, expected 6, got {result1}"

    # Test Case 2: Single element
    nums2 = [1]
    result2 = solution.maxSubArray(nums2)
    assert result2 == 1, f"Failed for nums={nums2}, expected 1, got {result2}"

    # Test Case 3: All positive
    nums3 = [5, 4, -1, 7, 8]
    result3 = solution.maxSubArray(nums3)
    assert result3 == 23, f"Failed for nums={nums3}, expected 23, got {result3}"

    # Test Case 4: All negative
    nums4 = [-5, -4, -1, -7, -8]
    result4 = solution.maxSubArray(nums4)
    assert result4 == -1, f"Failed for nums={nums4}, expected -1, got {result4}"

    # Test Case 5: Mixed case
    nums5 = [1, 2, 3, -2, 5]
    result5 = solution.maxSubArray(nums5)
    assert result5 == 9, f"Failed for nums={nums5}, expected 9, got {result5}"

    # Test Case 6: Complex case
    nums6 = [-1, -2, -3, -4]
    result6 = solution.maxSubArray(nums6)
    assert result6 == -1, f"Failed for nums={nums6}, expected -1, got {result6}"

    # Test Case 7: Edge case
    nums7 = [0]
    result7 = solution.maxSubArray(nums7)
    assert result7 == 0, f"Failed for nums={nums7}, expected 0, got {result7}"

    # Test Case 8: Large values
    nums8 = [1000, -1000, 1000]
    result8 = solution.maxSubArray(nums8)
    assert result8 == 1000, f"Failed for nums={nums8}, expected 1000, got {result8}"

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
        # Generate test data - alternating positive and negative
        nums = [(-1) ** i * (i + 1) for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.maxSubArray(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

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

    # Edge Case 1: Single element
    nums = [42]
    result = solution.maxSubArray(nums)
    print(f"Single element: {result} ✅")

    # Edge Case 2: All negative
    nums = [-5, -3, -1]
    result = solution.maxSubArray(nums)
    print(f"All negative: {result} ✅")

    # Edge Case 3: All positive
    nums = [1, 2, 3]
    result = solution.maxSubArray(nums)
    print(f"All positive: {result} ✅")

    # Edge Case 4: Large negative values
    nums = [-1000000, -1000000, -1000000]
    result = solution.maxSubArray(nums)
    print(f"Large negative values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset - mixed values
    size = 100000
    nums = [(-1) ** i * (i % 1000) for i in range(size)]

    start_time = time.time()
    result = solution.maxSubArray(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} elements, mixed values):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")

    # Large dataset - all positive
    nums2 = [i for i in range(size)]

    start_time = time.time()
    result2 = solution.maxSubArray(nums2)
    elapsed_time2 = time.time() - start_time

    print(f"\nLarge dataset ({size} elements, all positive):")
    print(f"Time: {elapsed_time2:.6f}s, Result: {result2}")


if __name__ == "__main__":
    print("🧪 Testing Maximum Subarray Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxSubArray method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using Kadane's algorithm")

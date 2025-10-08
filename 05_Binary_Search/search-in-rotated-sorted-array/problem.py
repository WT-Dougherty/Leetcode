"""
Search in Rotated Sorted Array - LeetCode Problem 33

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the
index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

import time
import random
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1, target1 = [4, 5, 6, 7, 0, 1, 2], 0
    result1 = solution.search(nums1, target1)
    assert (
        result1 == 4
    ), f"Failed for nums={nums1}, target={target1}, expected 4, got {result1}"

    # Test Case 2: Target not found
    nums2, target2 = [4, 5, 6, 7, 0, 1, 2], 3
    result2 = solution.search(nums2, target2)
    assert (
        result2 == -1
    ), f"Failed for nums={nums2}, target={target2}, expected -1, got {result2}"

    # Test Case 3: Single element found
    nums3, target3 = [1], 1
    result3 = solution.search(nums3, target3)
    assert (
        result3 == 0
    ), f"Failed for nums={nums3}, target={target3}, expected 0, got {result3}"

    # Test Case 4: Single element not found
    nums4, target4 = [1], 0
    result4 = solution.search(nums4, target4)
    assert (
        result4 == -1
    ), f"Failed for nums={nums4}, target={target4}, expected -1, got {result4}"

    # Test Case 5: No rotation
    nums5, target5 = [1, 2, 3, 4, 5], 3
    result5 = solution.search(nums5, target5)
    assert (
        result5 == 2
    ), f"Failed for nums={nums5}, target={target5}, expected 2, got {result5}"

    # Test Case 6: Target at beginning
    nums6, target6 = [4, 5, 6, 7, 0, 1, 2], 4
    result6 = solution.search(nums6, target6)
    assert (
        result6 == 0
    ), f"Failed for nums={nums6}, target={target6}, expected 0, got {result6}"

    # Test Case 7: Target at end
    nums7, target7 = [4, 5, 6, 7, 0, 1, 2], 2
    result7 = solution.search(nums7, target7)
    assert (
        result7 == 6
    ), f"Failed for nums={nums7}, target={target7}, expected 6, got {result7}"

    # Test Case 8: Negative numbers
    nums8, target8 = [-5, -3, -1, 0, 2, 4], -1
    result8 = solution.search(nums8, target8)
    assert (
        result8 == 2
    ), f"Failed for nums={nums8}, target={target8}, expected 2, got {result8}"

    # Test Case 9: Large rotation
    nums9, target9 = [5, 6, 7, 8, 9, 1, 2, 3, 4], 1
    result9 = solution.search(nums9, target9)
    assert (
        result9 == 5
    ), f"Failed for nums={nums9}, target={target9}, expected 5, got {result9}"

    # Test Case 10: Edge case with maximum constraint
    nums10, target10 = [5000, 1, 2, 3, 4], 5000
    result10 = solution.search(nums10, target10)
    assert (
        result10 == 0
    ), f"Failed for nums={nums10}, target={target10}, expected 0, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 5000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create rotated sorted array
        nums = list(range(size))
        rotation_point = random.randint(1, size - 1)
        nums = nums[rotation_point:] + nums[:rotation_point]
        target = random.choice(nums)  # Ensure target exists

        # Test approach
        start_time = time.time()
        result = solution.search(nums, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(log n) complexity by checking if time growth is logarithmic
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            n1, n2 = test_sizes[i - 1], test_sizes[i]
            expected_ratio = (n2.bit_length() - 1) / (n1.bit_length() - 1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance for logarithmic
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (min_expected <= actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    nums = list(range(5000))
    rotation_point = random.randint(1, 4999)
    nums = nums[rotation_point:] + nums[:rotation_point]
    target = random.choice(nums)
    result = solution.search(nums, target)
    assert result >= 0
    print(f"Maximum length (5k elements): {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [5000, 1, 2, 3, 4]
    target = 5000
    result = solution.search(nums, target)
    assert result == 0
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    nums = [-5000, -4999, -4998, -4997, -4996]
    target = -5000
    result = solution.search(nums, target)
    assert result == 0
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All same elements (edge case)
    nums = [5] * 1000
    target = 5
    result = solution.search(nums, target)
    assert result >= 0
    print(f"All same elements: {result} ✅")

    # Edge Case 5: Sequential numbers rotated
    nums = list(range(1, 1001))
    rotation_point = 500
    nums = nums[rotation_point:] + nums[:rotation_point]
    target = 1
    result = solution.search(nums, target)
    assert result == 500
    print(f"Sequential numbers rotated: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = list(range(5000))
    rotation_point = random.randint(1, 4999)
    nums = nums[rotation_point:] + nums[:rotation_point]
    target = random.choice(nums)

    start_time = time.time()
    result = solution.search(nums, target)
    time1 = time.time() - start_time

    print(f"Large dataset (5k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Search in Rotated Sorted Array Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the search method")
        print("- Aim for O(log n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use binary search algorithm")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using binary search algorithm")

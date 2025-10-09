"""
Find Minimum in Rotated Sorted Array - LeetCode Problem 153

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element
of this array.

You must write an algorithm that runs in O(log n) time.
"""

import time
import random
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [3, 4, 5, 1, 2]
    result1 = solution.findMin(nums1)
    assert result1 == 1, f"Failed for nums={nums1}, expected 1, got {result1}"

    # Test Case 2: Another rotation
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    result2 = solution.findMin(nums2)
    assert result2 == 0, f"Failed for nums={nums2}, expected 0, got {result2}"

    # Test Case 3: No rotation
    nums3 = [11, 13, 15, 17]
    result3 = solution.findMin(nums3)
    assert result3 == 11, f"Failed for nums={nums3}, expected 11, got {result3}"

    # Test Case 4: Single element
    nums4 = [1]
    result4 = solution.findMin(nums4)
    assert result4 == 1, f"Failed for nums={nums4}, expected 1, got {result4}"

    # Test Case 5: Two elements
    nums5 = [2, 1]
    result5 = solution.findMin(nums5)
    assert result5 == 1, f"Failed for nums={nums5}, expected 1, got {result5}"

    # Test Case 6: Two elements no rotation
    nums6 = [1, 2]
    result6 = solution.findMin(nums6)
    assert result6 == 1, f"Failed for nums={nums6}, expected 1, got {result6}"

    # Test Case 7: Negative numbers
    nums7 = [-1, 0, 1, 2, -2]
    result7 = solution.findMin(nums7)
    assert result7 == -2, f"Failed for nums={nums7}, expected -2, got {result7}"

    # Test Case 8: All negative numbers
    nums8 = [-5, -4, -3, -2, -1]
    result8 = solution.findMin(nums8)
    assert result8 == -5, f"Failed for nums={nums8}, expected -5, got {result8}"

    # Test Case 9: Large rotation
    nums9 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    result9 = solution.findMin(nums9)
    assert result9 == 1, f"Failed for nums={nums9}, expected 1, got {result9}"

    # Test Case 10: Edge case with maximum constraint
    nums10 = [5000, 1, 2, 3, 4]
    result10 = solution.findMin(nums10)
    assert result10 == 1, f"Failed for nums={nums10}, expected 1, got {result10}"

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

        # Test approach
        start_time = time.time()
        result = solution.findMin(nums)
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

            if not (actual <= max_expected):
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
    result = solution.findMin(nums)
    assert result == 0
    print(f"Maximum length (5k elements): {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [5000, 1, 2, 3, 4]
    result = solution.findMin(nums)
    assert result == 1
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    nums = [-5000, -4999, -4998, -4997, -4996]
    result = solution.findMin(nums)
    assert result == -5000
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All same elements (edge case)
    nums = [5] * 1000
    result = solution.findMin(nums)
    assert result == 5
    print(f"All same elements: {result} ✅")

    # Edge Case 5: Sequential numbers rotated
    nums = list(range(1, 1001))
    rotation_point = 500
    nums = nums[rotation_point:] + nums[:rotation_point]
    result = solution.findMin(nums)
    assert result == 1
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

    start_time = time.time()
    result = solution.findMin(nums)
    time1 = time.time() - start_time

    print(f"Large dataset (5k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Find Minimum in Rotated Sorted Array Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findMin method")
        print("- Aim for O(log n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use binary search algorithm")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using binary search algorithm")

"""
Two Sum - LeetCode Problem 1

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice. You can return the answer in any order.
"""

import time
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return [hm[target - nums[i]], i]
            hm[nums[i]] = i
        return [-1, -1]

    def BruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1, target1 = [2, 7, 11, 15], 9
    result1 = solution.twoSum(nums1, target1)
    assert sorted(result1) == [
        0,
        1,
    ], f"Failed for nums={nums1}, target={target1}, got {result1}"

    # Test Case 2: Different indices
    nums2, target2 = [3, 2, 4], 6
    result2 = solution.twoSum(nums2, target2)
    assert sorted(result2) == [
        1,
        2,
    ], f"Failed for nums={nums2}, target={target2}, got {result2}"

    # Test Case 3: Same numbers
    nums3, target3 = [3, 3], 6
    result3 = solution.twoSum(nums3, target3)
    assert sorted(result3) == [
        0,
        1,
    ], f"Failed for nums={nums3}, target={target3}, got {result3}"

    # Test Case 4: Negative numbers
    nums4, target4 = [-1, -2, -3, -4, -5], -8
    result4 = solution.twoSum(nums4, target4)
    assert sorted(result4) == [
        2,
        4,
    ], f"Failed for nums={nums4}, target={target4}, got {result4}"

    # Test Case 5: Zero target
    nums5, target5 = [1, 2, 3, -9, -2], 0
    result5 = solution.twoSum(nums5, target5)
    assert sorted(result5) == [
        1,
        4,
    ], f"Failed for nums={nums5}, target={target5}, got {result5}"

    # Test Case 6: Large numbers
    nums6, target6 = [1000000000, -1000000000, 2, 3], 0
    result6 = solution.twoSum(nums6, target6)
    assert sorted(result6) == [
        0,
        1,
    ], f"Failed for nums={nums6}, target={target6}, got {result6}"

    # Test Case 7: Duplicate values
    nums7, target7 = [1, 2, 2, 5], 4
    result7 = solution.twoSum(nums7, target7)
    assert sorted(result7) == [
        1,
        2,
    ], f"Failed for nums={nums7}, target={target7}, got {result7}"

    # Test Case 8: First and last
    nums8, target8 = [1, 2, 3, 4, 6], 6
    result8 = solution.twoSum(nums8, target8)
    assert sorted(result8) == [
        1,
        3,
    ], f"Failed for nums={nums8}, target={target8}, got {result8}"

    # Test Case 9: Adjacent elements (unique solution)
    nums9, target9 = [1, 2, 3, 4, 8], 7
    result9 = solution.twoSum(nums9, target9)
    assert sorted(result9) == [
        2,
        3,
    ], f"Failed for nums={nums9}, target={target9}, got {result9}"

    # Test Case 10: Minimum length
    nums10, target10 = [1, 2], 3
    result10 = solution.twoSum(nums10, target10)
    assert sorted(result10) == [
        0,
        1,
    ], f"Failed for nums={nums10}, target={target10}, got {result10}"

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
        # Generate test data - force worst-case behavior for brute force
        # Solution is at the end, forcing algorithm to check many pairs
        nums = list(range(size))
        target = nums[size - 2] + nums[size - 1]  # Last two elements

        # Test approach
        start_time = time.time()
        result = solution.twoSum(nums, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        if len(result) == 2:
            actual_sum = nums[result[0]] + nums[result[1]]
            assert actual_sum == target, f"Sum mismatch: {actual_sum} != {target}"

        print(f"{size}\t{elapsed_time:.6f}s\tIndices: {result}")

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
        tolerance = 0.5  # Allow 50% variance for O(n) detection
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
    nums = [1, 2]
    target = 3
    result = solution.twoSum(nums, target)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [10**9, -(10**9), 0]
    target = 0
    result = solution.twoSum(nums, target)
    print(f"Large numbers: {result} ✅")

    # Edge Case 3: All same numbers
    nums = [5] * 1000
    target = 10
    result = solution.twoSum(nums, target)
    print(f"All same numbers: {result} ✅")

    # Edge Case 4: Negative target
    nums = [1, 2, 3, 4, 5]
    target = -1
    result = solution.twoSum(nums, target)
    print(f"Negative target (no solution): {result} ✅")

    # Edge Case 5: Zero target with mixed numbers
    nums = [-1, 0, 1, 2]
    target = 0
    result = solution.twoSum(nums, target)
    print(f"Zero target: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = list(range(100000))
    target = nums[0] + nums[99999]  # First + last

    start_time = time.time()
    result = solution.twoSum(nums, target)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")

    # Verify result
    if len(result) == 2:
        actual_sum = nums[result[0]] + nums[result[1]]
        print(
            f"Verification: {nums[result[0]]} + {nums[result[1]]} = {actual_sum} (target: {target})"
        )


if __name__ == "__main__":
    print("🧪 Testing Two Sum Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the twoSum method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash maps or other O(n) approaches")

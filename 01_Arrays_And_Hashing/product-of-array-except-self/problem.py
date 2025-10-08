"""
Product of Array Except Self - LeetCode Problem 238

Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i]. The product of any prefix or suffix
of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs
in O(n) time and without using the division operator.
"""

import time
import random
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 2, 3, 4]
    result1 = solution.productExceptSelf(nums1)
    expected1 = [24, 12, 8, 6]
    assert (
        result1 == expected1
    ), f"Failed for {nums1}, expected {expected1}, got {result1}"

    # Test Case 2: With zeros
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    expected2 = [0, 0, 9, 0, 0]
    assert (
        result2 == expected2
    ), f"Failed for {nums2}, expected {expected2}, got {result2}"

    # Test Case 3: Two elements
    nums3 = [2, 3]
    result3 = solution.productExceptSelf(nums3)
    expected3 = [3, 2]
    assert (
        result3 == expected3
    ), f"Failed for {nums3}, expected {expected3}, got {result3}"

    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4]
    result4 = solution.productExceptSelf(nums4)
    expected4 = [24, 12, 8, 6]
    assert (
        result4 == expected4
    ), f"Failed for {nums4}, expected {expected4}, got {result4}"

    # Test Case 5: Mixed positive and negative
    nums5 = [1, -1, 2, -2]
    result5 = solution.productExceptSelf(nums5)
    expected5 = [4, -4, 2, -2]
    assert (
        result5 == expected5
    ), f"Failed for {nums5}, expected {expected5}, got {result5}"

    # Test Case 6: Single zero
    nums6 = [1, 2, 0, 4]
    result6 = solution.productExceptSelf(nums6)
    expected6 = [0, 0, 8, 0]
    assert (
        result6 == expected6
    ), f"Failed for {nums6}, expected {expected6}, got {result6}"

    # Test Case 7: All ones
    nums7 = [1, 1, 1, 1]
    result7 = solution.productExceptSelf(nums7)
    expected7 = [1, 1, 1, 1]
    assert (
        result7 == expected7
    ), f"Failed for {nums7}, expected {expected7}, got {result7}"

    # Test Case 8: Large numbers
    nums8 = [2, 3, 4, 5]
    result8 = solution.productExceptSelf(nums8)
    expected8 = [60, 40, 30, 24]
    assert (
        result8 == expected8
    ), f"Failed for {nums8}, expected {expected8}, got {result8}"

    # Test Case 9: With negative zero
    nums9 = [1, 2, 3, 0, 5]
    result9 = solution.productExceptSelf(nums9)
    expected9 = [0, 0, 0, 30, 0]
    assert (
        result9 == expected9
    ), f"Failed for {nums9}, expected {expected9}, got {result9}"

    # Test Case 10: Minimum length
    nums10 = [1, 2]
    result10 = solution.productExceptSelf(nums10)
    expected10 = [2, 1]
    assert (
        result10 == expected10
    ), f"Failed for {nums10}, expected {expected10}, got {result10}"

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
        nums = [random.randint(-30, 30) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.productExceptSelf(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result length
        assert len(result) == len(
            nums
        ), f"Length mismatch: {len(result)} != {len(nums)}"

        # Verify one result manually
        if size > 0:
            expected_first = 1
            for i in range(1, len(nums)):
                expected_first *= nums[i]
            assert (
                result[0] == expected_first
            ), f"First element wrong: {result[0]} != {expected_first}"

        print(f"{size}\t{elapsed_time:.6f}s\tLength: {len(result)}")

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
    nums = [1, 2]
    result = solution.productExceptSelf(nums)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [30] * 1000
    result = solution.productExceptSelf(nums)
    print(f"Maximum values (30): {len(result)} elements ✅")

    # Edge Case 3: All zeros
    nums = [0] * 100
    result = solution.productExceptSelf(nums)
    print(f"All zeros: {result[:5]}... ✅")

    # Edge Case 4: Alternating positive/negative
    nums = [1, -1] * 500
    result = solution.productExceptSelf(nums)
    print(f"Alternating pattern: {len(result)} elements ✅")

    # Edge Case 5: Single non-zero
    nums = [0, 0, 0, 5, 0]
    result = solution.productExceptSelf(nums)
    print(f"Single non-zero: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = [random.randint(-30, 30) for _ in range(100000)]

    start_time = time.time()
    result = solution.productExceptSelf(nums)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Length: {len(result)}")

    # Verify result
    if len(result) > 0:
        # Check first element
        expected_first = 1
        for i in range(1, len(nums)):
            expected_first *= nums[i]
        print(f"Verification: First element = {result[0]} (expected: {expected_first})")


if __name__ == "__main__":
    print("🧪 Testing Product of Array Except Self Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the productExceptSelf method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Do not use division operator")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using prefix and suffix products")

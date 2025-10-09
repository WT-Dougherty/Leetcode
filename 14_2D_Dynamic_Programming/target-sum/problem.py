"""
Target Sum - LeetCode Problem 494

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the two symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.
"""

import time
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    result1 = solution.findTargetSumWays(nums1, target1)
    assert (
        result1 == 5
    ), f"Failed for nums={nums1}, target={target1}, expected 5, got {result1}"

    # Test Case 2: Single element
    nums2 = [1]
    target2 = 1
    result2 = solution.findTargetSumWays(nums2, target2)
    assert (
        result2 == 1
    ), f"Failed for nums={nums2}, target={target2}, expected 1, got {result2}"

    # Test Case 3: Two elements
    nums3 = [1, 1]
    target3 = 0
    result3 = solution.findTargetSumWays(nums3, target3)
    assert (
        result3 == 2
    ), f"Failed for nums={nums3}, target={target3}, expected 2, got {result3}"

    # Test Case 4: Complex case
    nums4 = [1, 2, 3, 4, 5]
    target4 = 3
    result4 = solution.findTargetSumWays(nums4, target4)
    assert (
        result4 == 3
    ), f"Failed for nums={nums4}, target={target4}, expected 3, got {result4}"

    # Test Case 5: All same values
    nums5 = [1, 1, 1]
    target5 = 1
    result5 = solution.findTargetSumWays(nums5, target5)
    assert (
        result5 == 3
    ), f"Failed for nums={nums5}, target={target5}, expected 3, got {result5}"

    # Test Case 6: Edge case
    nums6 = [1]
    target6 = -1
    result6 = solution.findTargetSumWays(nums6, target6)
    assert (
        result6 == 1
    ), f"Failed for nums={nums6}, target={target6}, expected 1, got {result6}"

    # Test Case 7: Large target
    nums7 = [1, 2, 3]
    target7 = 6
    result7 = solution.findTargetSumWays(nums7, target7)
    assert (
        result7 == 1
    ), f"Failed for nums={nums7}, target={target7}, expected 1, got {result7}"

    # Test Case 8: Zero target
    nums8 = [1, 2, 3]
    target8 = 0
    result8 = solution.findTargetSumWays(nums8, target8)
    assert (
        result8 == 2
    ), f"Failed for nums={nums8}, target={target8}, expected 2, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 15, 20]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tSum\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create array with values that sum to even number
        nums = [i % 10 + 1 for i in range(size)]
        target = sum(nums) // 2

        # Test approach
        start_time = time.time()
        result = solution.findTargetSumWays(nums, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{target}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * sum) complexity where n is length of nums and sum is the total sum
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n * sum) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_sum = sum([j % 10 + 1 for j in range(test_sizes[i - 1])])
            curr_sum = sum([j % 10 + 1 for j in range(test_sizes[i])])
            prev_complexity = test_sizes[i - 1] * prev_sum
            curr_complexity = test_sizes[i] * curr_sum
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n*sum): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 3.0  # Allow 300% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n * sum)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n * sum) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n * sum), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * sum)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 element)
    nums1 = [1]
    target1 = 1
    result1 = solution.findTargetSumWays(nums1, target1)
    assert result1 == 1, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (20 elements)
    nums2 = [i % 1000 + 1 for i in range(20)]
    target2 = 0
    result2 = solution.findTargetSumWays(nums2, target2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (1000)
    nums3 = [1000]
    target3 = 1000
    result3 = solution.findTargetSumWays(nums3, target3)
    assert result3 == 1, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (0)
    nums4 = [0]
    target4 = 0
    result4 = solution.findTargetSumWays(nums4, target4)
    assert result4 == 1, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All zeros
    nums5 = [0, 0, 0]
    target5 = 0
    result5 = solution.findTargetSumWays(nums5, target5)
    assert result5 == 8, f"All zeros failed: {result5}"
    print(f"All zeros: ✅")

    # Edge Case 6: Maximum target (1000)
    nums6 = [1, 2, 3]
    target6 = 1000
    result6 = solution.findTargetSumWays(nums6, target6)
    assert result6 == 0, f"Max target failed: {result6}"
    print(f"Maximum target: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Target Sum:")

    # Large dataset
    nums = [i % 10 + 1 for i in range(20)]
    target = sum(nums) // 2

    start_time = time.time()
    result = solution.findTargetSumWays(nums, target)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (nums={len(nums)}, target={target}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Target Sum Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findTargetSumWays method")
        print("- Aim for O(n * sum) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * sum)")
        print("- Consider using dynamic programming")

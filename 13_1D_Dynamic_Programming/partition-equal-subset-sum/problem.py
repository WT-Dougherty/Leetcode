"""
Partition Equal Subset Sum - LeetCode Problem 416

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets with equal sum.
"""

import time
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 5, 11, 5]
    result1 = solution.canPartition(nums1)
    assert result1 == True, f"Failed for {nums1}, expected True, got {result1}"

    # Test Case 2: Impossible case
    nums2 = [1, 2, 3, 5]
    result2 = solution.canPartition(nums2)
    assert result2 == False, f"Failed for {nums2}, expected False, got {result2}"

    # Test Case 3: Single element
    nums3 = [1]
    result3 = solution.canPartition(nums3)
    assert result3 == False, f"Failed for {nums3}, expected False, got {result3}"

    # Test Case 4: Two elements
    nums4 = [1, 1]
    result4 = solution.canPartition(nums4)
    assert result4 == True, f"Failed for {nums4}, expected True, got {result4}"

    # Test Case 5: Three elements
    nums5 = [1, 2, 3]
    result5 = solution.canPartition(nums5)
    assert result5 == True, f"Failed for {nums5}, expected True, got {result5}"

    # Test Case 6: All same values
    nums6 = [1, 1, 1, 1]
    result6 = solution.canPartition(nums6)
    assert result6 == True, f"Failed for {nums6}, expected True, got {result6}"

    # Test Case 7: Complex case
    nums7 = [1, 2, 3, 4, 5, 6, 7]
    result7 = solution.canPartition(nums7)
    assert result7 == True, f"Failed for {nums7}, expected True, got {result7}"

    # Test Case 8: Edge case
    nums8 = [1, 2, 5]
    result8 = solution.canPartition(nums8)
    assert result8 == False, f"Failed for {nums8}, expected False, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with values that sum to even number
        nums = [i % 10 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.canPartition(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * sum) complexity
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
    result1 = solution.canPartition(nums1)
    assert result1 == False, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (200 elements)
    nums2 = [i % 100 + 1 for i in range(200)]
    result2 = solution.canPartition(nums2)
    assert isinstance(result2, bool), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (100)
    nums3 = [100, 100]
    result3 = solution.canPartition(nums3)
    assert result3 == True, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (1)
    nums4 = [1, 1]
    result4 = solution.canPartition(nums4)
    assert result4 == True, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All same values
    nums5 = [5] * 20
    result5 = solution.canPartition(nums5)
    assert result5 == True, f"All same values failed: {result5}"
    print(f"All same values: ✅")

    # Edge Case 6: Odd sum
    nums6 = [1, 2, 3, 4, 5]
    result6 = solution.canPartition(nums6)
    assert result6 == True, f"Odd sum failed: {result6}"
    print(f"Odd sum: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Partition Equal Subset Sum:")

    # Large dataset
    nums = [i % 10 + 1 for i in range(100)]

    start_time = time.time()
    result = solution.canPartition(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100 elements):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Partition Equal Subset Sum Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the canPartition method")
        print("- Aim for O(n * sum) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * sum)")
        print("- Consider using dynamic programming with subset sum")

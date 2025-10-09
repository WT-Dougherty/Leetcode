"""
3Sum - LeetCode Problem 15

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

import time
import random
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert len(result1) == len(
        expected1
    ), f"Failed for {nums1}, expected {len(expected1)} triplets, got {len(result1)}"

    # Test Case 2: No solution
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    assert result2 == [], f"Failed for {nums2}, expected empty list"

    # Test Case 3: All zeros
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    assert [0, 0, 0] in result3, f"Failed for {nums3}"

    # Test Case 4: Minimum length
    nums4 = [0, 0, 0]
    result4 = solution.threeSum(nums4)
    assert len(result4) == 1, f"Failed for {nums4}"

    # Test Case 5: Large numbers
    nums5 = [-100000, 50000, 50000]
    result5 = solution.threeSum(nums5)
    assert len(result5) == 1, f"Failed for {nums5}"

    # Test Case 6: Mixed positive and negative
    nums6 = [-2, 0, 1, 1, 2]
    result6 = solution.threeSum(nums6)
    assert len(result6) == 2, f"Failed for {nums6}"

    # Test Case 7: All negative
    nums7 = [-1, -1, -1, -1]
    result7 = solution.threeSum(nums7)
    assert result7 == [], f"Failed for {nums7}"

    # Test Case 8: All positive
    nums8 = [1, 1, 1, 1]
    result8 = solution.threeSum(nums8)
    assert result8 == [], f"Failed for {nums8}"

    # Test Case 9: Duplicate handling
    nums9 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    result9 = solution.threeSum(nums9)
    assert len(result9) >= 4, f"Failed for {nums9}"

    # Test Case 10: Edge case with zeros
    nums10 = [0, 0, 0, 0]
    result10 = solution.threeSum(nums10)
    assert [0, 0, 0] in result10, f"Failed for {nums10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n^2)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tTriplets")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        nums = [random.randint(-1000, 1000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.threeSum(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tFound: {len(result)}")

    # Verify O(n^2) complexity by checking if time growth is approximately quadratic
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n^2) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] / test_sizes[i - 1]) ** 2
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n^2): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^2)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n^3) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n^2), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^2)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum length
    nums = [0, 0, 0]
    result = solution.threeSum(nums)
    print(f"Minimum length: {len(result)} triplets ✅")

    # Edge Case 2: Maximum constraint values
    nums = [-100000] * 1000 + [100000] * 1000 + [0] * 1000
    result = solution.threeSum(nums)
    print(f"Maximum constraint values: {len(result)} triplets ✅")

    # Edge Case 3: All same numbers
    nums = [5] * 1000
    result = solution.threeSum(nums)
    print(f"All same numbers: {len(result)} triplets ✅")

    # Edge Case 4: Sequential numbers
    nums = list(range(-500, 501))
    result = solution.threeSum(nums)
    print(f"Sequential numbers: {len(result)} triplets ✅")

    # Edge Case 5: Alternating pattern
    nums = [1, -1] * 500
    result = solution.threeSum(nums)
    print(f"Alternating pattern: {len(result)} triplets ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = [random.randint(-1000, 1000) for _ in range(3000)]

    start_time = time.time()
    result = solution.threeSum(nums)
    time1 = time.time() - start_time

    print(f"Large dataset (3,000 elements):")
    print(f"Time: {time1:.6f}s, Triplets found: {len(result)}")


if __name__ == "__main__":
    print("🧪 Testing 3Sum Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the threeSum method")
        print("- Aim for O(n^2) time complexity")
        print("- Handle all edge cases correctly")
        print("- Avoid duplicate triplets")
        print("- Use sorting and two pointers")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^2)")
        print("- Consider using sorting and two pointers approach")

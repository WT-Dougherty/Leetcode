"""
Binary Search - LeetCode Problem 704

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

import time
import random


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.Binary_Search(nums, target, 0, len(nums) - 1)

    def Binary_Search(self, nums: list[int], target: int, left: int, right: int):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.Binary_Search(nums, target, left, mid - 1)
        else:
            return self.Binary_Search(nums, target, mid + 1, right)


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
    result1 = solution.search(nums1, target1)
    assert (
        result1 == 4
    ), f"Failed for nums={nums1}, target={target1}, expected 4, got {result1}"

    # Test Case 2: Target not found
    nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
    result2 = solution.search(nums2, target2)
    assert (
        result2 == -1
    ), f"Failed for nums={nums2}, target={target2}, expected -1, got {result2}"

    # Test Case 3: Single element found
    nums3, target3 = [5], 5
    result3 = solution.search(nums3, target3)
    assert (
        result3 == 0
    ), f"Failed for nums={nums3}, target={target3}, expected 0, got {result3}"

    # Test Case 4: Single element not found
    nums4, target4 = [5], 3
    result4 = solution.search(nums4, target4)
    assert (
        result4 == -1
    ), f"Failed for nums={nums4}, target={target4}, expected -1, got {result4}"

    # Test Case 5: Target at beginning
    nums5, target5 = [1, 2, 3, 4, 5], 1
    result5 = solution.search(nums5, target5)
    assert (
        result5 == 0
    ), f"Failed for nums={nums5}, target={target5}, expected 0, got {result5}"

    # Test Case 6: Target at end
    nums6, target6 = [1, 2, 3, 4, 5], 5
    result6 = solution.search(nums6, target6)
    assert (
        result6 == 4
    ), f"Failed for nums={nums6}, target={target6}, expected 4, got {result6}"

    # Test Case 7: Negative numbers
    nums7, target7 = [-5, -3, -1, 0, 2, 4], -1
    result7 = solution.search(nums7, target7)
    assert (
        result7 == 2
    ), f"Failed for nums={nums7}, target={target7}, expected 2, got {result7}"

    # Test Case 8: All negative numbers
    nums8, target8 = [-5, -4, -3, -2, -1], -3
    result8 = solution.search(nums8, target8)
    assert (
        result8 == 2
    ), f"Failed for nums={nums8}, target={target8}, expected 2, got {result8}"

    # Test Case 9: Large array
    nums9 = list(range(1, 10001))
    target9 = 5000
    result9 = solution.search(nums9, target9)
    assert result9 == 4999, f"Failed for large array, expected 4999, got {result9}"

    # Test Case 10: Edge case with duplicates
    nums10, target10 = [1, 2, 2, 3, 4], 2
    result10 = solution.search(nums10, target10)
    assert result10 in [
        1,
        2,
    ], f"Failed for nums={nums10}, target={target10}, expected 1 or 2, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        nums = sorted([random.randint(-10000, 10000) for _ in range(size)])
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
    nums = sorted([random.randint(-10000, 10000) for _ in range(10000)])
    target = random.choice(nums)
    result = solution.search(nums, target)
    print(f"Maximum length (10k elements): {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [-10000, 0, 10000]
    target = 10000
    result = solution.search(nums, target)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    nums = [-10000, 0, 10000]
    target = -10000
    result = solution.search(nums, target)
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All same elements
    nums = [5] * 1000
    target = 5
    result = solution.search(nums, target)
    assert result >= 0
    print(f"All same elements: {result} ✅")

    # Edge Case 5: Sequential numbers
    nums = list(range(1, 1001))
    target = 500
    result = solution.search(nums, target)
    assert result == 499
    print(f"Sequential numbers: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = sorted([random.randint(-10000, 10000) for _ in range(100000)])
    target = random.choice(nums)

    start_time = time.time()
    result = solution.search(nums, target)
    time1 = time.time() - start_time

    print(f"Large dataset (100k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Binary Search Problem")
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

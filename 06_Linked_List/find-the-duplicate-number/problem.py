"""
Find The Duplicate Number - LeetCode Problem 287

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

import time
import random
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 3, 4, 2, 2]
    result1 = solution.findDuplicate(nums1)
    assert result1 == 2, f"Failed for {nums1}, expected 2, got {result1}"

    # Test Case 2: Another case
    nums2 = [3, 1, 3, 4, 2]
    result2 = solution.findDuplicate(nums2)
    assert result2 == 3, f"Failed for {nums2}, expected 3, got {result2}"

    # Test Case 3: Duplicate at beginning
    nums3 = [1, 1, 2, 3, 4]
    result3 = solution.findDuplicate(nums3)
    assert result3 == 1, f"Failed for {nums3}, expected 1, got {result3}"

    # Test Case 4: Duplicate at end
    nums4 = [1, 2, 3, 4, 4]
    result4 = solution.findDuplicate(nums4)
    assert result4 == 4, f"Failed for {nums4}, expected 4, got {result4}"

    # Test Case 5: Two elements
    nums5 = [1, 1]
    result5 = solution.findDuplicate(nums5)
    assert result5 == 1, f"Failed for {nums5}, expected 1, got {result5}"

    # Test Case 6: Three elements
    nums6 = [1, 2, 2]
    result6 = solution.findDuplicate(nums6)
    assert result6 == 2, f"Failed for {nums6}, expected 2, got {result6}"

    # Test Case 7: Large range
    nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 5]
    result7 = solution.findDuplicate(nums7)
    assert result7 == 5, f"Failed for large range, expected 5, got {result7}"

    # Test Case 8: All same
    nums8 = [1, 1, 1, 1]
    result8 = solution.findDuplicate(nums8)
    assert result8 == 1, f"Failed for all same, expected 1, got {result8}"

    # Test Case 9: Maximum constraint
    nums9 = list(range(1, 100001)) + [50000]
    result9 = solution.findDuplicate(nums9)
    assert result9 == 50000, f"Failed for max constraint"

    # Test Case 10: Minimum constraint
    nums10 = [1, 1]
    result10 = solution.findDuplicate(nums10)
    assert result10 == 1, f"Failed for min constraint, expected 1, got {result10}"

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
        nums = list(range(1, size + 1))
        duplicate_val = random.randint(1, size)
        nums.append(duplicate_val)
        random.shuffle(nums)

        # Test approach
        start_time = time.time()
        result = solution.findDuplicate(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result == duplicate_val, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

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

    # Edge Case 1: Maximum constraint length
    nums = list(range(1, 100001))
    nums.append(50000)
    random.shuffle(nums)
    result = solution.findDuplicate(nums)
    assert result == 50000
    print(f"Maximum length (100k elements): ✅")

    # Edge Case 2: Maximum constraint values
    nums = [100000] * 100000 + [100000]
    result = solution.findDuplicate(nums)
    assert result == 100000
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    nums = [1] * 100000 + [1]
    result = solution.findDuplicate(nums)
    assert result == 1
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Duplicate at different positions
    for pos in [0, 1000, 5000, 9999]:
        nums = list(range(1, 10001))
        nums[pos] = 5000  # Create duplicate
        result = solution.findDuplicate(nums)
        assert result == 5000
    print(f"Duplicate at different positions: ✅")

    # Edge Case 5: Sequential duplicates
    nums = list(range(1, 1001)) + [500, 501, 502]
    result = solution.findDuplicate(nums)
    assert result in [500, 501, 502]
    print(f"Sequential duplicates: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = list(range(1, 100001))
    duplicate_val = 50000
    nums.append(duplicate_val)
    random.shuffle(nums)

    start_time = time.time()
    result = solution.findDuplicate(nums)
    time1 = time.time() - start_time

    assert result == duplicate_val

    print(f"Large dataset (100k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Find The Duplicate Number Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findDuplicate method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use Floyd's cycle detection algorithm")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using Floyd's cycle detection algorithm")

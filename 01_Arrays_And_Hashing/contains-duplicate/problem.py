"""
Contains Duplicate - LeetCode Problem 217

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

import time
import random
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for num in nums:
            if num in dupes:
                return True
            dupes.add(num)
        return False


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case with duplicates
    nums1 = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums1) == True, f"Failed for {nums1}"

    # Test Case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums2) == False, f"Failed for {nums2}"

    # Test Case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums3) == True, f"Failed for {nums3}"

    # Test Case 4: Single element
    nums4 = [1]
    assert solution.containsDuplicate(nums4) == False, f"Failed for {nums4}"

    # Test Case 5: Two identical elements
    nums5 = [1, 1]
    assert solution.containsDuplicate(nums5) == True, f"Failed for {nums5}"

    # Test Case 6: Large numbers
    nums6 = [1000000000, -1000000000, 1000000000]
    assert solution.containsDuplicate(nums6) == True, f"Failed for {nums6}"

    # Test Case 7: All zeros
    nums7 = [0, 0, 0]
    assert solution.containsDuplicate(nums7) == True, f"Failed for {nums7}"

    # Test Case 8: Empty array (edge case)
    nums8 = []
    assert solution.containsDuplicate(nums8) == False, f"Failed for {nums8}"

    # Test Case 9: Duplicate at the end
    nums9 = [1, 2, 3, 4, 5, 1]
    assert solution.containsDuplicate(nums9) == True, f"Failed for {nums9}"

    # Test Case 10: Duplicate at the beginning
    nums10 = [1, 1, 2, 3, 4, 5]
    assert solution.containsDuplicate(nums10) == True, f"Failed for {nums10}"

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
        # Generate test data - no duplicates (worst case)
        nums = list(range(size))
        random.shuffle(nums)

        # Test approach
        start_time = time.time()
        result = solution.containsDuplicate(nums)
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

    # Edge Case 1: Minimum constraint (1 element)
    nums = [42]
    result = solution.containsDuplicate(nums)
    print(f"Single element [42]: {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [10**9, -(10**9), 10**9]
    result = solution.containsDuplicate(nums)
    print(f"Large numbers with duplicate: {result} ✅")

    # Edge Case 3: All same elements
    nums = [5] * 1000
    result = solution.containsDuplicate(nums)
    print(f"All same elements (1000x): {result} ✅")

    # Edge Case 4: Alternating pattern
    nums = [1, 2] * 500
    result = solution.containsDuplicate(nums)
    print(f"Alternating pattern (no duplicates): {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset with no duplicates
    large_nums = list(range(100000))
    random.shuffle(large_nums)

    start_time = time.time()
    result1 = solution.containsDuplicate(large_nums)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements, no duplicates):")
    print(f"Time: {time1:.6f}s, Result: {result1}")

    # Large dataset with duplicates
    large_nums_dup = list(range(100000)) + [99999]
    random.shuffle(large_nums_dup)

    start_time = time.time()
    result2 = solution.containsDuplicate(large_nums_dup)
    time2 = time.time() - start_time

    print(f"\nLarge dataset (100,000 elements, with duplicates):")
    print(f"Time: {time2:.6f}s, Result: {result2}")


if __name__ == "__main__":
    print("🧪 Testing Contains Duplicate Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the containsDuplicate method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash sets or other O(n) approaches")

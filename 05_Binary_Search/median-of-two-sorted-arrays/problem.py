"""
Median of Two Sorted Arrays - LeetCode Problem 4

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median
of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

import time
import random
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1_1, nums2_1 = [1, 3], [2]
    result1 = solution.findMedianSortedArrays(nums1_1, nums2_1)
    assert (
        abs(result1 - 2.0) < 1e-6
    ), f"Failed for nums1={nums1_1}, nums2={nums2_1}, expected 2.0, got {result1}"

    # Test Case 2: Even total length
    nums1_2, nums2_2 = [1, 2], [3, 4]
    result2 = solution.findMedianSortedArrays(nums1_2, nums2_2)
    assert (
        abs(result2 - 2.5) < 1e-6
    ), f"Failed for nums1={nums1_2}, nums2={nums2_2}, expected 2.5, got {result2}"

    # Test Case 3: One empty array
    nums1_3, nums2_3 = [], [1]
    result3 = solution.findMedianSortedArrays(nums1_3, nums2_3)
    assert (
        abs(result3 - 1.0) < 1e-6
    ), f"Failed for nums1={nums1_3}, nums2={nums2_3}, expected 1.0, got {result3}"

    # Test Case 4: Other empty array
    nums1_4, nums2_4 = [2], []
    result4 = solution.findMedianSortedArrays(nums1_4, nums2_4)
    assert (
        abs(result4 - 2.0) < 1e-6
    ), f"Failed for nums1={nums1_4}, nums2={nums2_4}, expected 2.0, got {result4}"

    # Test Case 5: Both arrays same length
    nums1_5, nums2_5 = [1, 2], [3, 4]
    result5 = solution.findMedianSortedArrays(nums1_5, nums2_5)
    assert (
        abs(result5 - 2.5) < 1e-6
    ), f"Failed for nums1={nums1_5}, nums2={nums2_5}, expected 2.5, got {result5}"

    # Test Case 6: Negative numbers
    nums1_6, nums2_6 = [-1, 0], [1, 2]
    result6 = solution.findMedianSortedArrays(nums1_6, nums2_6)
    assert (
        abs(result6 - 0.5) < 1e-6
    ), f"Failed for nums1={nums1_6}, nums2={nums2_6}, expected 0.5, got {result6}"

    # Test Case 7: All negative numbers
    nums1_7, nums2_7 = [-3, -2], [-1, 0]
    result7 = solution.findMedianSortedArrays(nums1_7, nums2_7)
    assert (
        abs(result7 - (-1.5)) < 1e-6
    ), f"Failed for nums1={nums1_7}, nums2={nums2_7}, expected -1.5, got {result7}"

    # Test Case 8: Single elements
    nums1_8, nums2_8 = [1], [2]
    result8 = solution.findMedianSortedArrays(nums1_8, nums2_8)
    assert (
        abs(result8 - 1.5) < 1e-6
    ), f"Failed for nums1={nums1_8}, nums2={nums2_8}, expected 1.5, got {result8}"

    # Test Case 9: Large numbers
    nums1_9, nums2_9 = [1000000], [2000000]
    result9 = solution.findMedianSortedArrays(nums1_9, nums2_9)
    assert (
        abs(result9 - 1500000.0) < 1e-6
    ), f"Failed for nums1={nums1_9}, nums2={nums2_9}, expected 1500000.0, got {result9}"

    # Test Case 10: Complex case
    nums1_10, nums2_10 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
    result10 = solution.findMedianSortedArrays(nums1_10, nums2_10)
    assert (
        abs(result10 - 5.5) < 1e-6
    ), f"Failed for nums1={nums1_10}, nums2={nums2_10}, expected 5.5, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log(m+n))"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(100, 100), (500, 500), (1000, 1000)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for m, n in test_sizes:
        # Generate test data
        nums1 = sorted([random.randint(-1000, 1000) for _ in range(m)])
        nums2 = sorted([random.randint(-1000, 1000) for _ in range(n)])

        # Test approach
        start_time = time.time()
        result = solution.findMedianSortedArrays(nums1, nums2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{m}+{n}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(log(m+n)) complexity by checking if time growth is logarithmic
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log(m+n)) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            size1, size2 = m1 + n1, m2 + n2
            expected_ratio = (size2.bit_length() - 1) / (size1.bit_length() - 1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(log(m+n)): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance for logarithmic
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log(m+n))")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m+n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(log(m+n)), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log(m+n))")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    nums1 = sorted([random.randint(-1000, 1000) for _ in range(1000)])
    nums2 = sorted([random.randint(-1000, 1000) for _ in range(1000)])
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Maximum length (1k+1k elements): {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums1 = [10**6]
    nums2 = [10**6]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert abs(result - 10**6) < 1e-6
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    nums1 = [-(10**6)]
    nums2 = [-(10**6)]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert abs(result - (-(10**6))) < 1e-6
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: One array much larger
    nums1 = sorted([random.randint(-1000, 1000) for _ in range(100)])
    nums2 = sorted([random.randint(-1000, 1000) for _ in range(900)])
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"One array much larger: {result} ✅")

    # Edge Case 5: All same elements
    nums1 = [5] * 500
    nums2 = [5] * 500
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert abs(result - 5.0) < 1e-6
    print(f"All same elements: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums1 = sorted([random.randint(-1000, 1000) for _ in range(1000)])
    nums2 = sorted([random.randint(-1000, 1000) for _ in range(1000)])

    start_time = time.time()
    result = solution.findMedianSortedArrays(nums1, nums2)
    time1 = time.time() - start_time

    print(f"Large dataset (1k+1k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Median of Two Sorted Arrays Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findMedianSortedArrays method")
        print("- Aim for O(log(m+n)) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use binary search algorithm")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log(m+n))")
        print("- Consider using binary search algorithm")

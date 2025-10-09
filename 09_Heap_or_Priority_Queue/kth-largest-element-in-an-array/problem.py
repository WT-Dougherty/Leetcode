"""
Kth Largest Element in an Array - LeetCode Problem 215

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in sorted order, not the kth distinct element.
"""

import time
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = solution.findKthLargest(nums1, k1)
    assert result1 == 5, f"Failed for [3,2,1,5,6,4], k=2, expected 5, got {result1}"

    # Test Case 2: Duplicate elements
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    assert (
        result2 == 4
    ), f"Failed for [3,2,3,1,2,4,5,5,6], k=4, expected 4, got {result2}"

    # Test Case 3: Single element
    nums3 = [1]
    k3 = 1
    result3 = solution.findKthLargest(nums3, k3)
    assert result3 == 1, f"Failed for [1], k=1, expected 1, got {result3}"

    # Test Case 4: Two elements
    nums4 = [2, 1]
    k4 = 1
    result4 = solution.findKthLargest(nums4, k4)
    assert result4 == 2, f"Failed for [2,1], k=1, expected 2, got {result4}"

    # Test Case 5: All same elements
    nums5 = [5, 5, 5, 5]
    k5 = 2
    result5 = solution.findKthLargest(nums5, k5)
    assert result5 == 5, f"Failed for [5,5,5,5], k=2, expected 5, got {result5}"

    # Test Case 6: Negative numbers
    nums6 = [-1, 2, 0]
    k6 = 2
    result6 = solution.findKthLargest(nums6, k6)
    assert result6 == 0, f"Failed for [-1,2,0], k=2, expected 0, got {result6}"

    # Test Case 7: Large numbers
    nums7 = [100000, -100000, 0]
    k7 = 1
    result7 = solution.findKthLargest(nums7, k7)
    assert (
        result7 == 100000
    ), f"Failed for [100000,-100000,0], k=1, expected 100000, got {result7}"

    # Test Case 8: k equals array length
    nums8 = [1, 2, 3, 4, 5]
    k8 = 5
    result8 = solution.findKthLargest(nums8, k8)
    assert result8 == 1, f"Failed for [1,2,3,4,5], k=5, expected 1, got {result8}"

    # Test Case 9: Reverse sorted
    nums9 = [5, 4, 3, 2, 1]
    k9 = 3
    result9 = solution.findKthLargest(nums9, k9)
    assert result9 == 3, f"Failed for [5,4,3,2,1], k=3, expected 3, got {result9}"

    # Test Case 10: Already sorted
    nums10 = [1, 2, 3, 4, 5]
    k10 = 2
    result10 = solution.findKthLargest(nums10, k10)
    assert result10 == 4, f"Failed for [1,2,3,4,5], k=2, expected 4, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tK\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data
        nums = list(range(size))
        k = size // 2  # Middle element

        # Test approach
        start_time = time.time()
        result = solution.findKthLargest(nums, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{k}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) average case complexity (QuickSelect) or O(n log k) for heap
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

        # Check if ratios are within acceptable range
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n) complexity")
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

    # Edge Case 1: Minimum constraint (1 element, k=1)
    nums1 = [42]
    result1 = solution.findKthLargest(nums1, 1)
    assert result1 == 42, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint values
    nums2 = [10**4, -(10**4), 0]
    result2 = solution.findKthLargest(nums2, 1)
    assert result2 == 10**4, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All same elements
    nums3 = [5] * 1000
    result3 = solution.findKthLargest(nums3, 500)
    assert result3 == 5, f"All same elements failed: {result3}"
    print(f"All same elements: ✅")

    # Edge Case 4: k equals array length
    nums4 = list(range(100))
    result4 = solution.findKthLargest(nums4, 100)
    assert result4 == 0, f"k equals array length failed: {result4}"
    print(f"k equals array length: ✅")

    # Edge Case 5: Large k
    nums5 = list(range(1000))
    result5 = solution.findKthLargest(nums5, 999)
    assert result5 == 1, f"Large k failed: {result5}"
    print(f"Large k: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Kth Largest Element:")

    # Large dataset
    nums = list(range(100000))
    k = 50000

    start_time = time.time()
    result = solution.findKthLargest(nums, k)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100,000 elements, k=50,000):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Kth Largest Element in an Array Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findKthLargest method")
        print("- Aim for O(n) average case or O(n log k) for heap approach")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using QuickSelect or heap-based approaches")

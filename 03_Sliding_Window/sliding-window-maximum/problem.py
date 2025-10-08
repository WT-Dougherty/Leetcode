"""
Sliding Window Maximum - LeetCode Problem 239

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.
"""

import time
import random
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1, k1 = [1, 3, -1, -3, 5, 3, 6, 7], 3
    result1 = solution.maxSlidingWindow(nums1, k1)
    expected1 = [3, 3, 5, 5, 6, 7]
    assert (
        result1 == expected1
    ), f"Failed for nums={nums1}, k={k1}, expected {expected1}, got {result1}"

    # Test Case 2: Single element
    nums2, k2 = [1], 1
    result2 = solution.maxSlidingWindow(nums2, k2)
    expected2 = [1]
    assert (
        result2 == expected2
    ), f"Failed for nums={nums2}, k={k2}, expected {expected2}, got {result2}"

    # Test Case 3: k equals length
    nums3, k3 = [1, 2, 3, 4, 5], 5
    result3 = solution.maxSlidingWindow(nums3, k3)
    expected3 = [5]
    assert (
        result3 == expected3
    ), f"Failed for nums={nums3}, k={k3}, expected {expected3}, got {result3}"

    # Test Case 4: Decreasing array
    nums4, k4 = [5, 4, 3, 2, 1], 3
    result4 = solution.maxSlidingWindow(nums4, k4)
    expected4 = [5, 4, 3]
    assert (
        result4 == expected4
    ), f"Failed for nums={nums4}, k={k4}, expected {expected4}, got {result4}"

    # Test Case 5: Increasing array
    nums5, k5 = [1, 2, 3, 4, 5], 3
    result5 = solution.maxSlidingWindow(nums5, k5)
    expected5 = [3, 4, 5]
    assert (
        result5 == expected5
    ), f"Failed for nums={nums5}, k={k5}, expected {expected5}, got {result5}"

    # Test Case 6: All same elements
    nums6, k6 = [2, 2, 2, 2], 2
    result6 = solution.maxSlidingWindow(nums6, k6)
    expected6 = [2, 2, 2]
    assert (
        result6 == expected6
    ), f"Failed for nums={nums6}, k={k6}, expected {expected6}, got {result6}"

    # Test Case 7: Negative numbers
    nums7, k7 = [-1, -2, -3, -4, -5], 3
    result7 = solution.maxSlidingWindow(nums7, k7)
    expected7 = [-1, -2, -3]
    assert (
        result7 == expected7
    ), f"Failed for nums={nums7}, k={k7}, expected {expected7}, got {result7}"

    # Test Case 8: Mixed positive and negative
    nums8, k8 = [1, -1, 2, -2, 3, -3], 2
    result8 = solution.maxSlidingWindow(nums8, k8)
    expected8 = [1, 2, 2, 3, 3]
    assert (
        result8 == expected8
    ), f"Failed for nums={nums8}, k={k8}, expected {expected8}, got {result8}"

    # Test Case 9: Large numbers
    nums9, k9 = [10000, -10000, 5000, -5000], 2
    result9 = solution.maxSlidingWindow(nums9, k9)
    expected9 = [10000, 5000, 5000]
    assert (
        result9 == expected9
    ), f"Failed for nums={nums9}, k={k9}, expected {expected9}, got {result9}"

    # Test Case 10: Edge case
    nums10, k10 = [7, 2, 4], 2
    result10 = solution.maxSlidingWindow(nums10, k10)
    expected10 = [7, 4]
    assert (
        result10 == expected10
    ), f"Failed for nums={nums10}, k={k10}, expected {expected10}, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tWindow Count")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        nums = [random.randint(-10000, 10000) for _ in range(size)]
        k = random.randint(1, min(100, size))

        # Test approach
        start_time = time.time()
        result = solution.maxSlidingWindow(nums, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)}")

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
    nums = [random.randint(-10000, 10000) for _ in range(100000)]
    k = 50000
    result = solution.maxSlidingWindow(nums, k)
    print(f"Maximum length (100k elements): {len(result)} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [10000] * 1000 + [-10000] * 1000
    k = 100
    result = solution.maxSlidingWindow(nums, k)
    print(f"Maximum constraint values: {len(result)} ✅")

    # Edge Case 3: k equals 1
    nums = [random.randint(-10000, 10000) for _ in range(1000)]
    k = 1
    result = solution.maxSlidingWindow(nums, k)
    print(f"k equals 1: {len(result)} ✅")

    # Edge Case 4: k equals array length
    nums = [random.randint(-10000, 10000) for _ in range(1000)]
    k = len(nums)
    result = solution.maxSlidingWindow(nums, k)
    print(f"k equals array length: {len(result)} ✅")

    # Edge Case 5: All zeros
    nums = [0] * 1000
    k = 100
    result = solution.maxSlidingWindow(nums, k)
    print(f"All zeros: {len(result)} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = [random.randint(-10000, 10000) for _ in range(100000)]
    k = 1000

    start_time = time.time()
    result = solution.maxSlidingWindow(nums, k)
    time1 = time.time() - start_time

    print(f"Large dataset (100k elements, k=1000):")
    print(f"Time: {time1:.6f}s, Window count: {len(result)}")


if __name__ == "__main__":
    print("🧪 Testing Sliding Window Maximum Problem")
    print("=" * 70)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxSlidingWindow method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use deque or monotonic queue")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using deque or monotonic queue")

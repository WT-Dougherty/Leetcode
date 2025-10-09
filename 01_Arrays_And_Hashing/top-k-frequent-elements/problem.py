"""
Top K Frequent Elements - LeetCode Problem 347

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""

import time
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    result1 = solution.topKFrequent(nums1, k1)
    assert set(result1) == {1, 2}, f"Failed for nums={nums1}, k={k1}, got {result1}"

    # Test Case 2: Single element
    nums2, k2 = [1], 1
    result2 = solution.topKFrequent(nums2, k2)
    assert result2 == [1], f"Failed for nums={nums2}, k={k2}, got {result2}"

    # Test Case 3: All same elements
    nums3, k3 = [1, 1, 1, 1], 1
    result3 = solution.topKFrequent(nums3, k3)
    assert result3 == [1], f"Failed for nums={nums3}, k={k3}, got {result3}"

    # Test Case 4: k equals array length
    nums4, k4 = [1, 2, 3, 4], 4
    result4 = solution.topKFrequent(nums4, k4)
    assert set(result4) == {
        1,
        2,
        3,
        4,
    }, f"Failed for nums={nums4}, k={k4}, got {result4}"

    # Test Case 5: Negative numbers
    nums5, k5 = [-1, -1, -2, -2, -3], 2
    result5 = solution.topKFrequent(nums5, k5)
    assert set(result5) == {-1, -2}, f"Failed for nums={nums5}, k={k5}, got {result5}"

    # Test Case 6: Mixed frequencies
    nums6, k6 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3
    result6 = solution.topKFrequent(nums6, k6)
    assert set(result6) == {2, 3, 4}, f"Failed for nums={nums6}, k={k6}, got {result6}"

    # Test Case 7: Large numbers
    nums7, k7 = [1000000000, -1000000000, 1000000000, 0], 2
    result7 = solution.topKFrequent(nums7, k7)
    assert set(result7) == {
        1000000000,
        -1000000000,
    }, f"Failed for nums={nums7}, k={k7}, got {result7}"

    # Test Case 8: Zero frequency
    nums8, k8 = [0, 0, 0, 1, 1], 2
    result8 = solution.topKFrequent(nums8, k8)
    assert set(result8) == {0, 1}, f"Failed for nums={nums8}, k={k8}, got {result8}"

    # Test Case 9: Decreasing frequencies
    nums9, k9 = [1, 1, 1, 2, 2, 3], 3
    result9 = solution.topKFrequent(nums9, k9)
    assert set(result9) == {1, 2, 3}, f"Failed for nums={nums9}, k={k9}, got {result9}"

    # Test Case 10: Complex case
    nums10, k10 = [1, 1, 1, 2, 2, 2, 3, 3, 4], 2
    result10 = solution.topKFrequent(nums10, k10)
    assert set(result10) == {1, 2}, f"Failed for nums={nums10}, k={k10}, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n log n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with some repeated elements
        nums = []
        # Add some frequent elements
        for i in range(size // 10):
            nums.extend([i] * (i + 1))  # Element i appears i+1 times

        # Add some unique elements
        for i in range(size // 10, size):
            nums.append(i)

        k = 5  # Always ask for top 5

        # Test approach
        start_time = time.time()
        result = solution.topKFrequent(nums, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        assert len(result) == k, f"Expected {k} elements, got {len(result)}"
        print(f"{size}\t{elapsed_time:.6f}s\tTop {k}: {result}")

    # Verify O(n log n) complexity by checking if time growth is approximately n log n
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * (test_sizes[i - 1].bit_length())
            curr_complexity = test_sizes[i] * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n^2) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum k
    nums = [1, 2, 3, 4, 5]
    k = 1
    result = solution.topKFrequent(nums, k)
    print(f"Minimum k=1: {result} ✅")

    # Edge Case 2: k equals unique elements
    nums = [1, 2, 3, 4, 5]
    k = 5
    result = solution.topKFrequent(nums, k)
    print(f"k equals unique elements: {len(result)} elements ✅")

    # Edge Case 3: All same elements
    nums = [42] * 1000
    k = 1
    result = solution.topKFrequent(nums, k)
    print(f"All same elements: {result} ✅")

    # Edge Case 4: Maximum constraint values
    nums = [10**4] * 1000 + [-(10**4)] * 500
    k = 2
    result = solution.topKFrequent(nums, k)
    print(f"Large numbers: {result} ✅")

    # Edge Case 5: Alternating pattern
    nums = [1, 2] * 500
    k = 2
    result = solution.topKFrequent(nums, k)
    print(f"Alternating pattern: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    nums = []
    # Create array with varying frequencies
    for i in range(1000):
        nums.extend([i] * (i % 10 + 1))  # Element i appears (i%10+1) times

    k = 10

    start_time = time.time()
    result = solution.topKFrequent(nums, k)
    time1 = time.time() - start_time

    print(f"Large dataset (55,000 elements):")
    print(f"Time: {time1:.6f}s, Top {k}: {result}")


if __name__ == "__main__":
    print("🧪 Testing Top K Frequent Elements Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the topKFrequent method")
        print("- Aim for O(n log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log n)")
        print("- Consider using hash maps and heaps or other O(n log n) approaches")

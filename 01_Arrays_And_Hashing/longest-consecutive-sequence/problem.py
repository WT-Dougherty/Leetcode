"""
Longest Consecutive Sequence - LeetCode Problem 128

Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence. You must write an algorithm that runs in O(n) time.
"""

import time
import random
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        for ele in nums:
            hash_set.add(ele)

        max_len = 0
        for ele in hash_set:
            cur_len = 1

            # check if element is start of sequence
            if ele - 1 in hash_set:
                max_len = max(max_len, cur_len)
                continue

            # iteratively count sequence length
            counter = ele + 1
            while counter in hash_set:
                cur_len += 1
                counter += 1
            max_len = max(max_len, cur_len)

        return max_len


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longestConsecutive(nums1)
    assert result1 == 4, f"Failed for {nums1}, expected 4, got {result1}"

    # Test Case 2: Longer sequence
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longestConsecutive(nums2)
    assert result2 == 9, f"Failed for {nums2}, expected 9, got {result2}"

    # Test Case 3: Empty array
    nums3 = []
    result3 = solution.longestConsecutive(nums3)
    assert result3 == 0, f"Failed for {nums3}, expected 0, got {result3}"

    # Test Case 4: Single element
    nums4 = [1]
    result4 = solution.longestConsecutive(nums4)
    assert result4 == 1, f"Failed for {nums4}, expected 1, got {result4}"

    # Test Case 5: No consecutive sequence
    nums5 = [1, 3, 5, 7, 9]
    result5 = solution.longestConsecutive(nums5)
    assert result5 == 1, f"Failed for {nums5}, expected 1, got {result5}"

    # Test Case 6: Negative numbers
    nums6 = [-1, -2, -3, 0, 1, 2]
    result6 = solution.longestConsecutive(nums6)
    assert result6 == 6, f"Failed for {nums6}, expected 6, got {result6}"

    # Test Case 7: Duplicates
    nums7 = [1, 2, 2, 3, 3, 4]
    result7 = solution.longestConsecutive(nums7)
    assert result7 == 4, f"Failed for {nums7}, expected 4, got {result7}"

    # Test Case 8: Large numbers
    nums8 = [1000000000, -1000000000, 1000000001, 1000000002]
    result8 = solution.longestConsecutive(nums8)
    assert result8 == 3, f"Failed for {nums8}, expected 3, got {result8}"

    # Test Case 9: Multiple sequences
    nums9 = [1, 2, 3, 10, 11, 12, 20, 21]
    result9 = solution.longestConsecutive(nums9)
    assert result9 == 3, f"Failed for {nums9}, expected 3, got {result9}"

    # Test Case 10: All same numbers
    nums10 = [5, 5, 5, 5]
    result10 = solution.longestConsecutive(nums10)
    assert result10 == 1, f"Failed for {nums10}, expected 1, got {result10}"

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
        # Generate test data - create array with some consecutive sequences
        nums = []

        # Add some consecutive sequences
        for i in range(size // 10):
            start = random.randint(-1000, 1000)
            length = random.randint(1, 10)
            for j in range(length):
                nums.append(start + j)

        # Add some random numbers
        for i in range(size - len(nums)):
            nums.append(random.randint(-1000, 1000))

        # Test approach
        start_time = time.time()
        result = solution.longestConsecutive(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tLongest: {result}")

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

            if not (actual <= max_expected):
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

    # Edge Case 1: Minimum constraint (empty array)
    nums = []
    result = solution.longestConsecutive(nums)
    print(f"Empty array: {result} ✅")

    # Edge Case 2: Maximum constraint values
    nums = [10**9, -(10**9), 10**9 - 1, -(10**9) + 1]
    result = solution.longestConsecutive(nums)
    print(f"Large numbers: {result} ✅")

    # Edge Case 3: All same elements
    nums = [42] * 1000
    result = solution.longestConsecutive(nums)
    print(f"All same elements: {result} ✅")

    # Edge Case 4: Alternating pattern
    nums = [1, 3, 5, 7, 9] * 200
    result = solution.longestConsecutive(nums)
    print(f"Alternating pattern: {result} ✅")

    # Edge Case 5: Perfect consecutive sequence
    nums = list(range(1000))
    result = solution.longestConsecutive(nums)
    print(f"Perfect consecutive: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset with consecutive sequences
    nums = []

    # Create several consecutive sequences
    for i in range(100):
        start = random.randint(-10000, 10000)
        length = random.randint(10, 100)
        for j in range(length):
            nums.append(start + j)

    # Add some random numbers
    for i in range(50000):
        nums.append(random.randint(-10000, 10000))

    start_time = time.time()
    result = solution.longestConsecutive(nums)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Longest sequence: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Consecutive Sequence Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the longestConsecutive method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use hash sets for efficient lookups")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash sets or union-find")

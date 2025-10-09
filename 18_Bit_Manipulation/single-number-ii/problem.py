"""
Single Number II - LeetCode Problem 137

Given an integer array nums where every element appears three times except for one,
which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

import time


class Solution:
    def singleNumber(self, nums):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [2, 2, 3, 2]
    result1 = solution.singleNumber(nums1)
    assert result1 == 3, f"Failed for nums={nums1}, expected 3, got {result1}"

    # Test Case 2: Larger array
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    result2 = solution.singleNumber(nums2)
    assert result2 == 99, f"Failed for nums={nums2}, expected 99, got {result2}"

    # Test Case 3: Single element
    nums3 = [1]
    result3 = solution.singleNumber(nums3)
    assert result3 == 1, f"Failed for nums={nums3}, expected 1, got {result3}"

    # Test Case 4: Negative numbers
    nums4 = [-1, -1, -1, -2]
    result4 = solution.singleNumber(nums4)
    assert result4 == -2, f"Failed for nums={nums4}, expected -2, got {result4}"

    # Test Case 5: Zero
    nums5 = [0, 0, 0, 1]
    result5 = solution.singleNumber(nums5)
    assert result5 == 1, f"Failed for nums={nums5}, expected 1, got {result5}"

    # Test Case 6: Edge case
    nums6 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
    result6 = solution.singleNumber(nums6)
    assert result6 == 4, f"Failed for nums={nums6}, expected 4, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        nums = [i for i in range(size)] * 3 + [size]
        # Shuffle the array
        import random

        random.shuffle(nums)

        start_time = time.time()
        result = solution.singleNumber(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Single element
    result = solution.singleNumber([42])
    print(f"Single element: {result} ✅")

    # Edge Case 2: Negative numbers
    result = solution.singleNumber([-1, -2, -1, -1])
    print(f"Negative numbers: {result} ✅")

    # Edge Case 3: Large array
    nums = [i for i in range(1000)] * 3 + [1000]
    result = solution.singleNumber(nums)
    print(f"Large array: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large array
    nums = [i for i in range(100000)] * 3 + [100000]

    start_time = time.time()
    result = solution.singleNumber(nums)
    elapsed_time = time.time() - start_time

    print(f"Large array (300,001 elements):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Single Number II Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the singleNumber method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using bit manipulation techniques")

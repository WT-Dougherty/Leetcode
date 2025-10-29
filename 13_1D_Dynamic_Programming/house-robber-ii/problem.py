"""
House Robber II - LeetCode Problem 213

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this
place are arranged in a circle. That means the first house is the neighbor
of the last house. Meanwhile, adjacent houses have a security system
connected, and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""

import time
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(a: List[int]) -> int:
            if len(a) < 3:
                return max(a)
            dp = [0] * len(a)
            dp[0] = a[0]
            dp[1] = max(dp[0], a[1])

            for i in range(2, len(a)):
                dp[i] = max(dp[i - 1], a[i] + dp[i - 2])
            return dp[-1]

        if len(nums) < 4:
            return max(nums)
        return max(rob1(nums[1:]), rob1(nums[:-1]))


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [2, 3, 2]
    result1 = solution.rob(nums1)
    assert result1 == 3, f"Failed for {nums1}, expected 3, got {result1}"

    # Test Case 2: Four houses
    nums2 = [1, 2, 3, 1]
    result2 = solution.rob(nums2)
    assert result2 == 4, f"Failed for {nums2}, expected 4, got {result2}"

    # Test Case 3: Three houses
    nums3 = [1, 2, 3]
    result3 = solution.rob(nums3)
    assert result3 == 3, f"Failed for {nums3}, expected 3, got {result3}"

    # Test Case 4: Two houses
    nums4 = [2, 1]
    result4 = solution.rob(nums4)
    assert result4 == 2, f"Failed for {nums4}, expected 2, got {result4}"

    # Test Case 5: Single house
    nums5 = [5]
    result5 = solution.rob(nums5)
    assert result5 == 5, f"Failed for {nums5}, expected 5, got {result5}"

    # Test Case 6: All same values
    nums6 = [3, 3, 3]
    result6 = solution.rob(nums6)
    assert result6 == 3, f"Failed for {nums6}, expected 3, got {result6}"

    # Test Case 7: Complex case
    nums7 = [1, 2, 3, 4, 5]
    result7 = solution.rob(nums7)
    assert result7 == 8, f"Failed for {nums7}, expected 8, got {result7}"

    # Test Case 8: Edge case
    nums8 = [2, 1, 1, 2]
    result8 = solution.rob(nums8)
    assert result8 == 3, f"Failed for {nums8}, expected 3, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with random values
        nums = [i % 10 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.rob(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity
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
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
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

    # Edge Case 1: Minimum constraint (1 house)
    nums1 = [100]
    result1 = solution.rob(nums1)
    assert result1 == 100, f"Single house failed: {result1}"
    print(f"Single house: ✅")

    # Edge Case 2: Maximum constraint (100 houses)
    nums2 = [i % 1000 + 1 for i in range(100)]
    result2 = solution.rob(nums2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum money (1000)
    nums3 = [1000, 1, 1000]
    result3 = solution.rob(nums3)
    assert result3 == 1000, f"Max money failed: {result3}"
    print(f"Maximum money: ✅")

    # Edge Case 4: Minimum money (0)
    nums4 = [0, 0, 0]
    result4 = solution.rob(nums4)
    assert result4 == 0, f"Min money failed: {result4}"
    print(f"Minimum money: ✅")

    # Edge Case 5: Two houses
    nums5 = [1, 2]
    result5 = solution.rob(nums5)
    assert result5 == 2, f"Two houses failed: {result5}"
    print(f"Two houses: ✅")

    # Edge Case 6: All zeros
    nums6 = [0] * 10
    result6 = solution.rob(nums6)
    assert result6 == 0, f"All zeros failed: {result6}"
    print(f"All zeros: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking House Robber II:")

    # Large dataset
    nums = [i % 10 + 1 for i in range(100)]

    start_time = time.time()
    result = solution.rob(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100 houses):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing House Robber II Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the rob method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming with circular constraint")

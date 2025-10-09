"""
Permutations - LeetCode Problem 46

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

import time
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(result1) == len(
        expected1
    ), f"Failed for [1,2,3], expected {len(expected1)} permutations, got {len(result1)}"
    for perm in expected1:
        assert perm in result1, f"Missing permutation {perm} in result {result1}"

    # Test Case 2: Two elements
    nums2 = [0, 1]
    result2 = solution.permute(nums2)
    expected2 = [[0, 1], [1, 0]]
    assert len(result2) == len(
        expected2
    ), f"Failed for [0,1], expected {len(expected2)} permutations, got {len(result2)}"
    for perm in expected2:
        assert perm in result2, f"Missing permutation {perm} in result {result2}"

    # Test Case 3: Single element
    nums3 = [1]
    result3 = solution.permute(nums3)
    expected3 = [[1]]
    assert result3 == expected3, f"Failed for [1], expected {expected3}, got {result3}"

    # Test Case 4: Four elements
    nums4 = [1, 2, 3, 4]
    result4 = solution.permute(nums4)
    expected4_count = 24  # 4! = 24
    assert (
        len(result4) == expected4_count
    ), f"Failed for [1,2,3,4], expected {expected4_count} permutations, got {len(result4)}"

    # Test Case 5: Five elements
    nums5 = [1, 2, 3, 4, 5]
    result5 = solution.permute(nums5)
    expected5_count = 120  # 5! = 120
    assert (
        len(result5) == expected5_count
    ), f"Failed for [1,2,3,4,5], expected {expected5_count} permutations, got {len(result5)}"

    # Test Case 6: Negative numbers
    nums6 = [-1, 0, 1]
    result6 = solution.permute(nums6)
    expected6_count = 6  # 3! = 6
    assert (
        len(result6) == expected6_count
    ), f"Failed for [-1,0,1], expected {expected6_count} permutations, got {len(result6)}"

    # Test Case 7: Large numbers
    nums7 = [10, 20, 30]
    result7 = solution.permute(nums7)
    expected7_count = 6  # 3! = 6
    assert (
        len(result7) == expected7_count
    ), f"Failed for [10,20,30], expected {expected7_count} permutations, got {len(result7)}"

    # Test Case 8: Six elements
    nums8 = [1, 2, 3, 4, 5, 6]
    result8 = solution.permute(nums8)
    expected8_count = 720  # 6! = 720
    assert (
        len(result8) == expected8_count
    ), f"Failed for [1,2,3,4,5,6], expected {expected8_count} permutations, got {len(result8)}"

    # Verify all permutations are valid
    for nums in [[1, 2, 3], [0, 1], [1, 2, 3, 4]]:
        result = solution.permute(nums)
        for perm in result:
            # Check that permutation has same length as original
            assert len(perm) == len(nums), f"Permutation {perm} has wrong length"
            # Check that permutation contains all elements from original
            assert set(perm) == set(
                nums
            ), f"Permutation {perm} doesn't contain all elements from {nums}"
            # Check that permutation has no duplicates
            assert len(perm) == len(set(perm)), f"Permutation {perm} has duplicates"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [3, 4, 5]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        nums = list(range(size))

        # Test approach
        start_time = time.time()
        result = solution.permute(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} permutations")

    # Verify O(N!) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(N!) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(N!): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance for factorial complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(N!)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(N!) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(N!), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(N!)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 element)
    nums1 = [1]
    result1 = solution.permute(nums1)
    assert result1 == [[1]], f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (6 elements)
    nums2 = [1, 2, 3, 4, 5, 6]
    result2 = solution.permute(nums2)
    assert len(result2) == 720, f"Max constraint failed: {len(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Negative numbers
    nums3 = [-10, 0, 10]
    result3 = solution.permute(nums3)
    assert len(result3) == 6, f"Negative numbers failed: {len(result3)}"
    print(f"Negative numbers: ✅")

    # Edge Case 4: Large numbers
    nums4 = [1000000, 2000000, 3000000]
    result4 = solution.permute(nums4)
    assert len(result4) == 6, f"Large numbers failed: {len(result4)}"
    print(f"Large numbers: ✅")

    # Edge Case 5: Zero
    nums5 = [0, 1, 2]
    result5 = solution.permute(nums5)
    assert len(result5) == 6, f"Zero included failed: {len(result5)}"
    print(f"Zero included: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Permutations:")

    # Large dataset
    nums = [1, 2, 3, 4, 5, 6]

    start_time = time.time()
    result = solution.permute(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (6 elements):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} permutations")


if __name__ == "__main__":
    print("🧪 Testing Permutations Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the permute method")
        print("- Aim for O(N!) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(N!)")
        print("- Consider using backtracking approach")

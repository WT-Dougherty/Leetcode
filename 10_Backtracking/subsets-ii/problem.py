"""
Subsets II - LeetCode Problem 90

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""

import time
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case with duplicates
    nums1 = [1, 2, 2]
    result1 = solution.subsetsWithDup(nums1)
    expected1 = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert len(result1) == len(
        expected1
    ), f"Failed for [1,2,2], expected {len(expected1)} subsets, got {len(result1)}"
    for subset in expected1:
        assert subset in result1, f"Missing subset {subset} in result {result1}"

    # Test Case 2: Single element
    nums2 = [0]
    result2 = solution.subsetsWithDup(nums2)
    expected2 = [[], [0]]
    assert len(result2) == len(
        expected2
    ), f"Failed for [0], expected {len(expected2)} subsets, got {len(result2)}"
    for subset in expected2:
        assert subset in result2, f"Missing subset {subset} in result {result2}"

    # Test Case 3: All same elements
    nums3 = [1, 1, 1]
    result3 = solution.subsetsWithDup(nums3)
    expected3 = [[], [1], [1, 1], [1, 1, 1]]
    assert len(result3) == len(
        expected3
    ), f"Failed for [1,1,1], expected {len(expected3)} subsets, got {len(result3)}"
    for subset in expected3:
        assert subset in result3, f"Missing subset {subset} in result {result3}"

    # Test Case 4: No duplicates
    nums4 = [1, 2, 3]
    result4 = solution.subsetsWithDup(nums4)
    expected4 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert len(result4) == len(
        expected4
    ), f"Failed for [1,2,3], expected {len(expected4)} subsets, got {len(result4)}"
    for subset in expected4:
        assert subset in result4, f"Missing subset {subset} in result {result4}"

    # Test Case 5: Multiple duplicates
    nums5 = [1, 1, 2, 2]
    result5 = solution.subsetsWithDup(nums5)
    expected5 = [
        [],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 2, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2],
    ]
    assert len(result5) == len(
        expected5
    ), f"Failed for [1,1,2,2], expected {len(expected5)} subsets, got {len(result5)}"
    for subset in expected5:
        assert subset in result5, f"Missing subset {subset} in result {result5}"

    # Test Case 6: Negative numbers with duplicates
    nums6 = [-1, 0, 1, -1]
    result6 = solution.subsetsWithDup(nums6)
    # Verify all subsets are valid
    for subset in result6:
        # Check that subset contains only elements from original array
        for element in subset:
            assert (
                element in nums6
            ), f"Subset {subset} contains element {element} not in {nums6}"

    # Test Case 7: Large numbers with duplicates
    nums7 = [10, 20, 10, 30]
    result7 = solution.subsetsWithDup(nums7)
    # Verify all subsets are valid
    for subset in result7:
        # Check that subset contains only elements from original array
        for element in subset:
            assert (
                element in nums7
            ), f"Subset {subset} contains element {element} not in {nums7}"

    # Test Case 8: Complex case
    nums8 = [1, 2, 2, 3, 3, 3]
    result8 = solution.subsetsWithDup(nums8)
    # Verify all subsets are valid
    for subset in result8:
        # Check that subset contains only elements from original array
        for element in subset:
            assert (
                element in nums8
            ), f"Subset {subset} contains element {element} not in {nums8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [5, 8, 10]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data with duplicates
        nums = [
            i for i in range(size // 2) for _ in range(2)
        ]  # Each number appears twice

        # Test approach
        start_time = time.time()
        result = solution.subsetsWithDup(nums)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} subsets")

    # Verify O(2^N) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(2^N) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = 2 ** (test_sizes[i] - test_sizes[i - 1])
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(2^N): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance for exponential complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(2^N)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(2^N) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(2^N), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(2^N)")
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
    result1 = solution.subsetsWithDup(nums1)
    assert result1 == [[], [1]], f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint (10 elements)
    nums2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    result2 = solution.subsetsWithDup(nums2)
    assert len(result2) > 0, f"Max constraint failed: {len(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same elements
    nums3 = [5] * 10
    result3 = solution.subsetsWithDup(nums3)
    assert len(result3) == 11, f"All same elements failed: {len(result3)}"
    print(f"All same elements: ✅")

    # Edge Case 4: Negative numbers
    nums4 = [-10, 0, 10, -10]
    result4 = solution.subsetsWithDup(nums4)
    assert len(result4) > 0, f"Negative numbers failed: {len(result4)}"
    print(f"Negative numbers: ✅")

    # Edge Case 5: Large numbers
    nums5 = [1000000, 2000000, 1000000]
    result5 = solution.subsetsWithDup(nums5)
    assert len(result5) > 0, f"Large numbers failed: {len(result5)}"
    print(f"Large numbers: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Subsets II:")

    # Large dataset
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

    start_time = time.time()
    result = solution.subsetsWithDup(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10 elements with duplicates):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} subsets")


if __name__ == "__main__":
    print("🧪 Testing Subsets II Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the subsetsWithDup method")
        print("- Aim for O(2^N) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(2^N)")
        print("- Consider using backtracking with duplicate handling")

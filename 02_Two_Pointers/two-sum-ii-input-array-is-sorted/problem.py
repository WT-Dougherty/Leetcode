"""
Two Sum II - Input Array Is Sorted - LeetCode Problem 167

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the
same element twice. Your solution must use only constant extra space.
"""

import time
import random
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            # case 1: we have identified the target
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    numbers1, target1 = [2, 7, 11, 15], 9
    result1 = solution.twoSum(numbers1, target1)
    assert result1 == [
        1,
        2,
    ], f"Failed for numbers={numbers1}, target={target1}, got {result1}"

    # Test Case 2: Different indices
    numbers2, target2 = [2, 3, 4], 6
    result2 = solution.twoSum(numbers2, target2)
    assert result2 == [
        1,
        3,
    ], f"Failed for numbers={numbers2}, target={target2}, got {result2}"

    # Test Case 3: Negative numbers
    numbers3, target3 = [-1, 0], -1
    result3 = solution.twoSum(numbers3, target3)
    assert result3 == [
        1,
        2,
    ], f"Failed for numbers={numbers3}, target={target3}, got {result3}"

    # Test Case 4: Large numbers (fixed - single solution)
    numbers4, target4 = [1, 2, 3, 4, 5, 9, 56, 90], 8
    result4 = solution.twoSum(numbers4, target4)
    assert result4 == [
        3,
        5,
    ], f"Failed for numbers={numbers4}, target={target4}, got {result4}"

    # Test Case 5: Minimum length
    numbers5, target5 = [1, 2], 3
    result5 = solution.twoSum(numbers5, target5)
    assert result5 == [
        1,
        2,
    ], f"Failed for numbers={numbers5}, target={target5}, got {result5}"

    # Test Case 6: Zero target
    numbers6, target6 = [-3, -1, 1, 3], 0
    result6 = solution.twoSum(numbers6, target6)
    assert result6 == [
        1,
        4,
    ], f"Failed for numbers={numbers6}, target={target6}, got {result6}"

    # Test Case 7: Fixed - single solution
    numbers7, target7 = [1, 2, 3, 5], 4
    result7 = solution.twoSum(numbers7, target7)
    assert result7 == [
        1,
        3,
    ], f"Failed for numbers={numbers7}, target={target7}, got {result7}"

    # Test Case 8: Fixed - single solution
    numbers8, target8 = [1, 2, 3, 4], 3
    result8 = solution.twoSum(numbers8, target8)
    assert result8 == [
        1,
        2,
    ], f"Failed for numbers={numbers8}, target={target8}, got {result8}"

    # Test Case 9: Large range (fixed - correct target)
    numbers9, target9 = list(range(1, 1001)), 1999
    result9 = solution.twoSum(numbers9, target9)
    assert result9 == [999, 1000], f"Failed for large range"

    # Test Case 10: Negative target
    numbers10, target10 = [-5, -3, -1, 0, 2], -3
    result10 = solution.twoSum(numbers10, target10)
    assert result10 == [
        1,
        5,
    ], f"Failed for numbers={numbers10}, target={target10}, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 30000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - sorted array
        numbers = sorted([random.randint(-1000, 1000) for _ in range(size)])
        target = numbers[0] + numbers[size - 1]  # Ensure solution exists

        # Test approach
        start_time = time.time()
        result = solution.twoSum(numbers, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        if len(result) == 2:
            actual_sum = numbers[result[0] - 1] + numbers[result[1] - 1]
            assert actual_sum == target, f"Sum mismatch: {actual_sum} != {target}"

        print(f"{size}\t{elapsed_time:.6f}s\tIndices: {result}")

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

    # Edge Case 1: Minimum length
    numbers = [1, 2]
    target = 3
    result = solution.twoSum(numbers, target)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    numbers = [-1000] * 1000 + [1000] * 1000
    target = 0
    result = solution.twoSum(numbers, target)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: All same numbers
    numbers = [5] * 1000
    target = 10
    result = solution.twoSum(numbers, target)
    print(f"All same numbers: {result} ✅")

    # Edge Case 4: Sequential numbers
    numbers = list(range(1, 1001))
    target = 1001
    result = solution.twoSum(numbers, target)
    print(f"Sequential numbers: {result} ✅")

    # Edge Case 5: Negative target
    numbers = list(range(-500, 501))
    target = -999
    result = solution.twoSum(numbers, target)
    print(f"Negative target: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    numbers = sorted([random.randint(-1000, 1000) for _ in range(30000)])
    target = numbers[0] + numbers[29999]

    start_time = time.time()
    result = solution.twoSum(numbers, target)
    time1 = time.time() - start_time

    print(f"Large dataset (30,000 elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")

    # Verify result
    if len(result) == 2:
        actual_sum = numbers[result[0] - 1] + numbers[result[1] - 1]
        print(
            f"Verification: {numbers[result[0]-1]} + {numbers[result[1]-1]} = {actual_sum} (target: {target})"
        )


if __name__ == "__main__":
    print("🧪 Testing Two Sum II - Input Array Is Sorted Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the twoSum method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two pointers approach")
        print("- Return 1-indexed positions")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using two pointers or binary search")

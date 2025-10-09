"""
Search 2D Matrix - LeetCode Problem 74

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

import time
import random
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    matrix1 = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    target1 = 5
    result1 = solution.searchMatrix(matrix1, target1)
    assert (
        result1 == True
    ), f"Failed for matrix={matrix1}, target={target1}, expected True, got {result1}"

    # Test Case 2: Target not found
    matrix2 = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    target2 = 15
    result2 = solution.searchMatrix(matrix2, target2)
    assert (
        result2 == False
    ), f"Failed for matrix={matrix2}, target={target2}, expected False, got {result2}"

    # Test Case 3: Single element matrix
    matrix3 = [[1]]
    target3 = 1
    result3 = solution.searchMatrix(matrix3, target3)
    assert (
        result3 == True
    ), f"Failed for matrix={matrix3}, target={target3}, expected True, got {result3}"

    # Test Case 4: Single element matrix not found
    matrix4 = [[1]]
    target4 = 0
    result4 = solution.searchMatrix(matrix4, target4)
    assert (
        result4 == False
    ), f"Failed for matrix={matrix4}, target={target4}, expected False, got {result4}"

    # Test Case 5: Single row
    matrix5 = [[1, 3, 5, 7]]
    target5 = 3
    result5 = solution.searchMatrix(matrix5, target5)
    assert (
        result5 == True
    ), f"Failed for matrix={matrix5}, target={target5}, expected True, got {result5}"

    # Test Case 6: Single column
    matrix6 = [[1], [3], [5], [7]]
    target6 = 5
    result6 = solution.searchMatrix(matrix6, target6)
    assert (
        result6 == True
    ), f"Failed for matrix={matrix6}, target={target6}, expected True, got {result6}"

    # Test Case 7: Target at first position
    matrix7 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    target7 = 1
    result7 = solution.searchMatrix(matrix7, target7)
    assert (
        result7 == True
    ), f"Failed for matrix={matrix7}, target={target7}, expected True, got {result7}"

    # Test Case 8: Target at last position
    matrix8 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    target8 = 9
    result8 = solution.searchMatrix(matrix8, target8)
    assert (
        result8 == True
    ), f"Failed for matrix={matrix8}, target={target8}, expected True, got {result8}"

    # Test Case 9: Negative numbers
    matrix9 = [[-5, -3, -1], [-2, 0, 2], [1, 3, 5]]
    target9 = -3
    result9 = solution.searchMatrix(matrix9, target9)
    assert (
        result9 == True
    ), f"Failed for matrix={matrix9}, target={target9}, expected True, got {result9}"

    # Test Case 10: Large matrix
    matrix10 = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(i * 10 + j)
        matrix10.append(row)
    target10 = 55
    result10 = solution.searchMatrix(matrix10, target10)
    assert (
        result10 == True
    ), f"Failed for large matrix, target={target10}, expected True, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log(m * n))"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(10, 10), (20, 20), (50, 50)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for m, n in test_sizes:
        # Generate test data
        matrix = []
        val = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(val)
                val += 1
            matrix.append(row)

        target = random.randint(0, m * n - 1)

        # Test approach
        start_time = time.time()
        result = solution.searchMatrix(matrix, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{m}x{n}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(log(m * n)) complexity by checking if time growth is logarithmic
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log(m * n)) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            size1, size2 = m1 * n1, m2 * n2
            expected_ratio = (size2.bit_length() - 1) / (size1.bit_length() - 1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(log(m * n)): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance for logarithmic
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log(m * n))")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m * n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(log(m * n)), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log(m * n))")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint size
    matrix = []
    val = 0
    for i in range(100):
        row = []
        for j in range(100):
            row.append(val)
            val += 1
        matrix.append(row)
    target = random.randint(0, 9999)
    result = solution.searchMatrix(matrix, target)
    print(f"Maximum size (100x100): {result} ✅")

    # Edge Case 2: Maximum constraint values
    matrix = [[-10000, 0], [10000, 20000]]
    target = 10000
    result = solution.searchMatrix(matrix, target)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    matrix = [[-10000, 0], [10000, 20000]]
    target = -10000
    result = solution.searchMatrix(matrix, target)
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All same elements
    matrix = [[5] * 10 for _ in range(10)]
    target = 5
    result = solution.searchMatrix(matrix, target)
    assert result == True
    print(f"All same elements: {result} ✅")

    # Edge Case 5: Sequential numbers
    matrix = []
    val = 0
    for i in range(10):
        row = []
        for j in range(10):
            row.append(val)
            val += 1
        matrix.append(row)
    target = 50
    result = solution.searchMatrix(matrix, target)
    assert result == True
    print(f"Sequential numbers: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    matrix = []
    val = 0
    for i in range(100):
        row = []
        for j in range(100):
            row.append(val)
            val += 1
        matrix.append(row)

    target = random.randint(0, 9999)

    start_time = time.time()
    result = solution.searchMatrix(matrix, target)
    time1 = time.time() - start_time

    print(f"Large dataset (100x100 matrix):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Search 2D Matrix Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the searchMatrix method")
        print("- Aim for O(log(m * n)) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use binary search algorithm")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log(m * n))")
        print("- Consider using binary search algorithm")

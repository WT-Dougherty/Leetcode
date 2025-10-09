"""
Longest Increasing Path in a Matrix - LeetCode Problem 329

Given an m x n integers matrix, return the length of the longest increasing path.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

import time
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    result1 = solution.longestIncreasingPath(matrix1)
    assert result1 == 4, f"Failed for {matrix1}, expected 4, got {result1}"

    # Test Case 2: Another case
    matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    result2 = solution.longestIncreasingPath(matrix2)
    assert result2 == 4, f"Failed for {matrix2}, expected 4, got {result2}"

    # Test Case 3: Single cell
    matrix3 = [[1]]
    result3 = solution.longestIncreasingPath(matrix3)
    assert result3 == 1, f"Failed for {matrix3}, expected 1, got {result3}"

    # Test Case 4: Single row
    matrix4 = [[1, 2, 3, 4, 5]]
    result4 = solution.longestIncreasingPath(matrix4)
    assert result4 == 5, f"Failed for {matrix4}, expected 5, got {result4}"

    # Test Case 5: Single column
    matrix5 = [[1], [2], [3], [4], [5]]
    result5 = solution.longestIncreasingPath(matrix5)
    assert result5 == 5, f"Failed for {matrix5}, expected 5, got {result5}"

    # Test Case 6: All same values
    matrix6 = [[1, 1], [1, 1]]
    result6 = solution.longestIncreasingPath(matrix6)
    assert result6 == 1, f"Failed for {matrix6}, expected 1, got {result6}"

    # Test Case 7: Complex case
    matrix7 = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    result7 = solution.longestIncreasingPath(matrix7)
    assert result7 == 9, f"Failed for {matrix7}, expected 9, got {result7}"

    # Test Case 8: Edge case
    matrix8 = [[1, 2], [2, 1]]
    result8 = solution.longestIncreasingPath(matrix8)
    assert result8 == 2, f"Failed for {matrix8}, expected 2, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [20, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create matrix with increasing values
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i * size + j)
            matrix.append(row)

        # Test approach
        start_time = time.time()
        result = solution.longestIncreasingPath(matrix)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}x{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * test_sizes[i - 1]
            curr_complexity = test_sizes[i] * test_sizes[i]
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m*n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(m * n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m * n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m * n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1x1)
    matrix1 = [[1]]
    result1 = solution.longestIncreasingPath(matrix1)
    assert result1 == 1, f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (200x200)
    matrix2 = []
    for i in range(200):
        row = []
        for j in range(200):
            row.append(i * 200 + j)
        matrix2.append(row)

    result2 = solution.longestIncreasingPath(matrix2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum value (2^31 - 1)
    matrix3 = [[2147483647, 1], [1, 2147483647]]
    result3 = solution.longestIncreasingPath(matrix3)
    assert result3 == 2, f"Max value failed: {result3}"
    print(f"Maximum value: ✅")

    # Edge Case 4: Minimum value (0)
    matrix4 = [[0, 0], [0, 0]]
    result4 = solution.longestIncreasingPath(matrix4)
    assert result4 == 1, f"Min value failed: {result4}"
    print(f"Minimum value: ✅")

    # Edge Case 5: All same values
    matrix5 = [[5] * 10 for _ in range(10)]
    result5 = solution.longestIncreasingPath(matrix5)
    assert result5 == 1, f"All same values failed: {result5}"
    print(f"All same values: ✅")

    # Edge Case 6: Single row
    matrix6 = [[1, 2, 3, 4, 5]]
    result6 = solution.longestIncreasingPath(matrix6)
    assert result6 == 5, f"Single row failed: {result6}"
    print(f"Single row: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Longest Increasing Path in a Matrix:")

    # Large dataset
    matrix = []
    for i in range(50):
        row = []
        for j in range(50):
            row.append(i * 50 + j)
        matrix.append(row)

    start_time = time.time()
    result = solution.longestIncreasingPath(matrix)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (50x50 matrix):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Increasing Path in a Matrix Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the longestIncreasingPath method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using DFS with memoization")

"""
Swim in Rising Water - LeetCode Problem 778

You are given an n x n integer matrix grid where each value grid[i][j] represents
the elevation at that point (i, j).
"""

import time
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    grid1 = [[0, 2], [1, 3]]
    result1 = solution.swimInWater(grid1)
    assert result1 == 3, f"Failed for basic case, expected 3, got {result1}"

    # Test Case 2: Complex case
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    result2 = solution.swimInWater(grid2)
    assert result2 == 16, f"Failed for complex case, expected 16, got {result2}"

    # Test Case 3: Single cell
    grid3 = [[0]]
    result3 = solution.swimInWater(grid3)
    assert result3 == 0, f"Failed for single cell, expected 0, got {result3}"

    # Test Case 4: 2x2 grid
    grid4 = [[0, 1], [2, 3]]
    result4 = solution.swimInWater(grid4)
    assert result4 == 2, f"Failed for 2x2 grid, expected 2, got {result4}"

    # Test Case 5: Increasing values
    grid5 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    result5 = solution.swimInWater(grid5)
    assert result5 == 8, f"Failed for increasing values, expected 8, got {result5}"

    # Test Case 6: Decreasing values
    grid6 = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
    result6 = solution.swimInWater(grid6)
    assert result6 == 8, f"Failed for decreasing values, expected 8, got {result6}"

    # Test Case 7: All same values
    grid7 = [[5, 5], [5, 5]]
    result7 = solution.swimInWater(grid7)
    assert result7 == 5, f"Failed for all same values, expected 5, got {result7}"

    # Test Case 8: Mixed values
    grid8 = [[0, 3, 1], [2, 4, 5], [6, 7, 8]]
    result8 = solution.swimInWater(grid8)
    assert result8 == 4, f"Failed for mixed values, expected 4, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 20, 30]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create a grid with increasing values
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i * size + j)
            grid.append(row)

        # Test approach
        start_time = time.time()
        result = solution.swimInWater(grid)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}x{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n^2 * log n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n^2 * log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (test_sizes[i - 1] ** 2) * (
                test_sizes[i - 1].bit_length()
            )
            curr_complexity = (test_sizes[i] ** 2) * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n^2*log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 3.0  # Allow 300% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^2 * log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n^2 * log n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n^2 * log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^2 * log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1x1)
    grid1 = [[0]]
    result1 = solution.swimInWater(grid1)
    assert result1 == 0, f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (50x50)
    grid2 = []
    for i in range(50):
        row = []
        for j in range(50):
            row.append(i * 50 + j)
        grid2.append(row)

    result2 = solution.swimInWater(grid2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum elevation (n^2 - 1)
    grid3 = [[0, 3], [2, 1]]
    result3 = solution.swimInWater(grid3)
    assert result3 == 2, f"Max elevation failed: {result3}"
    print(f"Maximum elevation: ✅")

    # Edge Case 4: Minimum elevation (0)
    grid4 = [[0, 0], [0, 0]]
    result4 = solution.swimInWater(grid4)
    assert result4 == 0, f"Min elevation failed: {result4}"
    print(f"Minimum elevation: ✅")

    # Edge Case 5: All unique values
    grid5 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    result5 = solution.swimInWater(grid5)
    assert result5 == 8, f"All unique values failed: {result5}"
    print(f"All unique values: ✅")

    # Edge Case 6: Single row
    grid6 = [[0, 1, 2, 3, 4]]
    result6 = solution.swimInWater(grid6)
    assert result6 == 4, f"Single row failed: {result6}"
    print(f"Single row: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Swim in Rising Water:")

    # Large dataset
    grid = []
    for i in range(20):
        row = []
        for j in range(20):
            row.append(i * 20 + j)
        grid.append(row)

    start_time = time.time()
    result = solution.swimInWater(grid)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (20x20 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Swim in Rising Water Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the swimInWater method")
        print("- Aim for O(n^2 * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^2 * log n)")
        print("- Consider using binary search with BFS/DFS")

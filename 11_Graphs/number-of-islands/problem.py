"""
Number of Islands - LeetCode Problem 200

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
"""

import time
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    result1 = solution.numIslands(grid1)
    assert result1 == 1, f"Failed for basic case, expected 1, got {result1}"

    # Test Case 2: Multiple islands
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    result2 = solution.numIslands(grid2)
    assert result2 == 3, f"Failed for multiple islands, expected 3, got {result2}"

    # Test Case 3: No islands
    grid3 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]
    result3 = solution.numIslands(grid3)
    assert result3 == 0, f"Failed for no islands, expected 0, got {result3}"

    # Test Case 4: Single cell island
    grid4 = [["1"]]
    result4 = solution.numIslands(grid4)
    assert result4 == 1, f"Failed for single cell, expected 1, got {result4}"

    # Test Case 5: All land
    grid5 = [
        ["1", "1"],
        ["1", "1"],
    ]
    result5 = solution.numIslands(grid5)
    assert result5 == 1, f"Failed for all land, expected 1, got {result5}"

    # Test Case 6: Linear island
    grid6 = [["1", "1", "1", "0", "0"]]
    result6 = solution.numIslands(grid6)
    assert result6 == 1, f"Failed for linear island, expected 1, got {result6}"

    # Test Case 7: L-shaped island
    grid7 = [
        ["1", "0"],
        ["1", "1"],
    ]
    result7 = solution.numIslands(grid7)
    assert result7 == 1, f"Failed for L-shaped island, expected 1, got {result7}"

    # Test Case 8: Complex shape
    grid8 = [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1"],
        ["0", "0", "0", "1", "1"],
    ]
    result8 = solution.numIslands(grid8)
    assert result8 == 2, f"Failed for complex shape, expected 2, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - checkerboard pattern
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append("1" if (i + j) % 2 == 0 else "0")
            grid.append(row)

        # Test approach
        start_time = time.time()
        result = solution.numIslands(grid)
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
            prev_complexity = test_sizes[i - 1] ** 2
            curr_complexity = test_sizes[i] ** 2
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
    grid1 = [["1"]]
    result1 = solution.numIslands(grid1)
    assert result1 == 1, f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (300x300)
    grid2 = []
    for i in range(300):
        row = []
        for j in range(300):
            row.append("1" if (i + j) % 2 == 0 else "0")
        grid2.append(row)

    result2 = solution.numIslands(grid2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All zeros
    grid3 = [["0"] * 10 for _ in range(10)]
    result3 = solution.numIslands(grid3)
    assert result3 == 0, f"All zeros failed: {result3}"
    print(f"All zeros: ✅")

    # Edge Case 4: All ones
    grid4 = [["1"] * 10 for _ in range(10)]
    result4 = solution.numIslands(grid4)
    assert result4 == 1, f"All ones failed: {result4}"
    print(f"All ones: ✅")

    # Edge Case 5: Single row
    grid5 = [["1", "0", "1", "1", "0"]]
    result5 = solution.numIslands(grid5)
    assert result5 == 2, f"Single row failed: {result5}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    grid6 = [["1"], ["0"], ["1"], ["1"]]
    result6 = solution.numIslands(grid6)
    assert result6 == 2, f"Single column failed: {result6}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Number of Islands:")

    # Large dataset
    grid = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append("1" if (i + j) % 3 == 0 else "0")
        grid.append(row)

    start_time = time.time()
    result = solution.numIslands(grid)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100x100 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Number of Islands Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the numIslands method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using DFS or BFS to explore islands")

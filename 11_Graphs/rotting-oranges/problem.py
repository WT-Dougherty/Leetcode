"""
Rotting Oranges - LeetCode Problem 994

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
"""

import time
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time_array = [
            [0 if grid[row][col] == 0 else -1 for col in range(len(grid[0]))]
            for row in range(len(grid))
        ]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    self.BFS(grid, time_array, (row, col))

        min_time = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if time_array[row][col] == -1:
                    return -1
                min_time = max(min_time, time_array[row][col])
        return min_time

    def BFS(
        self, grid: List[List[int]], time_array: List[List[int]], coord: tuple
    ) -> None:
        def Advance(c: tuple, proj_time: int) -> bool:
            if (
                c[0] >= 0
                and c[0] < len(grid)
                and c[1] >= 0
                and c[1] < len(grid[0])
                and grid[c[0]][c[1]] == 1
                and (time_array[c[0]][c[1]] == -1 or time_array[c[0]][c[1]] > proj_time)
            ):
                return True
            else:
                return False

        q = deque()
        q.appendleft((coord, 0))
        while True:
            if len(q) == 0:
                break

            pckg = q.pop()
            cur_coord = pckg[0]
            cur_time = pckg[1]

            time_array[cur_coord[0]][cur_coord[1]] = cur_time
            neighbors = [
                (cur_coord[0] - 1, cur_coord[1]),
                (cur_coord[0] + 1, cur_coord[1]),
                (cur_coord[0], cur_coord[1] - 1),
                (cur_coord[0], cur_coord[1] + 1),
            ]
            for n in neighbors:
                if Advance(n, cur_time + 1):
                    q.appendleft((n, cur_time + 1))


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result1 = solution.orangesRotting(grid1)
    assert result1 == 4, f"Failed for basic case, expected 4, got {result1}"

    # Test Case 2: Impossible case
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    result2 = solution.orangesRotting(grid2)
    assert result2 == -1, f"Failed for impossible case, expected -1, got {result2}"

    # Test Case 3: Already done
    grid3 = [[0, 2]]
    result3 = solution.orangesRotting(grid3)
    assert result3 == 0, f"Failed for already done, expected 0, got {result3}"

    # Test Case 4: No fresh oranges
    grid4 = [[0]]
    result4 = solution.orangesRotting(grid4)
    assert result4 == 0, f"Failed for no fresh oranges, expected 0, got {result4}"

    # Test Case 5: Single fresh orange
    grid5 = [[1]]
    result5 = solution.orangesRotting(grid5)
    assert result5 == -1, f"Failed for single fresh orange, expected -1, got {result5}"

    # Test Case 6: Single rotten orange
    grid6 = [[2]]
    result6 = solution.orangesRotting(grid6)
    assert result6 == 0, f"Failed for single rotten orange, expected 0, got {result6}"

    # Test Case 7: Multiple rotten oranges
    grid7 = [[2, 2], [1, 1], [0, 1]]
    result7 = solution.orangesRotting(grid7)
    assert (
        result7 == 2
    ), f"Failed for multiple rotten oranges, expected 2, got {result7}"

    # Test Case 8: Complex case
    grid8 = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
    result8 = solution.orangesRotting(grid8)
    assert result8 == 2, f"Failed for complex case, expected 2, got {result8}"

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
        # Generate test data - checkerboard pattern
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == 0 and j == 0:
                    row.append(2)  # Start with rotten orange
                elif (i + j) % 2 == 0:
                    row.append(1)  # Fresh orange
                else:
                    row.append(0)  # Empty
            grid.append(row)

        # Test approach
        start_time = time.time()
        result = solution.orangesRotting(grid)
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
    grid1 = [[1]]
    result1 = solution.orangesRotting(grid1)
    assert result1 == -1, f"Single fresh orange failed: {result1}"
    print(f"Single fresh orange: ✅")

    # Edge Case 2: Maximum constraint (10x10)
    grid2 = []
    for i in range(10):
        row = []
        for j in range(10):
            if i == 0 and j == 0:
                row.append(2)
            elif (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        grid2.append(row)

    result2 = solution.orangesRotting(grid2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All empty
    grid3 = [[0] * 5 for _ in range(5)]
    result3 = solution.orangesRotting(grid3)
    assert result3 == 0, f"All empty failed: {result3}"
    print(f"All empty: ✅")

    # Edge Case 4: All rotten
    grid4 = [[2] * 5 for _ in range(5)]
    result4 = solution.orangesRotting(grid4)
    assert result4 == 0, f"All rotten failed: {result4}"
    print(f"All rotten: ✅")

    # Edge Case 5: Single row
    grid5 = [[2, 1, 1, 0]]
    result5 = solution.orangesRotting(grid5)
    assert result5 == 2, f"Single row failed: {result5}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    grid6 = [[2], [1], [1], [0]]
    result6 = solution.orangesRotting(grid6)
    assert result6 == 2, f"Single column failed: {result6}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Rotting Oranges:")

    # Large dataset
    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            if i == 0 and j == 0:
                row.append(2)
            elif (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    start_time = time.time()
    result = solution.orangesRotting(grid)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10x10 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Rotting Oranges Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the orangesRotting method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using BFS with multiple starting points")

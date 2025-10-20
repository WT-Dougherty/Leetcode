"""
Max Area of Island - LeetCode Problem 695

You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical). You may assume all four edges of the
grid are surrounded by water.
"""

import time
from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                else:
                    max_area = max(self.DFS(grid, (i, j), 0), max_area)
        return max_area

    def BFS(self, grid: List[List[str]], coord: tuple) -> int:
        q = deque()
        q.appendleft(coord)
        grid[coord[0]][coord[1]] = 0
        count = 1
        while True:
            if len(q) == 0:
                break

            cur_node = q.pop()
            neighbors = [
                (cur_node[0] - 1, cur_node[1]),
                (cur_node[0] + 1, cur_node[1]),
                (cur_node[0], cur_node[1] - 1),
                (cur_node[0], cur_node[1] + 1),
            ]

            for n in neighbors:
                # check in range and equal to 1
                if (
                    n[0] < 0
                    or n[0] >= len(grid)
                    or n[1] < 0
                    or n[1] >= len(grid[0])
                    or grid[n[0]][n[1]] == 0
                ):
                    continue
                q.appendleft(n)
                grid[n[0]][n[1]] = 0
                count += 1
        return count

    def DFS(self, grid: List[List[str]], coord: tuple, count: int) -> int:
        def ValidNeighbor(n: tuple) -> bool:
            if (
                n[0] < 0
                or n[0] >= len(grid)
                or n[1] < 0
                or n[1] >= len(grid[0])
                or grid[n[0]][n[1]] == 0
            ):
                return False
            return True

        grid[coord[0]][coord[1]] = 0
        count += 1

        neighbors = [
            (coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1),
        ]
        for n in neighbors:
            if ValidNeighbor(n):
                count = self.DFS(grid, n, count)
        return count


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    result1 = solution.maxAreaOfIsland(grid1)
    assert result1 == 6, f"Failed for basic case, expected 6, got {result1}"

    # Test Case 2: No islands
    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    result2 = solution.maxAreaOfIsland(grid2)
    assert result2 == 0, f"Failed for no islands, expected 0, got {result2}"

    # Test Case 3: Single cell island
    grid3 = [[1]]
    result3 = solution.maxAreaOfIsland(grid3)
    assert result3 == 1, f"Failed for single cell, expected 1, got {result3}"

    # Test Case 4: All land
    grid4 = [[1, 1], [1, 1]]
    result4 = solution.maxAreaOfIsland(grid4)
    assert result4 == 4, f"Failed for all land, expected 4, got {result4}"

    # Test Case 5: Multiple islands
    grid5 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    result5 = solution.maxAreaOfIsland(grid5)
    assert result5 == 4, f"Failed for multiple islands, expected 4, got {result5}"

    # Test Case 6: Linear island
    grid6 = [[1, 1, 1, 0, 0]]
    result6 = solution.maxAreaOfIsland(grid6)
    assert result6 == 3, f"Failed for linear island, expected 3, got {result6}"

    # Test Case 7: L-shaped island
    grid7 = [[1, 0], [1, 1]]
    result7 = solution.maxAreaOfIsland(grid7)
    assert result7 == 3, f"Failed for L-shaped island, expected 3, got {result7}"

    # Test Case 8: Complex shape
    grid8 = [
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    result8 = solution.maxAreaOfIsland(grid8)
    assert result8 == 4, f"Failed for complex shape, expected 4, got {result8}"

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
                row.append((i + j) % 2)
            grid.append(row)

        # Test approach
        start_time = time.time()
        result = solution.maxAreaOfIsland(grid)
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
    result1 = solution.maxAreaOfIsland(grid1)
    assert result1 == 1, f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (50x50)
    grid2 = []
    for i in range(50):
        row = []
        for j in range(50):
            row.append(1 if (i + j) % 2 == 0 else 0)
        grid2.append(row)

    result2 = solution.maxAreaOfIsland(grid2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All zeros
    grid3 = [[0] * 10 for _ in range(10)]
    result3 = solution.maxAreaOfIsland(grid3)
    assert result3 == 0, f"All zeros failed: {result3}"
    print(f"All zeros: ✅")

    # Edge Case 4: All ones
    grid4 = [[1] * 10 for _ in range(10)]
    result4 = solution.maxAreaOfIsland(grid4)
    assert result4 == 100, f"All ones failed: {result4}"
    print(f"All ones: ✅")

    # Edge Case 5: Single row
    grid5 = [[1, 0, 1, 1, 0]]
    result5 = solution.maxAreaOfIsland(grid5)
    assert result5 == 2, f"Single row failed: {result5}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    grid6 = [[1], [0], [1], [1]]
    result6 = solution.maxAreaOfIsland(grid6)
    assert result6 == 2, f"Single column failed: {result6}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Max Area of Island:")

    # Large dataset
    grid = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append(1 if (i + j) % 3 == 0 else 0)
        grid.append(row)

    start_time = time.time()
    result = solution.maxAreaOfIsland(grid)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100x100 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Max Area of Island Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxAreaOfIsland method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using DFS or BFS to explore islands")

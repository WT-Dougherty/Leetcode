"""
Pacific Atlantic Water Flow - LeetCode Problem 417

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches
the island's right and bottom edges.
"""

import time
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def BFS(seen: set, q: deque):
            while q:
                cur = q.pop()
                neighbors = [
                    (cur[0] - 1, cur[1]),
                    (cur[0] + 1, cur[1]),
                    (cur[0], cur[1] - 1),
                    (cur[0], cur[1] + 1),
                ]
                for n in neighbors:
                    if (
                        n not in seen
                        and 0 <= n[0] < len(heights)
                        and 0 <= n[1] < len(heights[0])
                        and heights[n[0]][n[1]] >= heights[cur[0]][cur[1]]
                    ):
                        q.appendleft(n)
                        seen.add(n)

        pacific_coords = set()
        atlantic_coords = set()
        q = deque()

        # find valid pacific coords
        for row in range(len(heights)):
            q.appendleft((row, 0))
            pacific_coords.add((row, 0))
        for col in range(1, len(heights[0])):
            q.appendleft((0, col))
            pacific_coords.add((0, col))
        BFS(pacific_coords, q)

        # find valid atlantic coords
        for row in range(len(heights)):
            q.appendleft((row, len(heights[0]) - 1))
            atlantic_coords.add((row, len(heights[0]) - 1))
        for col in range(len(heights[0]) - 1):
            q.appendleft((len(heights) - 1, col))
            atlantic_coords.add((len(heights) - 1, col))
        BFS(atlantic_coords, q)

        return list(
            list(coord) for coord in pacific_coords.intersection(atlantic_coords)
        )


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    result1 = solution.pacificAtlantic(heights1)
    expected1 = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    # Sort both for comparison
    result1_sorted = sorted(result1)
    expected1_sorted = sorted(expected1)
    assert (
        result1_sorted == expected1_sorted
    ), f"Failed for basic case, expected {expected1_sorted}, got {result1_sorted}"

    # Test Case 2: Simple case
    heights2 = [[2, 1], [1, 2]]
    result2 = solution.pacificAtlantic(heights2)
    expected2 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    result2_sorted = sorted(result2)
    expected2_sorted = sorted(expected2)
    assert (
        result2_sorted == expected2_sorted
    ), f"Failed for simple case, expected {expected2_sorted}, got {result2_sorted}"

    # Test Case 3: Single cell
    heights3 = [[1]]
    result3 = solution.pacificAtlantic(heights3)
    expected3 = [[0, 0]]
    assert (
        result3 == expected3
    ), f"Failed for single cell, expected {expected3}, got {result3}"

    # Test Case 4: Single row
    heights4 = [[1, 2, 3, 4, 5]]
    result4 = solution.pacificAtlantic(heights4)
    expected4 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
    result4_sorted = sorted(result4)
    expected4_sorted = sorted(expected4)
    assert (
        result4_sorted == expected4_sorted
    ), f"Failed for single row, expected {expected4_sorted}, got {result4_sorted}"

    # Test Case 5: Single column
    heights5 = [[1], [2], [3], [4], [5]]
    result5 = solution.pacificAtlantic(heights5)
    expected5 = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
    result5_sorted = sorted(result5)
    expected5_sorted = sorted(expected5)
    assert (
        result5_sorted == expected5_sorted
    ), f"Failed for single column, expected {expected5_sorted}, got {result5_sorted}"

    # Test Case 6: Decreasing heights
    heights6 = [[1, 1], [1, 1], [1, 1]]
    result6 = solution.pacificAtlantic(heights6)
    expected6 = [[0, 1], [2, 1], [0, 0], [1, 1], [2, 0], [1, 0]]
    result6_sorted = sorted(result6)
    expected6_sorted = sorted(expected6)
    assert (
        result6_sorted == expected6_sorted
    ), f"Failed for decreasing heights, expected {expected6_sorted}, got {result6_sorted}"

    # Test Case 7: Increasing heights
    heights7 = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ]
    result7 = solution.pacificAtlantic(heights7)
    expected7 = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]
    result7_sorted = sorted(result7)
    expected7_sorted = sorted(expected7)
    assert (
        result7_sorted == expected7_sorted
    ), f"Failed for increasing heights, expected {expected7_sorted}, got {result7_sorted}"

    # Test Case 8: Complex case
    heights8 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    result8 = solution.pacificAtlantic(heights8)
    expected8 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    result8_sorted = sorted(result8)
    expected8_sorted = sorted(expected8)
    assert (
        result8_sorted == expected8_sorted
    ), f"Failed for complex case, expected {expected8_sorted}, got {result8_sorted}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 150]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - increasing pattern
        heights = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i + j)
            heights.append(row)

        # Test approach
        start_time = time.time()
        result = solution.pacificAtlantic(heights)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}x{size}\t{elapsed_time:.6f}s\t{len(result)} cells")

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
    heights1 = [[1]]
    result1 = solution.pacificAtlantic(heights1)
    assert result1 == [[0, 0]], f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (200x200)
    heights2 = []
    for i in range(200):
        row = []
        for j in range(200):
            row.append(i + j)
        heights2.append(row)

    result2 = solution.pacificAtlantic(heights2)
    assert isinstance(result2, list), f"Max constraint failed: {type(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum height values
    heights3 = [[10**5, 10**5], [10**5, 10**5]]
    result3 = solution.pacificAtlantic(heights3)
    expected3 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    result3_sorted = sorted(result3)
    expected3_sorted = sorted(expected3)
    assert (
        result3_sorted == expected3_sorted
    ), f"Max height values failed: {result3_sorted}"
    print(f"Maximum height values: ✅")

    # Edge Case 4: Minimum height values
    heights4 = [[0, 0], [0, 0]]
    result4 = solution.pacificAtlantic(heights4)
    expected4 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    result4_sorted = sorted(result4)
    expected4_sorted = sorted(expected4)
    assert (
        result4_sorted == expected4_sorted
    ), f"Min height values failed: {result4_sorted}"
    print(f"Minimum height values: ✅")

    # Edge Case 5: Single row
    heights5 = [[1, 2, 3, 4, 5]]
    result5 = solution.pacificAtlantic(heights5)
    assert len(result5) == 5, f"Single row failed: {len(result5)}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    heights6 = [[1], [2], [3], [4], [5]]
    result6 = solution.pacificAtlantic(heights6)
    assert len(result6) == 5, f"Single column failed: {len(result6)}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Pacific Atlantic Water Flow:")

    # Large dataset
    heights = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append(i + j)
        heights.append(row)

    start_time = time.time()
    result = solution.pacificAtlantic(heights)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100x100 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} cells")


if __name__ == "__main__":
    print("🧪 Testing Pacific Atlantic Water Flow Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the pacificAtlantic method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using DFS from ocean boundaries")

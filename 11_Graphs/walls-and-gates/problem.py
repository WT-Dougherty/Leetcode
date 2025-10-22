"""
Walls and Gates - LeetCode Problem 286

You are given an m x n grid rooms initialized with these three possible values:
- -1 A wall or an obstacle.
- 0 A gate.
- INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF.
"""

import time
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        WALL, GATE = -1, 0

        def BFS(coord: tuple) -> None:
            q = deque()
            seen = set()

            q.appendleft((0, coord))
            seen.add(coord)

            while q:
                d, cur = q.pop()
                rooms[cur[0]][cur[1]] = min(rooms[cur[0]][cur[1]], d)

                neighbors = [
                    (cur[0] - 1, cur[1]),
                    (cur[0] + 1, cur[1]),
                    (cur[0], cur[1] - 1),
                    (cur[0], cur[1] + 1),
                ]
                for nei in neighbors:
                    if 0 <= nei[0] < len(rooms) and 0 <= nei[1] < len(rooms[0]):
                        if (
                            nei in seen
                            or rooms[nei[0]][nei[1]] == WALL
                            or rooms[nei[0]][nei[1]] == GATE
                        ):
                            continue
                        else:
                            q.appendleft((d + 1, nei))
                            seen.add(nei)

        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == GATE:
                    BFS((row, col))


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    rooms1 = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    expected1 = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
    solution.wallsAndGates(rooms1)
    assert (
        rooms1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {rooms1}"

    # Test Case 2: Single gate
    rooms2 = [[2147483647, -1, 0, 2147483647]]
    expected2 = [[2147483647, -1, 0, 1]]
    solution.wallsAndGates(rooms2)
    assert (
        rooms2 == expected2
    ), f"Failed for single gate, expected {expected2}, got {rooms2}"

    # Test Case 3: No gates
    rooms3 = [[2147483647, -1, 2147483647]]
    expected3 = [[2147483647, -1, 2147483647]]
    solution.wallsAndGates(rooms3)
    assert (
        rooms3 == expected3
    ), f"Failed for no gates, expected {expected3}, got {rooms3}"

    # Test Case 4: All walls
    rooms4 = [[-1, -1], [-1, -1]]
    expected4 = [[-1, -1], [-1, -1]]
    solution.wallsAndGates(rooms4)
    assert (
        rooms4 == expected4
    ), f"Failed for all walls, expected {expected4}, got {rooms4}"

    # Test Case 5: Single room
    rooms5 = [[0]]
    expected5 = [[0]]
    solution.wallsAndGates(rooms5)
    assert (
        rooms5 == expected5
    ), f"Failed for single room, expected {expected5}, got {rooms5}"

    # Test Case 6: Multiple gates
    rooms6 = [
        [0, 2147483647],
        [2147483647, 0],
    ]
    expected6 = [
        [0, 1],
        [1, 0],
    ]
    solution.wallsAndGates(rooms6)
    assert (
        rooms6 == expected6
    ), f"Failed for multiple gates, expected {expected6}, got {rooms6}"

    # Test Case 7: Complex case
    rooms7 = [
        [2147483647, 0, 2147483647, 2147483647, 0, 2147483647, -1, 2147483647],
    ]
    expected7 = [
        [1, 0, 1, 1, 0, 1, -1, 2147483647],
    ]
    solution.wallsAndGates(rooms7)
    assert (
        rooms7 == expected7
    ), f"Failed for complex case, expected {expected7}, got {rooms7}"

    # Test Case 8: Single row
    rooms8 = [[0, 2147483647, 2147483647, -1, 0]]
    expected8 = [[0, 1, 2, -1, 0]]
    solution.wallsAndGates(rooms8)
    assert (
        rooms8 == expected8
    ), f"Failed for single row, expected {expected8}, got {rooms8}"

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
        # Generate test data - grid with gates
        rooms = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == 0 and j == 0:
                    row.append(0)  # Gate at top-left
                elif (i + j) % 10 == 0:
                    row.append(-1)  # Wall
                else:
                    row.append(2147483647)  # Empty room
            rooms.append(row)

        # Test approach
        start_time = time.time()
        solution.wallsAndGates(rooms)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}x{size}\t{elapsed_time:.6f}s\tModified")

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
    rooms1 = [[0]]
    solution.wallsAndGates(rooms1)
    assert rooms1 == [[0]], f"Single gate failed: {rooms1}"
    print(f"Single gate: ✅")

    # Edge Case 2: Maximum constraint (250x250)
    rooms2 = []
    for i in range(250):
        row = []
        for j in range(250):
            if i == 0 and j == 0:
                row.append(0)
            elif (i + j) % 10 == 0:
                row.append(-1)
            else:
                row.append(2147483647)
        rooms2.append(row)

    solution.wallsAndGates(rooms2)
    assert isinstance(rooms2, list), f"Max constraint failed: {type(rooms2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All walls
    rooms3 = [[-1] * 10 for _ in range(10)]
    solution.wallsAndGates(rooms3)
    assert all(cell == -1 for row in rooms3 for cell in row), f"All walls failed"
    print(f"All walls: ✅")

    # Edge Case 4: All gates
    rooms4 = [[0] * 10 for _ in range(10)]
    solution.wallsAndGates(rooms4)
    assert all(cell == 0 for row in rooms4 for cell in row), f"All gates failed"
    print(f"All gates: ✅")

    # Edge Case 5: Single row
    rooms5 = [[0, 2147483647, 2147483647, -1, 0]]
    solution.wallsAndGates(rooms5)
    assert rooms5 == [[0, 1, 2, -1, 0]], f"Single row failed: {rooms5}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    rooms6 = [[0], [2147483647], [2147483647], [-1], [0]]
    solution.wallsAndGates(rooms6)
    assert rooms6 == [[0], [1], [2], [-1], [0]], f"Single column failed: {rooms6}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Walls and Gates:")

    # Large dataset
    rooms = []
    for i in range(100):
        row = []
        for j in range(100):
            if i == 0 and j == 0:
                row.append(0)
            elif (i + j) % 10 == 0:
                row.append(-1)
            else:
                row.append(2147483647)
        rooms.append(row)

    start_time = time.time()
    solution.wallsAndGates(rooms)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100x100 grid):")
    print(f"Time: {elapsed_time:.6f}s, Result: Modified")


if __name__ == "__main__":
    print("🧪 Testing Walls and Gates Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the wallsAndGates method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using BFS from all gates simultaneously")

"""
Surrounded Regions - LeetCode Problem 130

Given an m x n matrix board containing 'X' and 'O', capture all regions that are
4-directionally surrounded by 'X'.
"""

import time
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        DEAD, BORDER, UNVISITED = 0, 1, 2
        states: List[List[str]] = [
            [BORDER if mark == "X" else UNVISITED for mark in row] for row in board
        ]
        for i in range(len(states[0])):
            if states[0][i] == UNVISITED:
                states[0][i] = DEAD
            if states[len(states) - 1][i] == UNVISITED:
                states[len(states) - 1][i] = DEAD
        for i in range(len(states)):
            if states[i][0] == UNVISITED:
                states[i][0] = DEAD
            if states[i][len(states[0]) - 1] == UNVISITED:
                states[i][len(states[0]) - 1] = DEAD

        def BFS(coord: tuple) -> bool:
            q = deque()
            q.appendleft(coord)
            seen.add(coord)

            while q:
                cur = q.pop()
                neighbors = [
                    (cur[0] - 1, cur[1]),
                    (cur[0] + 1, cur[1]),
                    (cur[0], cur[1] - 1),
                    (cur[0], cur[1] + 1),
                ]
                for nei in neighbors:
                    if nei in seen:
                        continue
                    if 0 <= nei[0] < len(board) and 0 <= nei[1] < len(board[0]):
                        if states[nei[0]][nei[1]] == DEAD:
                            return False
                        elif states[nei[0]][nei[1]] == BORDER:
                            continue
                        else:
                            q.appendleft(nei)
                            seen.add(nei)
                    else:
                        return False
            return True

        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if states[row][col] == UNVISITED:
                    if BFS((row, col)):
                        for r, c in seen:
                            states[r][c] = BORDER
                            board[r][c] = "X"
                    else:
                        for r, c in seen:
                            states[r][c] = DEAD
                    seen.clear()


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    solution.solve(board1)
    assert (
        board1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {board1}"

    # Test Case 2: Single cell
    board2 = [["X"]]
    expected2 = [["X"]]
    solution.solve(board2)
    assert (
        board2 == expected2
    ), f"Failed for single cell, expected {expected2}, got {board2}"

    # Test Case 3: All X's
    board3 = [["X", "X"], ["X", "X"]]
    expected3 = [["X", "X"], ["X", "X"]]
    solution.solve(board3)
    assert (
        board3 == expected3
    ), f"Failed for all X's, expected {expected3}, got {board3}"

    # Test Case 4: All O's
    board4 = [["O", "O"], ["O", "O"]]
    expected4 = [["O", "O"], ["O", "O"]]
    solution.solve(board4)
    assert (
        board4 == expected4
    ), f"Failed for all O's, expected {expected4}, got {board4}"

    # Test Case 5: No surrounded regions
    board5 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"],
    ]
    expected5 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"],
    ]
    solution.solve(board5)
    assert (
        board5 == expected5
    ), f"Failed for no surrounded regions, expected {expected5}, got {board5}"

    # Test Case 6: Single row
    board6 = [["X", "O", "X", "O", "X"]]
    expected6 = [["X", "O", "X", "O", "X"]]
    solution.solve(board6)
    assert (
        board6 == expected6
    ), f"Failed for single row, expected {expected6}, got {board6}"

    # Test Case 7: Single column
    board7 = [["X"], ["O"], ["X"], ["O"], ["X"]]
    expected7 = [["X"], ["O"], ["X"], ["O"], ["X"]]
    solution.solve(board7)
    assert (
        board7 == expected7
    ), f"Failed for single column, expected {expected7}, got {board7}"

    # Test Case 8: Complex case
    board8 = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
    expected8 = [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
    solution.solve(board8)
    assert (
        board8 == expected8
    ), f"Failed for complex case, expected {expected8}, got {board8}"

    # Test Case 9: Complex case
    board9 = [
        ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
        ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
        ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
        ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
        ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
        ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
    ]
    expected9 = [
        ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
        ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
        ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"],
        ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
    ]
    solution.solve(board9)
    assert (
        board9 == expected9
    ), f"Failed for complex case, expected {expected9}, got {board9}"

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
        # Generate test data - checkerboard pattern
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                if (i + j) % 2 == 0:
                    row.append("X")
                else:
                    row.append("O")
            board.append(row)

        # Test approach
        start_time = time.time()
        solution.solve(board)
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
    board1 = [["O"]]
    solution.solve(board1)
    assert board1 == [["O"]], f"Single O failed: {board1}"
    print(f"Single O: ✅")

    # Edge Case 2: Maximum constraint (200x200)
    board2 = []
    for i in range(200):
        row = []
        for j in range(200):
            if (i + j) % 2 == 0:
                row.append("X")
            else:
                row.append("O")
        board2.append(row)

    solution.solve(board2)
    assert isinstance(board2, list), f"Max constraint failed: {type(board2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All X's
    board3 = [["X"] * 10 for _ in range(10)]
    solution.solve(board3)
    assert all(cell == "X" for row in board3 for cell in row), f"All X's failed"
    print(f"All X's: ✅")

    # Edge Case 4: All O's
    board4 = [["O"] * 10 for _ in range(10)]
    solution.solve(board4)
    assert all(cell == "O" for row in board4 for cell in row), f"All O's failed"
    print(f"All O's: ✅")

    # Edge Case 5: Single row
    board5 = [["X", "O", "X", "O", "X"]]
    solution.solve(board5)
    assert board5 == [["X", "O", "X", "O", "X"]], f"Single row failed: {board5}"
    print(f"Single row: ✅")

    # Edge Case 6: Single column
    board6 = [["X"], ["O"], ["X"], ["O"], ["X"]]
    solution.solve(board6)
    assert board6 == [
        ["X"],
        ["O"],
        ["X"],
        ["O"],
        ["X"],
    ], f"Single column failed: {board6}"
    print(f"Single column: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Surrounded Regions:")

    # Large dataset
    board = []
    for i in range(100):
        row = []
        for j in range(100):
            if (i + j) % 2 == 0:
                row.append("X")
            else:
                row.append("O")
        board.append(row)

    start_time = time.time()
    solution.solve(board)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100x100 board):")
    print(f"Time: {elapsed_time:.6f}s, Result: Modified")


if __name__ == "__main__":
    print("🧪 Testing Surrounded Regions Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the solve method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using DFS from border O's")

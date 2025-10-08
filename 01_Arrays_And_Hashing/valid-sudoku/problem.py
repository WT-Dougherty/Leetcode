"""
Valid Sudoku - LeetCode Problem 36

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

import time
import random
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Valid board
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(board1) == True, f"Failed for valid board"

    # Test Case 2: Invalid board (duplicate in row)
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert (
        solution.isValidSudoku(board2) == False
    ), f"Failed for invalid board (duplicate in row)"

    # Test Case 3: Empty board
    board3 = [["."] * 9 for _ in range(9)]
    assert solution.isValidSudoku(board3) == True, f"Failed for empty board"

    # Test Case 4: Duplicate in column
    board4 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ["5", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert (
        solution.isValidSudoku(board4) == False
    ), f"Failed for invalid board (duplicate in column)"

    # Test Case 5: Duplicate in 3x3 box
    board5 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board5[0][0] = "6"  # Create duplicate in first 3x3 box
    assert (
        solution.isValidSudoku(board5) == False
    ), f"Failed for invalid board (duplicate in 3x3 box)"

    # Test Case 6: Single cell filled
    board6 = [["."] * 9 for _ in range(9)]
    board6[0][0] = "1"
    assert solution.isValidSudoku(board6) == True, f"Failed for single cell"

    # Test Case 7: Invalid character
    board7 = [["."] * 9 for _ in range(9)]
    board7[0][0] = "0"  # Invalid character
    assert solution.isValidSudoku(board7) == False, f"Failed for invalid character"

    # Test Case 8: Almost complete valid board
    board8 = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    assert (
        solution.isValidSudoku(board8) == True
    ), f"Failed for almost complete valid board"

    # Test Case 9: Invalid in middle 3x3 box
    board9 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board9[4][4] = "6"  # Create duplicate in middle 3x3 box
    assert solution.isValidSudoku(board9) == False, f"Failed for invalid middle 3x3 box"

    # Test Case 10: Edge case with multiple issues
    board10 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(board10) == False, f"Failed for multiple issues"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different board complexities - FAILS if too slow for 9x9"""
    solution = Solution()

    # Test different board complexities
    test_cases = ["empty", "sparse", "dense"]
    times = []

    print("\nTime Complexity Analysis:")
    print("Board Type\tTime\t\tResult")
    print("-" * 50)

    for board_type in test_cases:
        # Generate test board
        board = [["."] * 9 for _ in range(9)]

        if board_type == "empty":
            # Empty board
            pass
        elif board_type == "sparse":
            # Sparse board (few filled cells)
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    board[i][j] = str((i + j) % 9 + 1)
        else:  # dense
            # Dense board (many filled cells)
            for i in range(9):
                for j in range(9):
                    if (i + j) % 2 == 0:
                        board[i][j] = str((i + j) % 9 + 1)

        # Test approach
        start_time = time.time()
        result = solution.isValidSudoku(board)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{board_type}\t{elapsed_time:.6f}s\t{result}")

    # For Sudoku, we expect O(1) since board size is fixed (9x9)
    # But we can still check for reasonable performance
    max_time = max(times)
    if max_time > 0.01:  # More than 10ms for 9x9 board
        print(f"\n❌ FAILED: Performance too slow for fixed-size board")
        print(f"   Maximum time: {max_time:.6f}s (should be < 0.01s)")
        raise AssertionError(f"Time complexity test failed: too slow for 9x9 board")

    print(f"\n✅ PASSED: Performance acceptable for O(1) 9x9 board")
    return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: All empty
    board = [["."] * 9 for _ in range(9)]
    result = solution.isValidSudoku(board)
    print(f"All empty: {result} ✅")

    # Edge Case 2: All filled valid
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    result = solution.isValidSudoku(board)
    print(f"All filled valid: {result} ✅")

    # Edge Case 3: Single row filled
    board = [["."] * 9 for _ in range(9)]
    board[0] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = solution.isValidSudoku(board)
    print(f"Single row filled: {result} ✅")

    # Edge Case 4: Single column filled
    board = [["."] * 9 for _ in range(9)]
    for i in range(9):
        board[i][0] = str(i + 1)
    result = solution.isValidSudoku(board)
    print(f"Single column filled: {result} ✅")

    # Edge Case 5: Single 3x3 box filled
    board = [["."] * 9 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            board[i][j] = str(i * 3 + j + 1)
    result = solution.isValidSudoku(board)
    print(f"Single 3x3 box filled: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with multiple boards"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Test with multiple boards
    boards = []

    # Generate 1000 random boards
    for _ in range(1000):
        board = [["."] * 9 for _ in range(9)]
        # Fill some random cells
        for _ in range(random.randint(10, 30)):
            i, j = random.randint(0, 8), random.randint(0, 8)
            board[i][j] = str(random.randint(1, 9))
        boards.append(board)

    start_time = time.time()
    results = []
    for board in boards:
        result = solution.isValidSudoku(board)
        results.append(result)
    time1 = time.time() - start_time

    print(f"Multiple boards (1000 boards):")
    print(f"Time: {time1:.6f}s, Valid: {sum(results)}/{len(results)}")


if __name__ == "__main__":
    print("🧪 Testing Valid Sudoku Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isValidSudoku method")
        print("- Aim for O(1) time complexity (fixed 9x9 board)")
        print("- Handle all edge cases correctly")
        print("- Check rows, columns, and 3x3 boxes")
    else:
        print("\n❌ Tests failed - improve your solution's performance!")
        print("- Your solution appears to be too slow")
        print("- Consider using sets or arrays for tracking")

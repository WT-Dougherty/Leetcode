"""
Word Search - LeetCode Problem 79

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

import time
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    result1 = solution.exist(board1, word1)
    assert result1 == True, f"Failed for 'ABCCED', expected True, got {result1}"

    # Test Case 2: Another word
    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"
    result2 = solution.exist(board2, word2)
    assert result2 == True, f"Failed for 'SEE', expected True, got {result2}"

    # Test Case 3: Word not found
    board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCB"
    result3 = solution.exist(board3, word3)
    assert result3 == False, f"Failed for 'ABCB', expected False, got {result3}"

    # Test Case 4: Single character
    board4 = [["A", "B"], ["C", "D"]]
    word4 = "A"
    result4 = solution.exist(board4, word4)
    assert result4 == True, f"Failed for 'A', expected True, got {result4}"

    # Test Case 5: Single character not found
    board5 = [["A", "B"], ["C", "D"]]
    word5 = "E"
    result5 = solution.exist(board5, word5)
    assert result5 == False, f"Failed for 'E', expected False, got {result5}"

    # Test Case 6: Empty word
    board6 = [["A", "B"], ["C", "D"]]
    word6 = ""
    result6 = solution.exist(board6, word6)
    assert result6 == True, f"Failed for empty word, expected True, got {result6}"

    # Test Case 7: Single cell board
    board7 = [["A"]]
    word7 = "A"
    result7 = solution.exist(board7, word7)
    assert result7 == True, f"Failed for single cell 'A', expected True, got {result7}"

    # Test Case 8: Single cell board, word not found
    board8 = [["A"]]
    word8 = "B"
    result8 = solution.exist(board8, word8)
    assert (
        result8 == False
    ), f"Failed for single cell 'B', expected False, got {result8}"

    # Test Case 9: Long word
    board9 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word9 = "ABCDEFGHI"
    result9 = solution.exist(board9, word9)
    assert result9 == True, f"Failed for 'ABCDEFGHI', expected True, got {result9}"

    # Test Case 10: Word longer than board
    board10 = [["A", "B"], ["C", "D"]]
    word10 = "ABCDE"
    result10 = solution.exist(board10, word10)
    assert result10 == False, f"Failed for 'ABCDE', expected False, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(3, 3), (4, 4), (5, 5)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tWord\tTime\t\tResult")
    print("-" * 50)

    for m, n in test_sizes:
        # Generate test data
        board = [[chr(ord("A") + i + j) for j in range(n)] for i in range(m)]
        word = "A" * min(m * n, 10)  # Keep word length reasonable

        # Test approach
        start_time = time.time()
        result = solution.exist(board, word)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{m}x{n}\t{len(word)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(M * N * 4^L) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(M * N * 4^L) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            expected_ratio = (m2 * n2) / (m1 * n1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(M*N*4^L): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance for exponential complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(M*N*4^L)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(M*N*4^L) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(M*N*4^L), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(M*N*4^L)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1x1 board)
    board1 = [["A"]]
    result1 = solution.exist(board1, "A")
    assert result1 == True, f"1x1 board failed: {result1}"
    print(f"1x1 board: ✅")

    # Edge Case 2: Maximum constraint (6x6 board)
    board2 = [[chr(ord("A") + i + j) for j in range(6)] for i in range(6)]
    result2 = solution.exist(board2, "A")
    assert result2 == True, f"6x6 board failed: {result2}"
    print(f"6x6 board: ✅")

    # Edge Case 3: Maximum word length (15 characters)
    board3 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word3 = "ABCDEFGHIJKLMNO"
    result3 = solution.exist(board3, word3)
    assert result3 == False, f"Max word length failed: {result3}"
    print(f"Maximum word length: ✅")

    # Edge Case 4: All same characters
    board4 = [["A", "A"], ["A", "A"]]
    result4 = solution.exist(board4, "AAAA")
    assert result4 == True, f"All same characters failed: {result4}"
    print(f"All same characters: ✅")

    # Edge Case 5: No path possible
    board5 = [["A", "B"], ["C", "D"]]
    result5 = solution.exist(board5, "AC")
    assert result5 == False, f"No path possible failed: {result5}"
    print(f"No path possible: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Word Search:")

    # Large dataset
    board = [
        ["A", "B", "C", "D", "E", "F"],
        ["G", "H", "I", "J", "K", "L"],
        ["M", "N", "O", "P", "Q", "R"],
    ]
    word = "ABCDEFGHIJKLMNO"

    start_time = time.time()
    result = solution.exist(board, word)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (6x3 board, 15-char word):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Word Search Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the exist method")
        print("- Aim for O(M*N*4^L) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(M*N*4^L)")
        print("- Consider using DFS with backtracking")

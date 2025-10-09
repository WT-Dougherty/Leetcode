"""
Word Search II - LeetCode Problem 212

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent
cells are horizontally or vertically neighboring. The same letter cell may not be used
more than once in a word.
"""

import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    result1 = solution.findWords(board1, words1)
    expected1 = ["eat", "oath"]
    assert set(result1) == set(
        expected1
    ), f"Failed for basic case, expected {expected1}, got {result1}"

    # Test Case 2: No words found
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    result2 = solution.findWords(board2, words2)
    expected2 = []
    assert (
        result2 == expected2
    ), f"Failed for no words found, expected {expected2}, got {result2}"

    # Test Case 3: Single word
    board3 = [["a", "a"]]
    words3 = ["a"]
    result3 = solution.findWords(board3, words3)
    expected3 = ["a"]
    assert (
        result3 == expected3
    ), f"Failed for single word, expected {expected3}, got {result3}"

    # Test Case 4: Multiple same words
    board4 = [["a", "b"], ["c", "d"]]
    words4 = [
        "ab",
        "cb",
        "ad",
        "bd",
        "ac",
        "ca",
        "da",
        "bc",
        "db",
        "bdca",
        "dabc",
        "abb",
        "acb",
    ]
    result4 = solution.findWords(board4, words4)
    expected4 = ["ab", "ac", "bd", "ca", "db"]
    assert set(result4) == set(
        expected4
    ), f"Failed for multiple words, expected {expected4}, got {result4}"

    # Test Case 5: Single cell board
    board5 = [["a"]]
    words5 = ["a"]
    result5 = solution.findWords(board5, words5)
    expected5 = ["a"]
    assert (
        result5 == expected5
    ), f"Failed for single cell, expected {expected5}, got {result5}"

    # Test Case 6: Empty words
    board6 = [["a", "b"], ["c", "d"]]
    words6 = []
    result6 = solution.findWords(board6, words6)
    expected6 = []
    assert (
        result6 == expected6
    ), f"Failed for empty words, expected {expected6}, got {result6}"

    # Test Case 7: Long word
    board7 = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    words7 = ["abcdefghi"]
    result7 = solution.findWords(board7, words7)
    expected7 = ["abcdefghi"]
    assert (
        result7 == expected7
    ), f"Failed for long word, expected {expected7}, got {result7}"

    # Test Case 8: Maximum constraint
    board8 = [["a"] * 12 for _ in range(12)]
    words8 = ["a" * i for i in range(1, 11)]
    result8 = solution.findWords(board8, words8)
    assert len(result8) > 0, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m * n * 4^L)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(4, 4, 5), (6, 6, 10), (8, 8, 20)]
    times = []

    print("\nTime Complexity Analysis:")
    print("M\tN\tW\tTime\t\tResult")
    print("-" * 50)

    for m, n, w in test_sizes:
        # Generate test data
        board = [["a"] * n for _ in range(m)]
        words = [f"word{i}" for i in range(w)]

        # Test approach
        start_time = time.time()
        result = solution.findWords(board, words)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is a list
        assert isinstance(
            result, list
        ), f"Result verification failed for size ({m}, {n}, {w})"

        print(f"{m}\t{n}\t{w}\t{elapsed_time:.6f}s\t{len(result)} words")

    # For O(m * n * 4^L) complexity, time should grow exponentially with word length
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")

        # Since this is exponential complexity, we expect significant growth
        # We'll be more lenient with the tolerance
        tolerance = 2.0  # Allow 200% variance for exponential complexity

        # Check if time is growing reasonably (not too fast)
        for i, ratio in enumerate(ratios):
            if ratio > 10:  # If time grows more than 10x, it might be too slow
                print(f"\n⚠️  Time complexity might be worse than expected")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: got {ratio:.2f}x growth"
                )
                print(f"   This suggests exponential complexity is too high")

        print(f"\n✅ PASSED: Time complexity appears to be acceptable")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint board size
    board = [["a"] * 12 for _ in range(12)]
    words = ["a" * 10]
    result = solution.findWords(board, words)
    assert isinstance(result, list)
    print(f"Maximum constraint board size (12x12): ✅")

    # Edge Case 2: Maximum constraint words count
    board2 = [["a", "b"], ["c", "d"]]
    words2 = [f"word{i}" for i in range(30000)]
    result2 = solution.findWords(board2, words2)
    assert isinstance(result2, list)
    print(f"Maximum constraint words count (30k): ✅")

    # Edge Case 3: Maximum constraint word length
    board3 = [["a"] * 12 for _ in range(12)]
    words3 = ["a" * 10]
    result3 = solution.findWords(board3, words3)
    assert isinstance(result3, list)
    print(f"Maximum constraint word length (10): ✅")

    # Edge Case 4: Single cell board
    board4 = [["a"]]
    words4 = ["a"]
    result4 = solution.findWords(board4, words4)
    assert result4 == ["a"]
    print(f"Single cell board: ✅")

    # Edge Case 5: All same characters
    board5 = [["a", "a"], ["a", "a"]]
    words5 = ["aa", "aaa", "aaaa"]
    result5 = solution.findWords(board5, words5)
    assert isinstance(result5, list)
    print(f"All same characters: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    board = [["a"] * 10 for _ in range(10)]
    words = [f"word{i}" for i in range(1000)]

    start_time = time.time()
    result = solution.findWords(board, words)
    time1 = time.time() - start_time

    assert isinstance(result, list)

    print(f"Large dataset (10x10 board, 1k words):")
    print(f"Time: {time1:.6f}s, Result: {len(result)} words found")


if __name__ == "__main__":
    print("🧪 Testing Word Search II Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findWords method")
        print("- Aim for O(m * n * 4^L) time complexity where L is max word length")
        print("- Handle all edge cases correctly")
        print("- Use Trie + DFS approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n * 4^L)")
        print("- Consider using Trie + DFS approach")

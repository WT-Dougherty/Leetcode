"""
Word Ladder - LeetCode Problem 127

A transformation sequence from word beginWord to word endWord using a dictionary wordList
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList.
"""

import time
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    assert result1 == 5, f"Failed for basic case, expected 5, got {result1}"

    # Test Case 2: Impossible case
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    assert result2 == 0, f"Failed for impossible case, expected 0, got {result2}"

    # Test Case 3: Same word
    beginWord3 = "hit"
    endWord3 = "hit"
    wordList3 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    assert result3 == 1, f"Failed for same word, expected 1, got {result3}"

    # Test Case 4: Direct transformation
    beginWord4 = "hit"
    endWord4 = "hot"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    assert result4 == 2, f"Failed for direct transformation, expected 2, got {result4}"

    # Test Case 5: Empty wordList
    beginWord5 = "hit"
    endWord5 = "cog"
    wordList5 = []
    result5 = solution.ladderLength(beginWord5, endWord5, wordList5)
    assert result5 == 0, f"Failed for empty wordList, expected 0, got {result5}"

    # Test Case 6: Single word in wordList
    beginWord6 = "hit"
    endWord6 = "hot"
    wordList6 = ["hot"]
    result6 = solution.ladderLength(beginWord6, endWord6, wordList6)
    assert result6 == 2, f"Failed for single word, expected 2, got {result6}"

    # Test Case 7: Complex case
    beginWord7 = "a"
    endWord7 = "c"
    wordList7 = ["a", "b", "c"]
    result7 = solution.ladderLength(beginWord7, endWord7, wordList7)
    assert result7 == 2, f"Failed for complex case, expected 2, got {result7}"

    # Test Case 8: No path
    beginWord8 = "hot"
    endWord8 = "dog"
    wordList8 = ["hot", "dog"]
    result8 = solution.ladderLength(beginWord8, endWord8, wordList8)
    assert result8 == 0, f"Failed for no path, expected 0, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Words\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create words with single character differences
        wordList = []
        for i in range(size):
            word = "a" * 5  # 5 character words
            word = word[: i % 5] + chr(ord("a") + (i % 26)) + word[(i % 5) + 1 :]
            wordList.append(word)

        beginWord = "aaaaa"
        endWord = wordList[-1]

        # Test approach
        start_time = time.time()
        result = solution.ladderLength(beginWord, endWord, wordList)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(M^2 * N) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(M^2 * N) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (5**2) * test_sizes[i - 1]  # M=5, N=size
            curr_complexity = (5**2) * test_sizes[i]
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(M^2*N): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(M^2 * N)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(M^2 * N) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(M^2 * N), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(M^2 * N)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 word)
    beginWord1 = "a"
    endWord1 = "b"
    wordList1 = ["b"]
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    assert result1 == 2, f"Single word failed: {result1}"
    print(f"Single word: ✅")

    # Edge Case 2: Maximum constraint (5000 words)
    wordList2 = []
    for i in range(5000):
        word = "a" * 10
        word = word[: i % 10] + chr(ord("a") + (i % 26)) + word[(i % 10) + 1 :]
        wordList2.append(word)

    beginWord2 = "aaaaaaaaaa"
    endWord2 = wordList2[-1]

    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum word length (10 characters)
    beginWord3 = "a" * 10
    endWord3 = "b" * 10
    wordList3 = ["b" * 10]
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    assert result3 == 2, f"Max word length failed: {result3}"
    print(f"Maximum word length: ✅")

    # Edge Case 4: All same words
    beginWord4 = "abc"
    endWord4 = "def"
    wordList4 = ["abc"] * 100
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    assert result4 == 0, f"All same words failed: {result4}"
    print(f"All same words: ✅")

    # Edge Case 5: No valid transformations
    beginWord5 = "abc"
    endWord5 = "xyz"
    wordList5 = ["def", "ghi", "jkl"]
    result5 = solution.ladderLength(beginWord5, endWord5, wordList5)
    assert result5 == 0, f"No valid transformations failed: {result5}"
    print(f"No valid transformations: ✅")

    # Edge Case 6: Single character words
    beginWord6 = "a"
    endWord6 = "z"
    wordList6 = [
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    result6 = solution.ladderLength(beginWord6, endWord6, wordList6)
    assert result6 == 26, f"Single character words failed: {result6}"
    print(f"Single character words: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Word Ladder:")

    # Large dataset
    wordList = []
    for i in range(1000):
        word = "a" * 5
        word = word[: i % 5] + chr(ord("a") + (i % 26)) + word[(i % 5) + 1 :]
        wordList.append(word)

    beginWord = "aaaaa"
    endWord = wordList[-1]

    start_time = time.time()
    result = solution.ladderLength(beginWord, endWord, wordList)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 words, 5 characters each):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Word Ladder Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the ladderLength method")
        print("- Aim for O(M^2 * N) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(M^2 * N)")
        print("- Consider using BFS with word transformation")

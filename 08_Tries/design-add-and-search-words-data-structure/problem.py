"""
Design Add And Search Words Data Structure - LeetCode Problem 211

Design a data structure that supports adding new words and finding if a string matches
any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that
  matches word or false otherwise. word may contain dots '.' where dots can be matched
  with any letter.
"""

import time
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


class Solution:
    def __init__(self):
        self.wordDict = WordDictionary()

    def createWordDictionary(self) -> WordDictionary:
        """Helper method to create WordDictionary for testing"""
        return self.wordDict


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic operations
    wordDict = solution.createWordDictionary()
    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")

    result1 = wordDict.search("pad")
    assert result1 == False, f"Failed for search('pad'), expected False, got {result1}"

    result2 = wordDict.search("bad")
    assert result2 == True, f"Failed for search('bad'), expected True, got {result2}"

    result3 = wordDict.search(".ad")
    assert result3 == True, f"Failed for search('.ad'), expected True, got {result3}"

    result4 = wordDict.search("b..")
    assert result4 == True, f"Failed for search('b..'), expected True, got {result4}"

    # Test Case 2: Empty dictionary
    wordDict2 = WordDictionary()
    result5 = wordDict2.search("")
    assert (
        result5 == False
    ), f"Failed for empty dictionary search, expected False, got {result5}"

    # Test Case 3: Single character
    wordDict3 = WordDictionary()
    wordDict3.addWord("a")
    result6 = wordDict3.search("a")
    assert (
        result6 == True
    ), f"Failed for single char search, expected True, got {result6}"

    result7 = wordDict3.search(".")
    assert (
        result7 == True
    ), f"Failed for single dot search, expected True, got {result7}"

    # Test Case 4: Multiple dots
    wordDict4 = WordDictionary()
    wordDict4.addWord("cat")
    wordDict4.addWord("bat")
    wordDict4.addWord("rat")

    result8 = wordDict4.search("c.t")
    assert result8 == True, f"Failed for search('c.t'), expected True, got {result8}"

    result9 = wordDict4.search("..t")
    assert result9 == True, f"Failed for search('..t'), expected True, got {result9}"

    # Test Case 5: No matches
    wordDict5 = WordDictionary()
    wordDict5.addWord("hello")
    result10 = wordDict5.search("world")
    assert result10 == False, f"Failed for no match, expected False, got {result10}"

    result11 = wordDict5.search("h.llo")
    assert (
        result11 == True
    ), f"Failed for search('h.llo'), expected True, got {result11}"

    # Test Case 6: Empty string
    wordDict6 = WordDictionary()
    wordDict6.addWord("")
    result12 = wordDict6.search("")
    assert (
        result12 == True
    ), f"Failed for empty string search, expected True, got {result12}"

    # Test Case 7: Long words
    long_word = "a" * 25
    wordDict7 = WordDictionary()
    wordDict7.addWord(long_word)
    result13 = wordDict7.search(long_word)
    assert (
        result13 == True
    ), f"Failed for long word search, expected True, got {result13}"

    # Test Case 8: Maximum constraint
    wordDict8 = WordDictionary()
    for i in range(10000):
        word = f"word{i}"
        wordDict8.addWord(word)

    result14 = wordDict8.search("word0")
    assert (
        result14 == True
    ), f"Failed for max constraint search, expected True, got {result14}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m) for addWord, O(m * 26^k) for search"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        wordDict = WordDictionary()

        # Test approach - measure time for operations
        start_time = time.time()

        # AddWord operations
        for i in range(size):
            word = f"word{i}"
            wordDict.addWord(word)

        # Search operations (without dots)
        for i in range(size):
            word = f"word{i}"
            wordDict.search(word)

        # Search operations (with dots)
        for i in range(size):
            pattern = f"wo.{i}"
            wordDict.search(pattern)

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations")

    # For O(m) addWord and O(m * 26^k) search, time should grow with size
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios: {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than expected")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m) addWord, O(m * 26^k) search"
                )

        print(f"\n✅ PASSED: Time complexity appears to be acceptable")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint calls
    wordDict = WordDictionary()
    for i in range(10000):
        word = f"word{i}"
        wordDict.addWord(word)

    result = wordDict.search("word0")
    assert result == True
    print(f"Maximum constraint calls (10k): ✅")

    # Edge Case 2: Maximum constraint word length
    long_word = "a" * 25
    wordDict2 = WordDictionary()
    wordDict2.addWord(long_word)
    result = wordDict2.search(long_word)
    assert result == True
    print(f"Maximum constraint word length (25): ✅")

    # Edge Case 3: Maximum dots (2 dots)
    wordDict3 = WordDictionary()
    wordDict3.addWord("abc")
    wordDict3.addWord("adc")
    wordDict3.addWord("aec")
    result = wordDict3.search("a.c")
    assert result == True
    print(f"Maximum dots (2): ✅")

    # Edge Case 4: All dots
    wordDict4 = WordDictionary()
    wordDict4.addWord("cat")
    wordDict4.addWord("bat")
    wordDict4.addWord("rat")
    result = wordDict4.search("...")
    assert result == True
    print(f"All dots: ✅")

    # Edge Case 5: Single character words
    wordDict5 = WordDictionary()
    for i in range(26):
        wordDict5.addWord(chr(ord("a") + i))

    result = wordDict5.search(".")
    assert result == True
    print(f"Single character words: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    wordDict = WordDictionary()

    start_time = time.time()
    for i in range(5000):
        word = f"word{i}"
        wordDict.addWord(word)
    time1 = time.time() - start_time

    start_time = time.time()
    for i in range(5000):
        word = f"word{i}"
        wordDict.search(word)
    time2 = time.time() - start_time

    start_time = time.time()
    for i in range(5000):
        pattern = f"wo.{i}"
        wordDict.search(pattern)
    time3 = time.time() - start_time

    print(f"Large dataset (5k operations each):")
    print(f"AddWord time: {time1:.6f}s")
    print(f"Search time: {time2:.6f}s")
    print(f"Search with dots time: {time3:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Design Add And Search Words Data Structure Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the WordDictionary class")
        print("- Aim for O(m) time complexity for addWord")
        print(
            "- Aim for O(m * 26^k) time complexity for search where k is number of dots"
        )
        print("- Handle all edge cases correctly")
        print("- Use Trie with DFS for dot matching")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than expected")
        print("- Consider using Trie with DFS for dot matching")

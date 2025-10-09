"""
Implement Trie Prefix Tree - LeetCode Problem 208

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and search strings in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

import time
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


class Solution:
    def __init__(self):
        self.trie = Trie()

    def createTrie(self) -> Trie:
        """Helper method to create Trie for testing"""
        return self.trie


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic operations
    trie = solution.createTrie()
    trie.insert("apple")
    result1 = trie.search("apple")
    assert result1 == True, f"Failed for search('apple'), expected True, got {result1}"

    result2 = trie.search("app")
    assert result2 == False, f"Failed for search('app'), expected False, got {result2}"

    result3 = trie.startsWith("app")
    assert (
        result3 == True
    ), f"Failed for startsWith('app'), expected True, got {result3}"

    trie.insert("app")
    result4 = trie.search("app")
    assert (
        result4 == True
    ), f"Failed for search('app') after insert, expected True, got {result4}"

    # Test Case 2: Empty trie
    trie2 = Trie()
    result5 = trie2.search("")
    assert (
        result5 == False
    ), f"Failed for empty trie search, expected False, got {result5}"

    result6 = trie2.startsWith("")
    assert (
        result6 == False
    ), f"Failed for empty trie startsWith, expected False, got {result6}"

    # Test Case 3: Single character
    trie3 = Trie()
    trie3.insert("a")
    result7 = trie3.search("a")
    assert (
        result7 == True
    ), f"Failed for single char search, expected True, got {result7}"

    result8 = trie3.startsWith("a")
    assert (
        result8 == True
    ), f"Failed for single char startsWith, expected True, got {result8}"

    # Test Case 4: Multiple words
    trie4 = Trie()
    trie4.insert("cat")
    trie4.insert("car")
    trie4.insert("card")
    trie4.insert("careful")
    trie4.insert("care")

    result9 = trie4.search("car")
    assert result9 == True, f"Failed for search('car'), expected True, got {result9}"

    result10 = trie4.search("care")
    assert result10 == True, f"Failed for search('care'), expected True, got {result10}"

    result11 = trie4.startsWith("car")
    assert (
        result11 == True
    ), f"Failed for startsWith('car'), expected True, got {result11}"

    result12 = trie4.search("careful")
    assert (
        result12 == True
    ), f"Failed for search('careful'), expected True, got {result12}"

    # Test Case 5: Non-existent words
    trie5 = Trie()
    trie5.insert("hello")
    result13 = trie5.search("world")
    assert (
        result13 == False
    ), f"Failed for non-existent word, expected False, got {result13}"

    result14 = trie5.startsWith("xyz")
    assert (
        result14 == False
    ), f"Failed for non-existent prefix, expected False, got {result14}"

    # Test Case 6: Empty string
    trie6 = Trie()
    trie6.insert("")
    result15 = trie6.search("")
    assert (
        result15 == True
    ), f"Failed for empty string search, expected True, got {result15}"

    # Test Case 7: Long words
    long_word = "a" * 2000
    trie7 = Trie()
    trie7.insert(long_word)
    result16 = trie7.search(long_word)
    assert (
        result16 == True
    ), f"Failed for long word search, expected True, got {result16}"

    # Test Case 8: Maximum constraint
    trie8 = Trie()
    for i in range(30000):
        word = f"word{i}"
        trie8.insert(word)

    result17 = trie8.search("word0")
    assert (
        result17 == True
    ), f"Failed for max constraint search, expected True, got {result17}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        trie = Trie()

        # Test approach - measure time for operations
        start_time = time.time()

        # Insert operations
        for i in range(size):
            word = f"word{i}"
            trie.insert(word)

        # Search operations
        for i in range(size):
            word = f"word{i}"
            trie.search(word)

        # StartsWith operations
        for i in range(size):
            prefix = f"wo{i}"
            trie.startsWith(prefix)

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations")

    # For O(m) operations, time should grow approximately linearly with size
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m log m) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint calls
    trie = Trie()
    for i in range(30000):
        word = f"word{i}"
        trie.insert(word)

    result = trie.search("word0")
    assert result == True
    print(f"Maximum constraint calls (30k): ✅")

    # Edge Case 2: Maximum constraint word length
    long_word = "a" * 2000
    trie2 = Trie()
    trie2.insert(long_word)
    result = trie2.search(long_word)
    assert result == True
    print(f"Maximum constraint word length (2k): ✅")

    # Edge Case 3: Single character words
    trie3 = Trie()
    for i in range(26):
        trie3.insert(chr(ord("a") + i))

    result = trie3.search("a")
    assert result == True
    print(f"Single character words: ✅")

    # Edge Case 4: Empty string
    trie4 = Trie()
    trie4.insert("")
    result = trie4.search("")
    assert result == True
    print(f"Empty string: ✅")

    # Edge Case 5: Repeated words
    trie5 = Trie()
    for i in range(1000):
        trie5.insert("same")

    result = trie5.search("same")
    assert result == True
    print(f"Repeated words: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    trie = Trie()

    start_time = time.time()
    for i in range(10000):
        word = f"word{i}"
        trie.insert(word)
    time1 = time.time() - start_time

    start_time = time.time()
    for i in range(10000):
        word = f"word{i}"
        trie.search(word)
    time2 = time.time() - start_time

    start_time = time.time()
    for i in range(10000):
        prefix = f"wo{i}"
        trie.startsWith(prefix)
    time3 = time.time() - start_time

    print(f"Large dataset (10k operations each):")
    print(f"Insert time: {time1:.6f}s")
    print(f"Search time: {time2:.6f}s")
    print(f"StartsWith time: {time3:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Implement Trie Prefix Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the Trie class")
        print("- Aim for O(m) time complexity for each operation")
        print("- Handle all edge cases correctly")
        print("- Use TrieNode with children dictionary")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m)")
        print("- Consider using TrieNode with children dictionary")

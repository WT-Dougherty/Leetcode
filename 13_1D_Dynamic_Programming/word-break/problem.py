"""
Word Break - LeetCode Problem 139

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

import time
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.wordBreak(s1, wordDict1)
    assert (
        result1 == True
    ), f"Failed for s='{s1}', wordDict={wordDict1}, expected True, got {result1}"

    # Test Case 2: Reusable words
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    assert (
        result2 == True
    ), f"Failed for s='{s2}', wordDict={wordDict2}, expected True, got {result2}"

    # Test Case 3: Impossible case
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    assert (
        result3 == False
    ), f"Failed for s='{s3}', wordDict={wordDict3}, expected False, got {result3}"

    # Test Case 4: Single word
    s4 = "leetcode"
    wordDict4 = ["leet", "code"]
    result4 = solution.wordBreak(s4, wordDict4)
    assert (
        result4 == True
    ), f"Failed for s='{s4}', wordDict={wordDict4}, expected True, got {result4}"

    # Test Case 5: Empty string
    s5 = ""
    wordDict5 = ["leet", "code"]
    result5 = solution.wordBreak(s5, wordDict5)
    assert (
        result5 == True
    ), f"Failed for s='{s5}', wordDict={wordDict5}, expected True, got {result5}"

    # Test Case 6: Single character
    s6 = "a"
    wordDict6 = ["a"]
    result6 = solution.wordBreak(s6, wordDict6)
    assert (
        result6 == True
    ), f"Failed for s='{s6}', wordDict={wordDict6}, expected True, got {result6}"

    # Test Case 7: Complex case
    s7 = "catsanddog"
    wordDict7 = ["cat", "cats", "and", "sand", "dog"]
    result7 = solution.wordBreak(s7, wordDict7)
    assert (
        result7 == True
    ), f"Failed for s='{s7}', wordDict={wordDict7}, expected True, got {result7}"

    # Test Case 8: Edge case
    s8 = "goalspecial"
    wordDict8 = ["go", "goal", "goals", "special"]
    result8 = solution.wordBreak(s8, wordDict8)
    assert (
        result8 == True
    ), f"Failed for s='{s8}', wordDict={wordDict8}, expected True, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("Length\tWords\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create string and wordDict
        s = "a" * size
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]

        # Test approach
        start_time = time.time()
        result = solution.wordBreak(s, wordDict)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(wordDict)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * m) complexity where n is length of s and m is average word length
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n * m) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * 3  # Average word length ~3
            curr_complexity = test_sizes[i] * 3
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n*m): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n * m)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n * m) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n * m), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * m)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 character)
    s1 = "a"
    wordDict1 = ["a"]
    result1 = solution.wordBreak(s1, wordDict1)
    assert result1 == True, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (300 characters)
    s2 = "a" * 300
    wordDict2 = ["a"]
    result2 = solution.wordBreak(s2, wordDict2)
    assert isinstance(result2, bool), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum wordDict length (1000 words)
    s3 = "a"
    wordDict3 = ["a" + str(i) for i in range(1000)]
    result3 = solution.wordBreak(s3, wordDict3)
    assert isinstance(result3, bool), f"Max wordDict failed: {result3}"
    print(f"Maximum wordDict: ✅")

    # Edge Case 4: Maximum word length (20 characters)
    s4 = "a" * 20
    wordDict4 = ["a" * 20]
    result4 = solution.wordBreak(s4, wordDict4)
    assert result4 == True, f"Max word length failed: {result4}"
    print(f"Maximum word length: ✅")

    # Edge Case 5: Empty wordDict
    s5 = "a"
    wordDict5 = []
    result5 = solution.wordBreak(s5, wordDict5)
    assert result5 == False, f"Empty wordDict failed: {result5}"
    print(f"Empty wordDict: ✅")

    # Edge Case 6: No matching words
    s6 = "abc"
    wordDict6 = ["def", "ghi"]
    result6 = solution.wordBreak(s6, wordDict6)
    assert result6 == False, f"No matching words failed: {result6}"
    print(f"No matching words: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Word Break:")

    # Large dataset
    s = "a" * 100
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]

    start_time = time.time()
    result = solution.wordBreak(s, wordDict)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100 characters, {len(wordDict)} words):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Word Break Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the wordBreak method")
        print("- Aim for O(n * m) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * m)")
        print("- Consider using dynamic programming with memoization")

"""
Alien Dictionary - LeetCode Problem 269

There is a new alien language that uses the English alphabet. However, the order among
the letters is unknown to you.
"""

import time
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    result1 = solution.alienOrder(words1)
    expected1 = "wertf"
    assert (
        result1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {result1}"

    # Test Case 2: Simple case
    words2 = ["z", "x"]
    result2 = solution.alienOrder(words2)
    expected2 = "zx"
    assert (
        result2 == expected2
    ), f"Failed for simple case, expected {expected2}, got {result2}"

    # Test Case 3: Invalid case
    words3 = ["z", "x", "z"]
    result3 = solution.alienOrder(words3)
    expected3 = ""
    assert (
        result3 == expected3
    ), f"Failed for invalid case, expected {expected3}, got {result3}"

    # Test Case 4: Single word
    words4 = ["abc"]
    result4 = solution.alienOrder(words4)
    expected4 = "abc"
    assert (
        result4 == expected4
    ), f"Failed for single word, expected {expected4}, got {result4}"

    # Test Case 5: Multiple words same prefix
    words5 = ["abc", "ab"]
    result5 = solution.alienOrder(words5)
    expected5 = ""
    assert (
        result5 == expected5
    ), f"Failed for same prefix, expected {expected5}, got {result5}"

    # Test Case 6: Complex case
    words6 = ["wrt", "wrf", "er", "ett", "rftt", "te"]
    result6 = solution.alienOrder(words6)
    # Multiple valid solutions possible, just check it's not empty and contains all letters
    assert result6 != "", f"Failed for complex case, expected non-empty, got {result6}"
    assert len(result6) >= 5, f"Failed for complex case length, expected >= 5, got {len(result6)}"

    # Test Case 7: Two words
    words7 = ["ab", "adc"]
    result7 = solution.alienOrder(words7)
    expected7 = "abcd"
    assert (
        result7 == expected7
    ), f"Failed for two words, expected {expected7}, got {result7}"

    # Test Case 8: Empty list
    words8 = []
    result8 = solution.alienOrder(words8)
    expected8 = ""
    assert (
        result8 == expected8
    ), f"Failed for empty list, expected {expected8}, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Words\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create words with increasing length
        words = []
        for i in range(size):
            word = ""
            for j in range(min(i + 1, 10)):  # Max 10 characters
                word += chr(ord("a") + (j % 26))
            words.append(word)

        # Test approach
        start_time = time.time()
        result = solution.alienOrder(words)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} chars")

    # Verify O(C) complexity where C is total characters
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(C) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            # Approximate character count grows quadratically
            prev_chars = sum(min(j + 1, 10) for j in range(test_sizes[i - 1]))
            curr_chars = sum(min(j + 1, 10) for j in range(test_sizes[i]))
            expected_ratio = curr_chars / prev_chars
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(C): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(C)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(C) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(C), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(C)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 word)
    words1 = ["a"]
    result1 = solution.alienOrder(words1)
    assert result1 == "a", f"Single word failed: {result1}"
    print(f"Single word: ✅")

    # Edge Case 2: Maximum constraint (100 words)
    words2 = []
    for i in range(100):
        word = ""
        for j in range(min(i + 1, 100)):  # Max 100 characters
            word += chr(ord("a") + (j % 26))
        words2.append(word)

    result2 = solution.alienOrder(words2)
    assert isinstance(result2, str), f"Max constraint failed: {type(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same words
    words3 = ["abc"] * 50
    result3 = solution.alienOrder(words3)
    assert result3 == "abc", f"All same words failed: {result3}"
    print(f"All same words: ✅")

    # Edge Case 4: Single character words
    words4 = ["a", "b", "c", "d", "e"]
    result4 = solution.alienOrder(words4)
    assert len(result4) == 5, f"Single character words failed: {len(result4)}"
    print(f"Single character words: ✅")

    # Edge Case 5: Invalid prefix case
    words5 = ["abc", "ab"]
    result5 = solution.alienOrder(words5)
    assert result5 == "", f"Invalid prefix failed: {result5}"
    print(f"Invalid prefix: ✅")

    # Edge Case 6: Empty words
    words6 = [""]
    result6 = solution.alienOrder(words6)
    assert result6 == "", f"Empty words failed: {result6}"
    print(f"Empty words: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Alien Dictionary:")

    # Large dataset
    words = []
    for i in range(50):
        word = ""
        for j in range(min(i + 1, 20)):  # Max 20 characters
            word += chr(ord("a") + (j % 26))
        words.append(word)

    start_time = time.time()
    result = solution.alienOrder(words)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (50 words, up to 20 chars each):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} characters")


if __name__ == "__main__":
    print("🧪 Testing Alien Dictionary Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the alienOrder method")
        print("- Aim for O(C) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(C)")
        print("- Consider using topological sort with cycle detection")

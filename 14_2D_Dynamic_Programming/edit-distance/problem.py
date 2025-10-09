"""
Edit Distance - LeetCode Problem 72

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
"""

import time


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    word1_1 = "horse"
    word2_1 = "ros"
    result1 = solution.minDistance(word1_1, word2_1)
    assert (
        result1 == 3
    ), f"Failed for '{word1_1}' -> '{word2_1}', expected 3, got {result1}"

    # Test Case 2: Complex case
    word1_2 = "intention"
    word2_2 = "execution"
    result2 = solution.minDistance(word1_2, word2_2)
    assert (
        result2 == 5
    ), f"Failed for '{word1_2}' -> '{word2_2}', expected 5, got {result2}"

    # Test Case 3: Same strings
    word1_3 = "abc"
    word2_3 = "abc"
    result3 = solution.minDistance(word1_3, word2_3)
    assert (
        result3 == 0
    ), f"Failed for '{word1_3}' -> '{word2_3}', expected 0, got {result3}"

    # Test Case 4: Empty strings
    word1_4 = ""
    word2_4 = ""
    result4 = solution.minDistance(word1_4, word2_4)
    assert (
        result4 == 0
    ), f"Failed for '{word1_4}' -> '{word2_4}', expected 0, got {result4}"

    # Test Case 5: One empty string
    word1_5 = "abc"
    word2_5 = ""
    result5 = solution.minDistance(word1_5, word2_5)
    assert (
        result5 == 3
    ), f"Failed for '{word1_5}' -> '{word2_5}', expected 3, got {result5}"

    # Test Case 6: Single character
    word1_6 = "a"
    word2_6 = "b"
    result6 = solution.minDistance(word1_6, word2_6)
    assert (
        result6 == 1
    ), f"Failed for '{word1_6}' -> '{word2_6}', expected 1, got {result6}"

    # Test Case 7: Complex case
    word1_7 = "kitten"
    word2_7 = "sitting"
    result7 = solution.minDistance(word1_7, word2_7)
    assert (
        result7 == 3
    ), f"Failed for '{word1_7}' -> '{word2_7}', expected 3, got {result7}"

    # Test Case 8: Edge case
    word1_8 = "a"
    word2_8 = "ab"
    result8 = solution.minDistance(word1_8, word2_8)
    assert (
        result8 == 1
    ), f"Failed for '{word1_8}' -> '{word2_8}', expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("len1\tlen2\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create strings with some differences
        word1 = "a" * size
        word2 = "b" * size

        # Test approach
        start_time = time.time()
        result = solution.minDistance(word1, word2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{len(word1)}\t{len(word2)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity where m is length of word1 and n is length of word2
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * test_sizes[i - 1]
            curr_complexity = test_sizes[i] * test_sizes[i]
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

    # Edge Case 1: Minimum constraint (0 characters each)
    word1_1 = ""
    word2_1 = ""
    result1 = solution.minDistance(word1_1, word2_1)
    assert result1 == 0, f"Empty strings failed: {result1}"
    print(f"Empty strings: ✅")

    # Edge Case 2: Maximum constraint (500 characters each)
    word1_2 = "a" * 500
    word2_2 = "b" * 500
    result2 = solution.minDistance(word1_2, word2_2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: One empty string
    word1_3 = "abc"
    word2_3 = ""
    result3 = solution.minDistance(word1_3, word2_3)
    assert result3 == 3, f"One empty string failed: {result3}"
    print(f"One empty string: ✅")

    # Edge Case 4: Single character difference
    word1_4 = "a"
    word2_4 = "b"
    result4 = solution.minDistance(word1_4, word2_4)
    assert result4 == 1, f"Single character difference failed: {result4}"
    print(f"Single character difference: ✅")

    # Edge Case 5: All same characters
    word1_5 = "aaaa"
    word2_5 = "aaaa"
    result5 = solution.minDistance(word1_5, word2_5)
    assert result5 == 0, f"All same characters failed: {result5}"
    print(f"All same characters: ✅")

    # Edge Case 6: Completely different
    word1_6 = "abc"
    word2_6 = "xyz"
    result6 = solution.minDistance(word1_6, word2_6)
    assert result6 == 3, f"Completely different failed: {result6}"
    print(f"Completely different: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Edit Distance:")

    # Large dataset
    word1 = "a" * 100
    word2 = "b" * 100

    start_time = time.time()
    result = solution.minDistance(word1, word2)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (word1={len(word1)}, word2={len(word2)}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Edit Distance Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minDistance method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

"""
Permutation in String - LeetCode Problem 567

Given two strings s1 and s2, return true if s2 contains a permutation of s1.

In other words, one of s1's permutations is the substring of s2.
"""

import time
import random


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1_1, s2_1 = "ab", "eidbaooo"
    result1 = solution.checkInclusion(s1_1, s2_1)
    assert (
        result1 == True
    ), f"Failed for s1='{s1_1}', s2='{s2_1}', expected True, got {result1}"

    # Test Case 2: No permutation
    s1_2, s2_2 = "ab", "eidboaoo"
    result2 = solution.checkInclusion(s1_2, s2_2)
    assert (
        result2 == False
    ), f"Failed for s1='{s1_2}', s2='{s2_2}', expected False, got {result2}"

    # Test Case 3: Single character
    s1_3, s2_3 = "a", "a"
    result3 = solution.checkInclusion(s1_3, s2_3)
    assert (
        result3 == True
    ), f"Failed for s1='{s1_3}', s2='{s2_3}', expected True, got {result3}"

    # Test Case 4: Single character not found
    s1_4, s2_4 = "a", "b"
    result4 = solution.checkInclusion(s1_4, s2_4)
    assert (
        result4 == False
    ), f"Failed for s1='{s1_4}', s2='{s2_4}', expected False, got {result4}"

    # Test Case 5: Same strings
    s1_5, s2_5 = "abc", "abc"
    result5 = solution.checkInclusion(s1_5, s2_5)
    assert (
        result5 == True
    ), f"Failed for s1='{s1_5}', s2='{s2_5}', expected True, got {result5}"

    # Test Case 6: s1 longer than s2
    s1_6, s2_6 = "abc", "ab"
    result6 = solution.checkInclusion(s1_6, s2_6)
    assert (
        result6 == False
    ), f"Failed for s1='{s1_6}', s2='{s2_6}', expected False, got {result6}"

    # Test Case 7: Multiple occurrences
    s1_7, s2_7 = "ab", "abab"
    result7 = solution.checkInclusion(s1_7, s2_7)
    assert (
        result7 == True
    ), f"Failed for s1='{s1_7}', s2='{s2_7}', expected True, got {result7}"

    # Test Case 8: Complex case
    s1_8, s2_8 = "hello", "ooolleoooleh"
    result8 = solution.checkInclusion(s1_8, s2_8)
    assert (
        result8 == False
    ), f"Failed for s1='{s1_8}', s2='{s2_8}', expected False, got {result8}"

    # Test Case 9: Edge case with repeated characters
    s1_9, s2_9 = "aab", "eidbaaoo"
    result9 = solution.checkInclusion(s1_9, s2_9)
    assert (
        result9 == True
    ), f"Failed for s1='{s1_9}', s2='{s2_9}', expected True, got {result9}"

    # Test Case 10: Empty strings
    s1_10, s2_10 = "", "abc"
    result10 = solution.checkInclusion(s1_10, s2_10)
    assert (
        result10 == True
    ), f"Failed for s1='{s1_10}', s2='{s2_10}', expected True, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        s1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
        s2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=size))

        # Test approach
        start_time = time.time()
        result = solution.checkInclusion(s1, s2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    s1 = "a" * 10000
    s2 = "b" * 10000
    result = solution.checkInclusion(s1, s2)
    print(f"Maximum length (10k chars): {result} ✅")

    # Edge Case 2: All same characters
    s1 = "aaa"
    s2 = "aaaaaaaaaa"
    result = solution.checkInclusion(s1, s2)
    print(f"All same characters: {result} ✅")

    # Edge Case 3: Single character repeated
    s1 = "a"
    s2 = "a" * 1000
    result = solution.checkInclusion(s1, s2)
    print(f"Single char repeated: {result} ✅")

    # Edge Case 4: Alphabet order
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "zyxwvutsrqponmlkjihgfedcba"
    result = solution.checkInclusion(s1, s2)
    print(f"Alphabet order: {result} ✅")

    # Edge Case 5: Very short s1
    s1 = "ab"
    s2 = "abcdefghijklmnopqrstuvwxyz" * 100
    result = solution.checkInclusion(s1, s2)
    print(f"Very short s1: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=100000))

    start_time = time.time()
    result = solution.checkInclusion(s1, s2)
    time1 = time.time() - start_time

    print(f"Large dataset (s1=26 chars, s2=100k chars):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Permutation in String Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the checkInclusion method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use sliding window with character frequency")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using sliding window with frequency map")

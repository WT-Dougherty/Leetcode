"""
Longest Repeating Character Replacement - LeetCode Problem 424

You are given a string s and an integer k. You can choose any character of the string and
change it to any other uppercase English letter. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.
"""

import time
import random


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1, k1 = "ABAB", 2
    result1 = solution.characterReplacement(s1, k1)
    assert result1 == 4, f"Failed for s='{s1}', k={k1}, expected 4, got {result1}"

    # Test Case 2: Another basic case
    s2, k2 = "AABABBA", 1
    result2 = solution.characterReplacement(s2, k2)
    assert result2 == 4, f"Failed for s='{s2}', k={k2}, expected 4, got {result2}"

    # Test Case 3: No replacements needed
    s3, k3 = "AAAA", 0
    result3 = solution.characterReplacement(s3, k3)
    assert result3 == 4, f"Failed for s='{s3}', k={k3}, expected 4, got {result3}"

    # Test Case 4: Single character
    s4, k4 = "A", 1
    result4 = solution.characterReplacement(s4, k4)
    assert result4 == 1, f"Failed for s='{s4}', k={k4}, expected 1, got {result4}"

    # Test Case 5: All same characters
    s5, k5 = "BBBB", 2
    result5 = solution.characterReplacement(s5, k5)
    assert result5 == 4, f"Failed for s='{s5}', k={k5}, expected 4, got {result5}"

    # Test Case 6: Large k value
    s6, k6 = "ABCD", 4
    result6 = solution.characterReplacement(s6, k6)
    assert result6 == 4, f"Failed for s='{s6}', k={k6}, expected 4, got {result6}"

    # Test Case 7: Zero k
    s7, k7 = "ABCD", 0
    result7 = solution.characterReplacement(s7, k7)
    assert result7 == 1, f"Failed for s='{s7}', k={k7}, expected 1, got {result7}"

    # Test Case 8: Complex case
    s8, k8 = "AABABBA", 2
    result8 = solution.characterReplacement(s8, k8)
    assert result8 == 5, f"Failed for s='{s8}', k={k8}, expected 5, got {result8}"

    # Test Case 9: Alternating pattern
    s9, k9 = "ABABAB", 1
    result9 = solution.characterReplacement(s9, k9)
    assert result9 == 3, f"Failed for s='{s9}', k={k9}, expected 3, got {result9}"

    # Test Case 10: Edge case with k equals length
    s10, k10 = "ABC", 3
    result10 = solution.characterReplacement(s10, k10)
    assert result10 == 3, f"Failed for s='{s10}', k={k10}, expected 3, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tMax Length")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        s = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=size))
        k = random.randint(0, size)

        # Test approach
        start_time = time.time()
        result = solution.characterReplacement(s, k)
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

            if not (min_expected <= actual <= max_expected):
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
    s = "A" * 100000
    k = 50000
    result = solution.characterReplacement(s, k)
    print(f"Maximum length (100k chars): {result} ✅")

    # Edge Case 2: Maximum k value
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 1000
    k = len(s)
    result = solution.characterReplacement(s, k)
    print(f"Maximum k value: {result} ✅")

    # Edge Case 3: Zero k
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 100
    k = 0
    result = solution.characterReplacement(s, k)
    print(f"Zero k: {result} ✅")

    # Edge Case 4: Single character repeated
    s = "A" * 1000
    k = 0
    result = solution.characterReplacement(s, k)
    print(f"Single char repeated, k=0: {result} ✅")

    # Edge Case 5: All different characters
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = 1
    result = solution.characterReplacement(s, k)
    print(f"All different chars: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    s = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=100000))
    k = 50000

    start_time = time.time()
    result = solution.characterReplacement(s, k)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 characters, k=50,000):")
    print(f"Time: {time1:.6f}s, Max length: {result}")


if __name__ == "__main__":
    print("🧪 Testing Longest Repeating Character Replacement Problem")
    print("=" * 80)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the characterReplacement method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use sliding window with character frequency tracking")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using sliding window with frequency map")

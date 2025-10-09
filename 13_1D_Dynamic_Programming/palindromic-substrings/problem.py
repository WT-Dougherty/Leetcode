"""
Palindromic Substrings - LeetCode Problem 647

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

import time


class Solution:
    def countSubstrings(self, s: str) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "abc"
    result1 = solution.countSubstrings(s1)
    assert result1 == 3, f"Failed for '{s1}', expected 3, got {result1}"

    # Test Case 2: Multiple palindromes
    s2 = "aaa"
    result2 = solution.countSubstrings(s2)
    assert result2 == 6, f"Failed for '{s2}', expected 6, got {result2}"

    # Test Case 3: Single character
    s3 = "a"
    result3 = solution.countSubstrings(s3)
    assert result3 == 1, f"Failed for '{s3}', expected 1, got {result3}"

    # Test Case 4: No palindromes longer than 1
    s4 = "abc"
    result4 = solution.countSubstrings(s4)
    assert result4 == 3, f"Failed for '{s4}', expected 3, got {result4}"

    # Test Case 5: Mixed case
    s5 = "racecar"
    result5 = solution.countSubstrings(s5)
    assert result5 == 10, f"Failed for '{s5}', expected 10, got {result5}"

    # Test Case 6: Complex case
    s6 = "abccba"
    result6 = solution.countSubstrings(s6)
    assert result6 == 9, f"Failed for '{s6}', expected 9, got {result6}"

    # Test Case 7: Edge case
    s7 = "ab"
    result7 = solution.countSubstrings(s7)
    assert result7 == 2, f"Failed for '{s7}', expected 2, got {result7}"

    # Test Case 8: All same characters
    s8 = "aaaa"
    result8 = solution.countSubstrings(s8)
    assert result8 == 10, f"Failed for '{s8}', expected 10, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("Length\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create string with some palindromes
        s = "a" * (size // 2) + "b" * (size // 2)

        # Test approach
        start_time = time.time()
        result = solution.countSubstrings(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n^2) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n^2) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] / test_sizes[i - 1]) ** 2
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n^2): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^2)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n^2) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n^2), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^2)")
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
    result1 = solution.countSubstrings(s1)
    assert result1 == 1, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (1000 characters)
    s2 = "a" * 1000
    result2 = solution.countSubstrings(s2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same characters
    s3 = "z" * 100
    result3 = solution.countSubstrings(s3)
    assert result3 == 5050, f"All same characters failed: {result3}"
    print(f"All same characters: ✅")

    # Edge Case 4: No palindromes longer than 1
    s4 = "abcdefghijklmnopqrstuvwxyz"
    result4 = solution.countSubstrings(s4)
    assert result4 == 26, f"No long palindromes failed: {result4}"
    print(f"No long palindromes: ✅")

    # Edge Case 5: Alternating pattern
    s5 = "ababababab"
    result5 = solution.countSubstrings(s5)
    assert result5 == 10, f"Alternating pattern failed: {result5}"
    print(f"Alternating pattern: ✅")

    # Edge Case 6: Empty string (edge case)
    s6 = ""
    result6 = solution.countSubstrings(s6)
    assert result6 == 0, f"Empty string failed: {result6}"
    print(f"Empty string: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Palindromic Substrings:")

    # Large dataset
    s = "a" * 500 + "b" * 500

    start_time = time.time()
    result = solution.countSubstrings(s)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 characters):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Palindromic Substrings Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the countSubstrings method")
        print("- Aim for O(n^2) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^2)")
        print("- Consider using expand around centers approach")

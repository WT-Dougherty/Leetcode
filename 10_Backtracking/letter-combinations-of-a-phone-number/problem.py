"""
Letter Combinations of a Phone Number - LeetCode Problem 17

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.
"""

import time
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    digits1 = "23"
    result1 = solution.letterCombinations(digits1)
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert len(result1) == len(
        expected1
    ), f"Failed for '23', expected {len(expected1)} combinations, got {len(result1)}"
    for combo in expected1:
        assert combo in result1, f"Missing combination {combo} in result {result1}"

    # Test Case 2: Empty string
    digits2 = ""
    result2 = solution.letterCombinations(digits2)
    assert result2 == [], f"Failed for empty string, expected [], got {result2}"

    # Test Case 3: Single digit
    digits3 = "2"
    result3 = solution.letterCombinations(digits3)
    expected3 = ["a", "b", "c"]
    assert len(result3) == len(
        expected3
    ), f"Failed for '2', expected {len(expected3)} combinations, got {len(result3)}"
    for combo in expected3:
        assert combo in result3, f"Missing combination {combo} in result {result3}"

    # Test Case 4: Three digits
    digits4 = "234"
    result4 = solution.letterCombinations(digits4)
    expected4_count = 3 * 3 * 3  # 27 combinations
    assert (
        len(result4) == expected4_count
    ), f"Failed for '234', expected {expected4_count} combinations, got {len(result4)}"

    # Test Case 5: Four digits
    digits5 = "2345"
    result5 = solution.letterCombinations(digits5)
    expected5_count = 3 * 3 * 3 * 3  # 81 combinations
    assert (
        len(result5) == expected5_count
    ), f"Failed for '2345', expected {expected5_count} combinations, got {len(result5)}"

    # Test Case 6: Digits with 4 letters
    digits6 = "79"
    result6 = solution.letterCombinations(digits6)
    expected6_count = 4 * 4  # 16 combinations
    assert (
        len(result6) == expected6_count
    ), f"Failed for '79', expected {expected6_count} combinations, got {len(result6)}"

    # Test Case 7: All digits
    digits7 = "23456789"
    result7 = solution.letterCombinations(digits7)
    expected7_count = 3 * 3 * 3 * 3 * 3 * 3 * 4 * 4  # 3^6 * 4^2 = 729 * 16 = 11664
    assert (
        len(result7) == expected7_count
    ), f"Failed for all digits, expected {expected7_count} combinations, got {len(result7)}"

    # Test Case 8: Repeated digits
    digits8 = "22"
    result8 = solution.letterCombinations(digits8)
    expected8 = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
    assert len(result8) == len(
        expected8
    ), f"Failed for '22', expected {len(expected8)} combinations, got {len(result8)}"
    for combo in expected8:
        assert combo in result8, f"Missing combination {combo} in result {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [2, 3, 4]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        digits = "23456789"[:size]

        # Test approach
        start_time = time.time()
        result = solution.letterCombinations(digits)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} combinations")

    # Verify O(4^N) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(4^N) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = 4 ** (test_sizes[i] - test_sizes[i - 1])
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(4^N): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance for exponential complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(4^N)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(4^N) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(4^N), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(4^N)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 digit)
    digits1 = "2"
    result1 = solution.letterCombinations(digits1)
    assert len(result1) == 3, f"Single digit failed: {len(result1)}"
    print(f"Single digit: ✅")

    # Edge Case 2: Maximum constraint (4 digits)
    digits2 = "2345"
    result2 = solution.letterCombinations(digits2)
    assert len(result2) == 81, f"Max constraint failed: {len(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same digits
    digits3 = "2222"
    result3 = solution.letterCombinations(digits3)
    assert len(result3) == 81, f"All same digits failed: {len(result3)}"
    print(f"All same digits: ✅")

    # Edge Case 4: Digits with 4 letters
    digits4 = "79"
    result4 = solution.letterCombinations(digits4)
    assert len(result4) == 16, f"Digits with 4 letters failed: {len(result4)}"
    print(f"Digits with 4 letters: ✅")

    # Edge Case 5: Mixed digits
    digits5 = "23456789"
    result5 = solution.letterCombinations(digits5)
    assert len(result5) == 11664, f"Mixed digits failed: {len(result5)}"
    print(f"Mixed digits: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Letter Combinations:")

    # Large dataset
    digits = "23456789"

    start_time = time.time()
    result = solution.letterCombinations(digits)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (8 digits):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} combinations")


if __name__ == "__main__":
    print("🧪 Testing Letter Combinations of a Phone Number Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the letterCombinations method")
        print("- Aim for O(4^N) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(4^N)")
        print("- Consider using backtracking approach")

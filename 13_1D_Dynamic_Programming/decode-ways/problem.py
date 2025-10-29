"""
Decode Ways - LeetCode Problem 91

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

import time


class Solution:
    def numDecodings(self, s: str) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    result1 = solution.numDecodings("12")
    assert result1 == 2, f"Failed for '12', expected 2, got {result1}"

    # Test Case 2: Three ways
    result2 = solution.numDecodings("226")
    assert result2 == 3, f"Failed for '226', expected 3, got {result2}"

    # Test Case 3: Invalid case
    result3 = solution.numDecodings("06")
    assert result3 == 0, f"Failed for '06', expected 0, got {result3}"

    # Test Case 4: Single digit
    result4 = solution.numDecodings("1")
    assert result4 == 1, f"Failed for '1', expected 1, got {result4}"

    # Test Case 5: Two digits
    result5 = solution.numDecodings("27")
    assert result5 == 1, f"Failed for '27', expected 1, got {result5}"

    # Test Case 6: Complex case
    result6 = solution.numDecodings("11106")
    assert result6 == 2, f"Failed for '11106', expected 2, got {result6}"

    # Test Case 7: All valid
    result7 = solution.numDecodings("1111")
    assert result7 == 5, f"Failed for '1111', expected 5, got {result7}"

    # Test Case 8: Large case
    result8 = solution.numDecodings("123456789")
    assert result8 == 3, f"Failed for '123456789', expected 3, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Length\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create valid digit string
        s = "1" * size

        # Test approach
        start_time = time.time()
        result = solution.numDecodings(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity
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

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n) complexity")
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

    # Edge Case 1: Minimum constraint (1 character)
    result1 = solution.numDecodings("1")
    assert result1 == 1, f"Single character failed: {result1}"
    print(f"Single character: ✅")

    # Edge Case 2: Maximum constraint (100 characters)
    s2 = "1" * 100
    result2 = solution.numDecodings(s2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All zeros
    result3 = solution.numDecodings("000")
    assert result3 == 0, f"All zeros failed: {result3}"
    print(f"All zeros: ✅")

    # Edge Case 4: Leading zero
    result4 = solution.numDecodings("01")
    assert result4 == 0, f"Leading zero failed: {result4}"
    print(f"Leading zero: ✅")

    # Edge Case 5: All valid pairs
    result5 = solution.numDecodings("1212")
    assert result5 == 5, f"All valid pairs failed: {result5}"
    print(f"All valid pairs: ✅")

    # Edge Case 6: Invalid pairs
    result6 = solution.numDecodings("789")
    assert result6 == 1, f"Invalid pairs failed: {result6}"
    print(f"Invalid pairs: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Decode Ways:")

    # Large dataset
    s = "1" * 50

    start_time = time.time()
    result = solution.numDecodings(s)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (length=50):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Decode Ways Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the numDecodings method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming")

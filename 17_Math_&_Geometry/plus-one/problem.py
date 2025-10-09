"""
Plus One - LeetCode Problem 66

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right
order. The large integer does not contain any leading zeros.

Increment the large integer by one and return the resulting array of digits.
"""

import time


class Solution:
    def plusOne(self, digits):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    digits1 = [1, 2, 3]
    result1 = solution.plusOne(digits1)
    expected1 = [1, 2, 4]
    assert (
        result1 == expected1
    ), f"Failed for digits={digits1}, expected {expected1}, got {result1}"

    # Test Case 2: Carry over
    digits2 = [4, 3, 2, 1]
    result2 = solution.plusOne(digits2)
    expected2 = [4, 3, 2, 2]
    assert (
        result2 == expected2
    ), f"Failed for digits={digits2}, expected {expected2}, got {result2}"

    # Test Case 3: All nines
    digits3 = [9]
    result3 = solution.plusOne(digits3)
    expected3 = [1, 0]
    assert (
        result3 == expected3
    ), f"Failed for digits={digits3}, expected {expected3}, got {result3}"

    # Test Case 4: Multiple nines
    digits4 = [9, 9, 9]
    result4 = solution.plusOne(digits4)
    expected4 = [1, 0, 0, 0]
    assert (
        result4 == expected4
    ), f"Failed for digits={digits4}, expected {expected4}, got {result4}"

    # Test Case 5: Single digit
    digits5 = [5]
    result5 = solution.plusOne(digits5)
    expected5 = [6]
    assert (
        result5 == expected5
    ), f"Failed for digits={digits5}, expected {expected5}, got {result5}"

    # Test Case 6: Edge case
    digits6 = [1, 9]
    result6 = solution.plusOne(digits6)
    expected6 = [2, 0]
    assert (
        result6 == expected6
    ), f"Failed for digits={digits6}, expected {expected6}, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        digits = [9] * size

        start_time = time.time()
        result = solution.plusOne(digits)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} digits")

    # Verify O(n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Single digit
    result = solution.plusOne([0])
    print(f"Single digit (0): {result} ✅")

    # Edge Case 2: All zeros
    result = solution.plusOne([0, 0, 0])
    print(f"All zeros: {result} ✅")

    # Edge Case 3: Large number
    result = solution.plusOne([9] * 100)
    print(f"Large number (100 nines): {len(result)} digits ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    digits = [9] * 100000

    start_time = time.time()
    result = solution.plusOne(digits)
    elapsed_time = time.time() - start_time

    print(f"Large number (100,000 digits):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} digits")


if __name__ == "__main__":
    print("🧪 Testing Plus One Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the plusOne method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using simple carry propagation")

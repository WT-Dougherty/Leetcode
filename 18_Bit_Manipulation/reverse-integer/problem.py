"""
Reverse Integer - LeetCode Problem 7

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

import time


class Solution:
    def reverse(self, x):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    x1 = 123
    result1 = solution.reverse(x1)
    assert result1 == 321, f"Failed for x={x1}, expected 321, got {result1}"

    # Test Case 2: Negative number
    x2 = -123
    result2 = solution.reverse(x2)
    assert result2 == -321, f"Failed for x={x2}, expected -321, got {result2}"

    # Test Case 3: Trailing zeros
    x3 = 120
    result3 = solution.reverse(x3)
    assert result3 == 21, f"Failed for x={x3}, expected 21, got {result3}"

    # Test Case 4: Single digit
    x4 = 5
    result4 = solution.reverse(x4)
    assert result4 == 5, f"Failed for x={x4}, expected 5, got {result4}"

    # Test Case 5: Overflow case
    x5 = 1534236469
    result5 = solution.reverse(x5)
    assert result5 == 0, f"Failed for x={x5}, expected 0, got {result5}"

    # Test Case 6: Edge case
    x6 = 0
    result6 = solution.reverse(x6)
    assert result6 == 0, f"Failed for x={x6}, expected 0, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        x = size

        start_time = time.time()
        result = solution.reverse(x)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(log n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i].bit_length()) / (
                test_sizes[i - 1].bit_length()
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Zero
    result = solution.reverse(0)
    print(f"Zero: {result} ✅")

    # Edge Case 2: Single digit
    result = solution.reverse(7)
    print(f"Single digit: {result} ✅")

    # Edge Case 3: Large number
    result = solution.reverse(2147483647)
    print(f"Large number: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    x = 123456789

    start_time = time.time()
    result = solution.reverse(x)
    elapsed_time = time.time() - start_time

    print(f"Large number ({x}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Reverse Integer Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the reverse method")
        print("- Aim for O(log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using mathematical approach")

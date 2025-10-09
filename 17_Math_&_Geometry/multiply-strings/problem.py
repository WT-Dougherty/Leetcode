"""
Multiply Strings - LeetCode Problem 43

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integers directly.
"""

import time


class Solution:
    def multiply(self, num1, num2):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    num1_1 = "2"
    num2_1 = "3"
    result1 = solution.multiply(num1_1, num2_1)
    assert (
        result1 == "6"
    ), f"Failed for num1='{num1_1}', num2='{num2_1}', expected '6', got '{result1}'"

    # Test Case 2: Complex case
    num1_2 = "123"
    num2_2 = "456"
    result2 = solution.multiply(num1_2, num2_2)
    assert (
        result2 == "56088"
    ), f"Failed for num1='{num1_2}', num2='{num2_2}', expected '56088', got '{result2}'"

    # Test Case 3: Single digit
    num1_3 = "9"
    num2_3 = "9"
    result3 = solution.multiply(num1_3, num2_3)
    assert (
        result3 == "81"
    ), f"Failed for num1='{num1_3}', num2='{num2_3}', expected '81', got '{result3}'"

    # Test Case 4: Zero
    num1_4 = "0"
    num2_4 = "123"
    result4 = solution.multiply(num1_4, num2_4)
    assert (
        result4 == "0"
    ), f"Failed for num1='{num1_4}', num2='{num2_4}', expected '0', got '{result4}'"

    # Test Case 5: Large numbers
    num1_5 = "999"
    num2_5 = "999"
    result5 = solution.multiply(num1_5, num2_5)
    assert (
        result5 == "998001"
    ), f"Failed for num1='{num1_5}', num2='{num2_5}', expected '998001', got '{result5}'"

    # Test Case 6: Edge case
    num1_6 = "1"
    num2_6 = "1"
    result6 = solution.multiply(num1_6, num2_6)
    assert (
        result6 == "1"
    ), f"Failed for num1='{num1_6}', num2='{num2_6}', expected '1', got '{result6}'"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m * n)"""
    solution = Solution()

    test_sizes = [50, 100, 200]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        num1 = "9" * size
        num2 = "9" * size

        start_time = time.time()
        result = solution.multiply(num1, num2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} digits")

    # Verify O(m * n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] * test_sizes[i]) / (
                test_sizes[i - 1] * test_sizes[i - 1]
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m * n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(m * n), but got worse complexity"
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

    # Edge Case 1: Zero
    result = solution.multiply("0", "123")
    print(f"Zero multiplication: {result} ✅")

    # Edge Case 2: Single digits
    result = solution.multiply("5", "6")
    print(f"Single digits: {result} ✅")

    # Edge Case 3: Large numbers
    result = solution.multiply("999999", "999999")
    print(f"Large numbers: {len(result)} digits ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large numbers
    num1 = "9" * 200
    num2 = "9" * 200

    start_time = time.time()
    result = solution.multiply(num1, num2)
    elapsed_time = time.time() - start_time

    print(f"Large numbers (200 digits each):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} digits")


if __name__ == "__main__":
    print("🧪 Testing Multiply Strings Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the multiply method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using grade school multiplication algorithm")

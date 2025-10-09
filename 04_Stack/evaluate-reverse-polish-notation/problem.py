"""
Evaluate Reverse Polish Notation - LeetCode Problem 150

You are given an array of strings tokens that represents an arithmetic expression in a
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero operation.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

import time
import random


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    tokens1 = ["2", "1", "+", "3", "*"]
    result1 = solution.evalRPN(tokens1)
    assert result1 == 9, f"Failed for {tokens1}, expected 9, got {result1}"

    # Test Case 2: Division case
    tokens2 = ["4", "13", "5", "/", "+"]
    result2 = solution.evalRPN(tokens2)
    assert result2 == 6, f"Failed for {tokens2}, expected 6, got {result2}"

    # Test Case 3: Complex case
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result3 = solution.evalRPN(tokens3)
    assert result3 == 22, f"Failed for {tokens3}, expected 22, got {result3}"

    # Test Case 4: Single number
    tokens4 = ["42"]
    result4 = solution.evalRPN(tokens4)
    assert result4 == 42, f"Failed for {tokens4}, expected 42, got {result4}"

    # Test Case 5: Simple addition
    tokens5 = ["3", "4", "+"]
    result5 = solution.evalRPN(tokens5)
    assert result5 == 7, f"Failed for {tokens5}, expected 7, got {result5}"

    # Test Case 6: Simple subtraction
    tokens6 = ["5", "3", "-"]
    result6 = solution.evalRPN(tokens6)
    assert result6 == 2, f"Failed for {tokens6}, expected 2, got {result6}"

    # Test Case 7: Simple multiplication
    tokens7 = ["4", "5", "*"]
    result7 = solution.evalRPN(tokens7)
    assert result7 == 20, f"Failed for {tokens7}, expected 20, got {result7}"

    # Test Case 8: Simple division
    tokens8 = ["15", "3", "/"]
    result8 = solution.evalRPN(tokens8)
    assert result8 == 5, f"Failed for {tokens8}, expected 5, got {result8}"

    # Test Case 9: Division truncation
    tokens9 = ["7", "3", "/"]
    result9 = solution.evalRPN(tokens9)
    assert result9 == 2, f"Failed for {tokens9}, expected 2, got {result9}"

    # Test Case 10: Negative numbers
    tokens10 = ["-2", "3", "*"]
    result10 = solution.evalRPN(tokens10)
    assert result10 == -6, f"Failed for {tokens10}, expected -6, got {result10}"

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
        # Generate test data - valid RPN expression
        tokens = []
        numbers = [str(random.randint(-200, 200)) for _ in range(size // 2)]
        operators = ["+", "-", "*", "/"]

        # Create valid RPN: numbers followed by operators
        for i in range(len(numbers)):
            tokens.append(numbers[i])
            if i > 0 and i % 2 == 1:  # Add operator every 2 numbers
                tokens.append(random.choice(operators))

        # Test approach
        start_time = time.time()
        result = solution.evalRPN(tokens)
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
    tokens = ["1"] * 5000 + ["+"] * 4999
    result = solution.evalRPN(tokens)
    print(f"Maximum length (10k tokens): {result} ✅")

    # Edge Case 2: Maximum constraint values
    tokens = ["200", "200", "+"]
    result = solution.evalRPN(tokens)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    tokens = ["-200", "-200", "+"]
    result = solution.evalRPN(tokens)
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: Division by small numbers
    tokens = ["100", "1", "/"]
    result = solution.evalRPN(tokens)
    print(f"Division by 1: {result} ✅")

    # Edge Case 5: Large intermediate results
    tokens = ["200", "200", "*", "200", "*"]
    result = solution.evalRPN(tokens)
    print(f"Large intermediate results: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    tokens = []
    numbers = [str(random.randint(-200, 200)) for _ in range(50000)]
    operators = ["+", "-", "*", "/"]

    # Create valid RPN
    for i in range(len(numbers)):
        tokens.append(numbers[i])
        if i > 0 and i % 2 == 1:
            tokens.append(random.choice(operators))

    start_time = time.time()
    result = solution.evalRPN(tokens)
    time1 = time.time() - start_time

    print(f"Large dataset (100k tokens):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Evaluate Reverse Polish Notation Problem")
    print("=" * 70)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the evalRPN method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use stack data structure")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using stack data structure")

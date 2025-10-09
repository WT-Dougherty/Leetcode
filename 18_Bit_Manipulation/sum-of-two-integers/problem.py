"""
Sum of Two Integers - LeetCode Problem 371

Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

import time


class Solution:
    def getSum(self, a, b):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    a1, b1 = 1, 2
    result1 = solution.getSum(a1, b1)
    assert result1 == 3, f"Failed for a={a1}, b={b1}, expected 3, got {result1}"

    # Test Case 2: Another case
    a2, b2 = 2, 3
    result2 = solution.getSum(a2, b2)
    assert result2 == 5, f"Failed for a={a2}, b={b2}, expected 5, got {result2}"

    # Test Case 3: Negative numbers
    a3, b3 = -1, 1
    result3 = solution.getSum(a3, b3)
    assert result3 == 0, f"Failed for a={a3}, b={b3}, expected 0, got {result3}"

    # Test Case 4: Both negative
    a4, b4 = -1, -1
    result4 = solution.getSum(a4, b4)
    assert result4 == -2, f"Failed for a={a4}, b={b4}, expected -2, got {result4}"

    # Test Case 5: Zero
    a5, b5 = 0, 0
    result5 = solution.getSum(a5, b5)
    assert result5 == 0, f"Failed for a={a5}, b={b5}, expected 0, got {result5}"

    # Test Case 6: Edge case
    a6, b6 = 0, 1
    result6 = solution.getSum(a6, b6)
    assert result6 == 1, f"Failed for a={a6}, b={b6}, expected 1, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(1)"""
    solution = Solution()

    test_values = [(100, 200), (1000, 2000), (10000, 20000)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Values\t\tTime\t\tResult")
    print("-" * 50)

    for a, b in test_values:
        start_time = time.time()
        result = solution.getSum(a, b)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"({a}, {b})\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(1) complexity - should be very fast
    max_time = max(times)
    if max_time > 0.001:  # More than 1ms is suspicious for O(1)
        print(f"\n❌ FAILED: Time complexity appears worse than O(1)")
        print(f"Max time: {max_time:.6f}s (should be < 0.001s)")
        raise AssertionError(
            "Time complexity test failed: expected O(1), but got worse complexity"
        )

    print(f"\n✅ PASSED: Time complexity appears to be O(1)")
    return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Zero
    result = solution.getSum(0, 0)
    print(f"Zero: {result} ✅")

    # Edge Case 2: Negative numbers
    result = solution.getSum(-5, -3)
    print(f"Negative numbers: {result} ✅")

    # Edge Case 3: Large numbers
    result = solution.getSum(1000, 2000)
    print(f"Large numbers: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large numbers
    a, b = 1000000, 2000000

    start_time = time.time()
    result = solution.getSum(a, b)
    elapsed_time = time.time() - start_time

    print(f"Large numbers ({a}, {b}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Sum of Two Integers Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the getSum method")
        print("- Aim for O(1) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(1)")
        print("- Consider using bit manipulation techniques")

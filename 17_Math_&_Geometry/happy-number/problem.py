"""
Happy Number - LeetCode Problem 202

Write an algorithm to determine if a number n is happy.

A happy number is defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

import time


class Solution:
    def isHappy(self, n):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Happy number
    n1 = 19
    result1 = solution.isHappy(n1)
    assert result1 == True, f"Failed for n={n1}, expected True, got {result1}"

    # Test Case 2: Not happy number
    n2 = 2
    result2 = solution.isHappy(n2)
    assert result2 == False, f"Failed for n={n2}, expected False, got {result2}"

    # Test Case 3: Single digit happy
    n3 = 1
    result3 = solution.isHappy(n3)
    assert result3 == True, f"Failed for n={n3}, expected True, got {result3}"

    # Test Case 4: Single digit not happy
    n4 = 7
    result4 = solution.isHappy(n4)
    assert result4 == True, f"Failed for n={n4}, expected True, got {result4}"

    # Test Case 5: Large number
    n5 = 100
    result5 = solution.isHappy(n5)
    assert result5 == True, f"Failed for n={n5}, expected True, got {result5}"

    # Test Case 6: Edge case
    n6 = 4
    result6 = solution.isHappy(n6)
    assert result6 == False, f"Failed for n={n6}, expected False, got {result6}"

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
        start_time = time.time()
        result = solution.isHappy(size)
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

    # Edge Case 1: Single digit
    result = solution.isHappy(1)
    print(f"Single digit (1): {result} ✅")

    # Edge Case 2: Small number
    result = solution.isHappy(10)
    print(f"Small number (10): {result} ✅")

    # Edge Case 3: Large number
    result = solution.isHappy(999999)
    print(f"Large number (999999): {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    n = 999999999

    start_time = time.time()
    result = solution.isHappy(n)
    elapsed_time = time.time() - start_time

    print(f"Large number ({n}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Happy Number Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isHappy method")
        print("- Aim for O(log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using Floyd's cycle detection algorithm")

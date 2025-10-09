"""
Climbing Stairs - LeetCode Problem 70

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

import time
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    result1 = solution.climbStairs(2)
    assert result1 == 2, f"Failed for n=2, expected 2, got {result1}"

    # Test Case 2: Three steps
    result2 = solution.climbStairs(3)
    assert result2 == 3, f"Failed for n=3, expected 3, got {result2}"

    # Test Case 3: Four steps
    result3 = solution.climbStairs(4)
    assert result3 == 5, f"Failed for n=4, expected 5, got {result3}"

    # Test Case 4: Five steps
    result4 = solution.climbStairs(5)
    assert result4 == 8, f"Failed for n=5, expected 8, got {result4}"

    # Test Case 5: Six steps
    result5 = solution.climbStairs(6)
    assert result5 == 13, f"Failed for n=6, expected 13, got {result5}"

    # Test Case 6: Single step
    result6 = solution.climbStairs(1)
    assert result6 == 1, f"Failed for n=1, expected 1, got {result6}"

    # Test Case 7: Larger case
    result7 = solution.climbStairs(10)
    assert result7 == 89, f"Failed for n=10, expected 89, got {result7}"

    # Test Case 8: Maximum constraint
    result8 = solution.climbStairs(45)
    assert result8 == 1836311903, f"Failed for n=45, expected 1836311903, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 20, 30]
    times = []

    print("\nTime Complexity Analysis:")
    print("n\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Test approach
        start_time = time.time()
        result = solution.climbStairs(size)
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

    # Edge Case 1: Minimum constraint (1 step)
    result1 = solution.climbStairs(1)
    assert result1 == 1, f"Single step failed: {result1}"
    print(f"Single step: ✅")

    # Edge Case 2: Maximum constraint (45 steps)
    result2 = solution.climbStairs(45)
    assert result2 == 1836311903, f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Two steps
    result3 = solution.climbStairs(2)
    assert result3 == 2, f"Two steps failed: {result3}"
    print(f"Two steps: ✅")

    # Edge Case 4: Medium case
    result4 = solution.climbStairs(20)
    assert result4 == 10946, f"Medium case failed: {result4}"
    print(f"Medium case: ✅")

    # Edge Case 5: Fibonacci pattern verification
    for i in range(1, 11):
        result = solution.climbStairs(i)
        # Verify it follows Fibonacci pattern
        if i == 1:
            expected = 1
        elif i == 2:
            expected = 2
        else:
            prev1 = solution.climbStairs(i - 1)
            prev2 = solution.climbStairs(i - 2)
            expected = prev1 + prev2
        assert result == expected, f"Fibonacci pattern failed for n={i}"
    print(f"Fibonacci pattern: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Climbing Stairs:")

    # Large dataset
    n = 45

    start_time = time.time()
    result = solution.climbStairs(n)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (n=45):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Climbing Stairs Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the climbStairs method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming or Fibonacci approach")

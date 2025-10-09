"""
Unique Paths - LeetCode Problem 62

There is a robot on an m x n grid. The robot is initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot
can take to reach the bottom-right corner.

The testcases are generated so that the answer will fit in a 32-bit integer.
"""

import time


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    m1, n1 = 3, 7
    result1 = solution.uniquePaths(m1, n1)
    assert result1 == 28, f"Failed for m={m1}, n={n1}, expected 28, got {result1}"

    # Test Case 2: Small case
    m2, n2 = 3, 2
    result2 = solution.uniquePaths(m2, n2)
    assert result2 == 3, f"Failed for m={m2}, n={n2}, expected 3, got {result2}"

    # Test Case 3: Single row
    m3, n3 = 1, 1
    result3 = solution.uniquePaths(m3, n3)
    assert result3 == 1, f"Failed for m={m3}, n={n3}, expected 1, got {result3}"

    # Test Case 4: Single column
    m4, n4 = 1, 1
    result4 = solution.uniquePaths(m4, n4)
    assert result4 == 1, f"Failed for m={m4}, n={n4}, expected 1, got {result4}"

    # Test Case 5: Square case
    m5, n5 = 2, 2
    result5 = solution.uniquePaths(m5, n5)
    assert result5 == 2, f"Failed for m={m5}, n={n5}, expected 2, got {result5}"

    # Test Case 6: Large case
    m6, n6 = 7, 3
    result6 = solution.uniquePaths(m6, n6)
    assert result6 == 28, f"Failed for m={m6}, n={n6}, expected 28, got {result6}"

    # Test Case 7: Edge case
    m7, n7 = 1, 10
    result7 = solution.uniquePaths(m7, n7)
    assert result7 == 1, f"Failed for m={m7}, n={n7}, expected 1, got {result7}"

    # Test Case 8: Another case
    m8, n8 = 10, 1
    result8 = solution.uniquePaths(m8, n8)
    assert result8 == 1, f"Failed for m={m8}, n={n8}, expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [20, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("m\tn\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        m, n = size, size

        # Test approach
        start_time = time.time()
        result = solution.uniquePaths(m, n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{m}\t{n}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * test_sizes[i - 1]
            curr_complexity = test_sizes[i] * test_sizes[i]
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m*n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(m * n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m * n), but got worse complexity"
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

    # Edge Case 1: Minimum constraint (1x1)
    m1, n1 = 1, 1
    result1 = solution.uniquePaths(m1, n1)
    assert result1 == 1, f"Single cell failed: {result1}"
    print(f"Single cell: ✅")

    # Edge Case 2: Maximum constraint (100x100)
    m2, n2 = 100, 100
    result2 = solution.uniquePaths(m2, n2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Single row
    m3, n3 = 1, 100
    result3 = solution.uniquePaths(m3, n3)
    assert result3 == 1, f"Single row failed: {result3}"
    print(f"Single row: ✅")

    # Edge Case 4: Single column
    m4, n4 = 100, 1
    result4 = solution.uniquePaths(m4, n4)
    assert result4 == 1, f"Single column failed: {result4}"
    print(f"Single column: ✅")

    # Edge Case 5: Square case
    m5, n5 = 10, 10
    result5 = solution.uniquePaths(m5, n5)
    assert result5 == 48620, f"Square case failed: {result5}"
    print(f"Square case: ✅")

    # Edge Case 6: Rectangle case
    m6, n6 = 5, 10
    result6 = solution.uniquePaths(m6, n6)
    assert result6 == 715, f"Rectangle case failed: {result6}"
    print(f"Rectangle case: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Unique Paths:")

    # Large dataset
    m, n = 50, 50

    start_time = time.time()
    result = solution.uniquePaths(m, n)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (m={m}, n={n}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Unique Paths Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the uniquePaths method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using dynamic programming")

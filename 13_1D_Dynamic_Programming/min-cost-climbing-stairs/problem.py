"""
Min Cost Climbing Stairs - LeetCode Problem 746

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

import time
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    cost1 = [10, 15, 20]
    result1 = solution.minCostClimbingStairs(cost1)
    assert result1 == 15, f"Failed for {cost1}, expected 15, got {result1}"

    # Test Case 2: Complex case
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result2 = solution.minCostClimbingStairs(cost2)
    assert result2 == 6, f"Failed for {cost2}, expected 6, got {result2}"

    # Test Case 3: Two steps
    cost3 = [10, 15]
    result3 = solution.minCostClimbingStairs(cost3)
    assert result3 == 10, f"Failed for {cost3}, expected 10, got {result3}"

    # Test Case 4: Three steps
    cost4 = [1, 2, 3]
    result4 = solution.minCostClimbingStairs(cost4)
    assert result4 == 2, f"Failed for {cost4}, expected 2, got {result4}"

    # Test Case 5: Four steps
    cost5 = [1, 2, 3, 4]
    result5 = solution.minCostClimbingStairs(cost5)
    assert result5 == 4, f"Failed for {cost5}, expected 4, got {result5}"

    # Test Case 6: All same cost
    cost6 = [5, 5, 5, 5]
    result6 = solution.minCostClimbingStairs(cost6)
    assert result6 == 10, f"Failed for {cost6}, expected 10, got {result6}"

    # Test Case 7: Increasing cost
    cost7 = [1, 2, 3, 4, 5]
    result7 = solution.minCostClimbingStairs(cost7)
    assert result7 == 6, f"Failed for {cost7}, expected 6, got {result7}"

    # Test Case 8: Decreasing cost
    cost8 = [5, 4, 3, 2, 1]
    result8 = solution.minCostClimbingStairs(cost8)
    assert result8 == 6, f"Failed for {cost8}, expected 6, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create array with random costs
        cost = [i % 10 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.minCostClimbingStairs(cost)
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

    # Edge Case 1: Minimum constraint (2 steps)
    cost1 = [1, 2]
    result1 = solution.minCostClimbingStairs(cost1)
    assert result1 == 1, f"Two steps failed: {result1}"
    print(f"Two steps: ✅")

    # Edge Case 2: Maximum constraint (1000 steps)
    cost2 = [i % 999 + 1 for i in range(1000)]
    result2 = solution.minCostClimbingStairs(cost2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum cost (999)
    cost3 = [999, 999]
    result3 = solution.minCostClimbingStairs(cost3)
    assert result3 == 999, f"Max cost failed: {result3}"
    print(f"Maximum cost: ✅")

    # Edge Case 4: Minimum cost (0)
    cost4 = [0, 0]
    result4 = solution.minCostClimbingStairs(cost4)
    assert result4 == 0, f"Min cost failed: {result4}"
    print(f"Minimum cost: ✅")

    # Edge Case 5: All zeros
    cost5 = [0, 0, 0, 0]
    result5 = solution.minCostClimbingStairs(cost5)
    assert result5 == 0, f"All zeros failed: {result5}"
    print(f"All zeros: ✅")

    # Edge Case 6: Alternating pattern
    cost6 = [1, 2, 1, 2, 1, 2]
    result6 = solution.minCostClimbingStairs(cost6)
    assert result6 == 4, f"Alternating pattern failed: {result6}"
    print(f"Alternating pattern: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Min Cost Climbing Stairs:")

    # Large dataset
    cost = [i % 10 + 1 for i in range(1000)]

    start_time = time.time()
    result = solution.minCostClimbingStairs(cost)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 steps):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Min Cost Climbing Stairs Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minCostClimbingStairs method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming")

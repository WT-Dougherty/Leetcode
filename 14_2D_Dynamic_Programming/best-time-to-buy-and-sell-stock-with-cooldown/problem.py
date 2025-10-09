"""
Best Time to Buy and Sell Stock with Cooldown - LeetCode Problem 309

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    prices1 = [1, 2, 3, 0, 2]
    result1 = solution.maxProfit(prices1)
    assert result1 == 3, f"Failed for {prices1}, expected 3, got {result1}"

    # Test Case 2: Single day
    prices2 = [1]
    result2 = solution.maxProfit(prices2)
    assert result2 == 0, f"Failed for {prices2}, expected 0, got {result2}"

    # Test Case 3: Two days
    prices3 = [1, 2]
    result3 = solution.maxProfit(prices3)
    assert result3 == 1, f"Failed for {prices3}, expected 1, got {result3}"

    # Test Case 4: Decreasing prices
    prices4 = [3, 2, 1]
    result4 = solution.maxProfit(prices4)
    assert result4 == 0, f"Failed for {prices4}, expected 0, got {result4}"

    # Test Case 5: Increasing prices
    prices5 = [1, 2, 3, 4, 5]
    result5 = solution.maxProfit(prices5)
    assert result5 == 4, f"Failed for {prices5}, expected 4, got {result5}"

    # Test Case 6: Complex case
    prices6 = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    result6 = solution.maxProfit(prices6)
    assert result6 == 15, f"Failed for {prices6}, expected 15, got {result6}"

    # Test Case 7: All same prices
    prices7 = [5, 5, 5, 5]
    result7 = solution.maxProfit(prices7)
    assert result7 == 0, f"Failed for {prices7}, expected 0, got {result7}"

    # Test Case 8: Edge case
    prices8 = [2, 1, 4]
    result8 = solution.maxProfit(prices8)
    assert result8 == 3, f"Failed for {prices8}, expected 3, got {result8}"

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
        # Generate test data - create array with random prices
        prices = [i % 100 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.maxProfit(prices)
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

    # Edge Case 1: Minimum constraint (1 day)
    prices1 = [100]
    result1 = solution.maxProfit(prices1)
    assert result1 == 0, f"Single day failed: {result1}"
    print(f"Single day: ✅")

    # Edge Case 2: Maximum constraint (5000 days)
    prices2 = [i % 1000 + 1 for i in range(5000)]
    result2 = solution.maxProfit(prices2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum price (1000)
    prices3 = [1000, 999, 1000]
    result3 = solution.maxProfit(prices3)
    assert result3 == 1, f"Max price failed: {result3}"
    print(f"Maximum price: ✅")

    # Edge Case 4: Minimum price (0)
    prices4 = [0, 1, 0]
    result4 = solution.maxProfit(prices4)
    assert result4 == 1, f"Min price failed: {result4}"
    print(f"Minimum price: ✅")

    # Edge Case 5: Alternating pattern
    prices5 = [1, 2, 1, 2, 1, 2]
    result5 = solution.maxProfit(prices5)
    assert result5 == 2, f"Alternating pattern failed: {result5}"
    print(f"Alternating pattern: ✅")

    # Edge Case 6: All zeros
    prices6 = [0, 0, 0, 0]
    result6 = solution.maxProfit(prices6)
    assert result6 == 0, f"All zeros failed: {result6}"
    print(f"All zeros: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Best Time to Buy and Sell Stock with Cooldown:")

    # Large dataset
    prices = [i % 100 + 1 for i in range(1000)]

    start_time = time.time()
    result = solution.maxProfit(prices)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 days):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Best Time to Buy and Sell Stock with Cooldown Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxProfit method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming with state tracking")

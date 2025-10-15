"""
Best Time to Buy and Sell Stock - LeetCode Problem 121

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.
"""

import time
import random
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            max_profit = max(max_profit, prices[right] - prices[left])
            if left == right:
                right += 1
            elif prices[left] > prices[right]:
                left += 1
            else:
                right += 1
        return max_profit


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    assert result1 == 5, f"Failed for {prices1}, expected 5, got {result1}"

    # Test Case 2: No profit
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    assert result2 == 0, f"Failed for {prices2}, expected 0, got {result2}"

    # Test Case 3: Single day
    prices3 = [1]
    result3 = solution.maxProfit(prices3)
    assert result3 == 0, f"Failed for {prices3}, expected 0, got {result3}"

    # Test Case 4: Two days - profit
    prices4 = [1, 2]
    result4 = solution.maxProfit(prices4)
    assert result4 == 1, f"Failed for {prices4}, expected 1, got {result4}"

    # Test Case 5: Two days - no profit
    prices5 = [2, 1]
    result5 = solution.maxProfit(prices5)
    assert result5 == 0, f"Failed for {prices5}, expected 0, got {result5}"

    # Test Case 6: All same prices
    prices6 = [5, 5, 5, 5]
    result6 = solution.maxProfit(prices6)
    assert result6 == 0, f"Failed for {prices6}, expected 0, got {result6}"

    # Test Case 7: Increasing prices
    prices7 = [1, 2, 3, 4, 5]
    result7 = solution.maxProfit(prices7)
    assert result7 == 4, f"Failed for {prices7}, expected 4, got {result7}"

    # Test Case 8: Decreasing prices
    prices8 = [5, 4, 3, 2, 1]
    result8 = solution.maxProfit(prices8)
    assert result8 == 0, f"Failed for {prices8}, expected 0, got {result8}"

    # Test Case 9: Large profit
    prices9 = [1, 100]
    result9 = solution.maxProfit(prices9)
    assert result9 == 99, f"Failed for {prices9}, expected 99, got {result9}"

    # Test Case 10: Complex case
    prices10 = [3, 3, 5, 0, 0, 3, 1, 4]
    result10 = solution.maxProfit(prices10)
    assert result10 == 4, f"Failed for {prices10}, expected 4, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tMax Profit")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        prices = [random.randint(0, 10000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.maxProfit(prices)
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

    # Edge Case 1: Minimum length
    prices = [1]
    result = solution.maxProfit(prices)
    print(f"Minimum length: {result} ✅")

    # Edge Case 2: Maximum constraint values
    prices = [10000] * 100000
    result = solution.maxProfit(prices)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: All zeros
    prices = [0] * 1000
    result = solution.maxProfit(prices)
    print(f"All zeros: {result} ✅")

    # Edge Case 4: Alternating pattern
    prices = [1, 10000] * 500
    result = solution.maxProfit(prices)
    print(f"Alternating pattern: {result} ✅")

    # Edge Case 5: Single peak
    prices = [1] * 500 + [10000] + [1] * 500
    result = solution.maxProfit(prices)
    print(f"Single peak: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    prices = [random.randint(0, 10000) for _ in range(100000)]

    start_time = time.time()
    result = solution.maxProfit(prices)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 elements):")
    print(f"Time: {time1:.6f}s, Max profit: {result}")


if __name__ == "__main__":
    print("🧪 Testing Best Time to Buy and Sell Stock Problem")
    print("=" * 70)

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
        print("- Use sliding window or two pointers approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using sliding window or tracking minimum price")
